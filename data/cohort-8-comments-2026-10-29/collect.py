"""Read-only GitHub collection; run with an authenticated gh CLI. Resumes raw files."""
import argparse
import concurrent.futures
import datetime
import json
import re
from pathlib import Path
import subprocess
import time

def configure():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, help='Repository: OWNER/REPO')
    parser.add_argument('--project', required=True, help='Organization project: OWNER/NUMBER')
    parser.add_argument('--output', required=True, type=Path, help='Snapshot directory; same scope resumes cached raw files')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo):
        parser.error('--repo must be OWNER/REPO')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[1-9][0-9]*', args.project):
        parser.error('--project must be OWNER/NUMBER with a positive number')
    global ROOT, RAW, REPO, QUERY, PROJECT
    ROOT = args.output.expanduser().resolve()
    RAW = ROOT / 'raw'
    REPO = args.repo
    PROJECT = args.project
    QUERY = f'repo:{REPO} is:pr project:{PROJECT}'
    scope = {'repo': REPO, 'project': PROJECT}
    config = ROOT / 'collection-config.json'
    manifest = ROOT / 'manifest.json'
    if config.exists():
        if json.loads(config.read_text()) != scope:
            parser.error('Output directory belongs to a different repository/project; choose a new directory')
    elif manifest.exists():
        if json.loads(manifest.read_text()).get('query') != QUERY:
            parser.error('Existing snapshot query differs; choose a new output directory')
    elif RAW.exists() and any(RAW.iterdir()):
        parser.error('Cannot verify existing raw cache scope; choose a new output directory')
    RAW.mkdir(parents=True, exist_ok=True)
    save(config, scope)


def api(endpoint, params=None, paginate=False):
    cmd = ['gh', 'api', '-X', 'POST' if endpoint == 'graphql' else 'GET', endpoint]
    if paginate:
        cmd += ['--paginate', '--slurp']
    for key, value in (params or {}).items():
        cmd += ['-f', f'{key}={value}']
    for attempt in range(3):
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            obj = json.loads(result.stdout)
            return [item for page in obj for item in page] if paginate else obj
        if attempt < 2:
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError(result.stderr)


def save(path, obj):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)


def cached(name, endpoint, paginate=False):
    path = RAW / name
    if path.exists():
        return json.loads(path.read_text())
    obj = api(endpoint, {'per_page': 100} if paginate else None, paginate)
    save(path, obj)
    return obj


def collect(item):
    n = item['number']
    pr = cached(f'{n}-pr.json', f'repos/{REPO}/pulls/{n}')
    records = []
    for kind, endpoint in (
        ('issue_comment', f'repos/{REPO}/issues/{n}/comments'),
        ('review_comment', f'repos/{REPO}/pulls/{n}/comments'),
        ('review', f'repos/{REPO}/pulls/{n}/reviews'),
    ):
        for c in cached(f'{n}-{kind}.json', endpoint, True):
            user = c.get('user') or {}
            records.append({
                'record_key': f'{kind}:{c["id"]}', 'kind': kind,
                'id': c['id'], 'pr_number': n, 'pr_title': pr['title'],
                'pr_author': pr['user']['login'], 'author': user.get('login'),
                'author_type': user.get('type'), 'is_bot': user.get('type') == 'Bot',
                'author_association': c.get('author_association'),
                'body': c.get('body'), 'url': c.get('html_url'),
                'created_at': c.get('created_at') or c.get('submitted_at'),
                'updated_at': c.get('updated_at'), 'state': c.get('state'),
                'in_reply_to_id': c.get('in_reply_to_id'),
                'review_id': c.get('pull_request_review_id'),
                'path': c.get('path'), 'line': c.get('line'),
                'original_line': c.get('original_line'), 'diff_hunk': c.get('diff_hunk'),
            })
    warnings = []
    actual = sum(r['kind'] == 'issue_comment' for r in records)
    if actual != pr['comments']:
        owner, name = REPO.split('/')
        query = 'query { repository(owner:%s,name:%s) { pullRequest(number:%d) { comments(first:100) { totalCount nodes { databaseId } pageInfo { hasNextPage } } } } }' % (json.dumps(owner), json.dumps(name), n)
        graph = api('graphql', {'query': query})
        save(RAW / f'{n}-comment-count-check.json', graph)
        connection = graph['data']['repository']['pullRequest']['comments']
        assert connection['totalCount'] == actual, (n, 'REST/GraphQL count mismatch')
        if not connection['pageInfo']['hasNextPage']:
            assert {c['databaseId'] for c in connection['nodes']} == {r['id'] for r in records if r['kind'] == 'issue_comment'}
        warnings.append({'pr_number': n, 'kind': 'issue_comment', 'pr_detail_count': pr['comments'],
                         'rest_list_count': actual, 'graphql_count': connection['totalCount'],
                         'note': 'PR detail count differs; REST list agrees with GraphQL. Cause unknown.'})
    assert sum(r['kind'] == 'review_comment' for r in records) == pr['review_comments'], n
    return pr, records, warnings


def jsonl(name, rows):
    (ROOT / name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def main():
    configure()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    items = []
    page = 1
    while True:
        result = api('search/issues', {'q': QUERY, 'per_page': 100, 'page': page, 'sort': 'created', 'order': 'asc'})
        save(RAW / f'search-{page}.json', result)
        assert not result['incomplete_results']
        assert result['total_count'] <= 1000, 'Partition search before collecting more than 1000 results'
        items.extend(result['items'])
        if len(items) >= result['total_count']:
            break
        page += 1
    assert len({p['number'] for p in items}) == result['total_count']
    prs, records, errors, warnings = [], [], [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        pending = {pool.submit(collect, item): item['number'] for item in items}
        for i, future in enumerate(concurrent.futures.as_completed(pending), 1):
            try:
                pr, rows, checks = future.result()
                prs.append(pr)
                records.extend(rows)
                warnings.extend(checks)
            except Exception as exc:
                errors.append({'pr_number': pending[future], 'error': str(exc)})
            if i % 20 == 0 or i == len(items):
                print(f'{i}/{len(items)} PRs processed; errors={len(errors)}', flush=True)
    prs.sort(key=lambda p: p['number'])
    records.sort(key=lambda r: (r['pr_number'], r['created_at'] or '', r['record_key']))
    assert len({r['record_key'] for r in records}) == len(records)
    jsonl('prs.jsonl', prs)
    jsonl('comments-and-reviews.jsonl', records)
    human = [r for r in records if not r['is_bot'] and (r['body'] or '').strip()]
    jsonl('human-comments-and-reviews.jsonl', human)
    sections = [f'# {REPO} · 프로젝트 {PROJECT} 사람이 작성한 댓글·리뷰 원문\n',
                'PR별 생성 시각 순서. 원문을 보존하며 공식 규칙 여부는 판정하지 않는다.\n']
    current_pr = None
    for r in human:
        if r['pr_number'] != current_pr:
            current_pr = r['pr_number']
            sections.append(f'\n## [#{current_pr} {r["pr_title"]}](https://github.com/{REPO}/pull/{current_pr})\n')
        sections.append(f'\n### {r["kind"]} · {r["author"]} · {r["created_at"]}\n')
        sections.append(f'- 원문: {r["url"]}\n- ID: {r["record_key"]}\n')
        if r['path']:
            sections.append(f'- 파일: {r["path"]}, 줄: {r["line"]}, 원래 줄: {r["original_line"]}\n')
        if r['in_reply_to_id']:
            sections.append(f'- 답글 대상: review_comment:{r["in_reply_to_id"]}\n')
        if r['state']:
            sections.append(f'- 리뷰 상태: {r["state"]}\n')
        fence = '`' * max(4, 1 + max((len(m[0]) for m in re.finditer(r'`+', r['body'])), default=0))
        sections.append(f'\n{fence}text\n{r["body"]}\n{fence}\n')
    (ROOT / 'human-comments-by-pr.md').write_text(''.join(sections))
    counts = {}
    for r in records:
        key = r['kind'] + ('_bot' if r['is_bot'] else '_human')
        counts[key] = counts.get(key, 0) + 1
    manifest = {'started_at': started, 'finished_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'query': QUERY, 'project_url': 'https://github.com/orgs/' + PROJECT.replace('/', '/projects/'),
        'project_membership_source': 'GitHub project-qualified issue search',
        'scope': f'All currently searchable PRs in project {PROJECT}, all currently available comments regardless of comment date',
        'expected_pr_count': len(items), 'collected_pr_count': len(prs), 'record_count': len(records),
        'human_nonempty_body_count': len(human), 'counts': counts, 'errors': errors, 'count_warnings': warnings,
        'limitations': ['Deleted comments and edit history are unavailable.', 'Project Week/Status fields and thread resolved state are not collected.', 'This is current project membership, not historical membership.', 'Snapshot is not atomic; each endpoint was fetched separately.']}
    save(ROOT / 'manifest.json', manifest)
    print(json.dumps(manifest, ensure_ascii=False, indent=2), flush=True)
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

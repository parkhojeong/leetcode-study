# 8기 PR 댓글 수집 데이터

온보딩 가이드의 근거를 검토하기 위한 원문 데이터다. 댓글의 조언을 공식 규칙으로 판정하거나 요약하지 않았다.

## 수집 범위

- 저장소: `DaleStudy/leetcode-study`
- 프로젝트: https://github.com/orgs/DaleStudy/projects/29
- 검색식: `repo:DaleStudy/leetcode-study is:pr project:DaleStudy/29`
- 공식 8기 기간: 2026-06-21 ~ 2026-10-03 (저장소 README 기준)
- 프로젝트에 현재 연결되어 검색되는 PR을 수집하며, 제목이나 날짜로 추가 제외하지 않는다.
- 각 PR의 일반 댓글, 코드 줄 댓글과 답글, 리뷰 제출 기록을 모든 페이지에 걸쳐 수집한다.
- 종료 이후의 댓글도 포함한다. 날짜는 API 원문의 UTC를 유지한다.

## 파일

| 파일 | 내용 |
|---|---|
| `manifest.json` | 수집 시각, 범위, 건수, 오류, 제약 |
| `raw/search-*.json` | 프로젝트 조건으로 조회한 PR 목록 원본 |
| `raw/{PR}-pr.json` | PR 상세 API 원본 |
| `raw/{PR}-issue_comment.json` | 일반 댓글 API 원본 |
| `raw/{PR}-review_comment.json` | 코드 줄 댓글과 답글 API 원본 |
| `raw/{PR}-review.json` | 리뷰 제출 API 원본, 빈 본문 포함 |
| `prs.jsonl` | PR 상세 원본 통합, 한 줄에 PR 하나 |
| `comments-and-reviews.jsonl` | 전체 댓글·리뷰 정규화 데이터 |
| `human-comments-and-reviews.jsonl` | Bot 유형 제외, 비어 있지 않은 본문만 추출 |
| `human-comments-by-pr.md` | 사람이 작성한 원문을 PR별로 읽는 뷰 |
| `collect.py` | 읽기 전용 수집 스크립트 |
| `collection-config.json` | 인자 지원 버전 실행 시 생성되는 저장소·프로젝트 설정; 다른 범위의 캐시 혼용 방지 |

## 데이터 해석

- `kind`는 `issue_comment`, `review_comment`, `review`로 구분한다.
- 리뷰 제출 기록과 코드 줄 댓글은 별개다. 빈 본문의 리뷰 제출을 댓글 수에 합산하지 않는다.
- `record_key`는 종류와 ID를 결합한 고유 키다.
- `in_reply_to_id`는 코드 줄 댓글의 부모 댓글 ID다. 일반 댓글의 인용이나 @멘션은 답글 관계로 추정하지 않는다.
- `review_id`로 코드 줄 댓글과 리뷰 제출을 연결할 수 있다.
- `is_bot`은 REST API의 `user.type == Bot` 기준이다. 사람 계정으로 작성된 자동화 여부까지 판정하지 않는다.
- PR 작성자의 답변과 다른 참여자의 피드백을 모두 보존한다.
- 읽기용 뷰에서 원문은 코드 블록으로 표시한다. Markdown 본문 안의 HTML 주석도 그대로 보인다.

## 검증과 제약

검색의 `total_count`, `incomplete_results`, PR 번호 중복을 검증한다. 각 PR 상세의 `comments`, `review_comments` 값과 실제 수집 건수를 대조한다. 일반 댓글 수가 다르면 GraphQL 목록으로 교차 확인하고 `raw/{PR}-comment-count-check.json` 및 `manifest.json`의 `count_warnings`에 근거를 보존한다. REST 댓글 목록과 GraphQL이 일치해도 상세 카운터와의 차이 원인은 단정하지 않는다. 실패한 PR은 `manifest.json`의 `errors`에 남기며 스크립트가 실패 코드로 종료한다.

CLI 토큰에 `read:project` 권한이 없어 프로젝트 상세 GraphQL API 대신 프로젝트 조건 검색을 사용했다. 따라서 Week/Status 필드 및 과거 프로젝트 소속, 검색되지 않는 항목까지의 완전성은 검증하지 못했다. 스레드 해결 상태는 이 데이터에 없다. 삭제된 댓글과 수정 전 본문도 제공되지 않는다. 여러 API를 순차 조회하므로 단일 시점의 원자적 스냅샷은 아니다.

## 재실행

Python 3.9 이상과 GitHub CLI(`gh`)가 필요하다. 먼저 `gh auth login`으로 수집 대상에 읽기 접근 가능한 계정으로 로그인한다. 별도 Python 패키지는 필요하지 않다.

```sh
python3 data/cohort-8-comments-2026-10-29/collect.py \
  --repo DaleStudy/leetcode-study \
  --project DaleStudy/29 \
  --output data/cohort-8-comments-2026-10-29
```

세 인자는 모두 필수다. `--project`는 조직 계정과 프로젝트 번호를 `OWNER/NUMBER` 형식으로 받는다. 다른 저장소·프로젝트에도 사용할 수 있다.

이미 저장된 PR별 원본은 재사용한다. 이는 중단된 수집을 이어가기 위한 동작이며 최신 데이터로 갱신하는 기능은 아니다. 새 스냅샷은 `--output`에 새 폴더를 지정한다. 검색 결과와 통합 파일은 재실행 시 다시 생성된다. 기존 출력 폴더의 저장소·프로젝트가 다르면 실행을 중단한다. `manifest.json`의 시작·종료 시각은 해당 실행 시각이며, 캐시된 원본을 다시 조회한 시각을 뜻하지 않는다.

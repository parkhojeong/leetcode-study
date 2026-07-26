# DaleStudy LeetCode Submission Notes

`CONTRIBUTING.md`의 답안 제출 가이드와 코드 리뷰 가이드를 기준으로 작업한다.

## 파일 작성 규칙

- 답안은 루트의 문제별 폴더에 작성한다. 예: `two-sum/parkhojeong.py`.
- 사용한 언어에 맞추어 파일 확장자를 사용한다. 예: java 이면 `two-sum/parkhojeong.java`
- 파일명은 자신의 GitHub 계정명으로 시작한다. 예: `{github-username}.py`
- 제출하는 모든 파일 끝에는 개행문자를 포함한다.

## 커밋 메시지 규칙

- 커밋 메시지는 `{problem name} solution` 형식이다.
  - 예: `two sum solution`
- 문제별 파일 단위로 커밋한다.

## 주차별 문제 목록

- `problem-weeks.json`을 기준으로 확인한다.
- `problem-weeks.json`에는 주차별 문제 slug, `leetcode` URL, `github-issue` URL을 둔다.
- `problem-categories.json`에는 문제 분류, 난이도, 풀이 의도 메타데이터를 둔다.
- `leetcode` URL은 문제 페이지와 accepted submission 확인에 사용한다.
- `github-issue` URL은 문제 이슈 확인과 PR Description 작성에 사용한다.

## PR 체크리스트

- 한 주차의 답안은 하나의 PR에 모았다.
- PR base는 `DaleStudy/leetcode-study`의 `main`이다.
- PR 제목은 `[Discord 별명] WEEK N Solutions` 형식이다.
  - 예: `[parkhojeong] WEEK 01 Solutions`
- PR Description에 현재 주차에 해당하는 문제 이슈 번호를 체크박스로 적는다.
```md 예) 1주차 
- [ ] #217
- [ ] #219
- [ ] #237
- [ ] #240
- [ ] #264
```
- Projects에서 현재 Week를 설정했다.
- 풀이를 모두 마쳤으면 Projects Status를 `In Review`로 설정했다.

## PR 제출 이후 체크리스트

- 내가 올린 PR의 직전 PR에 나를 reviewer로 추가한다.
- 리뷰 반영 후에는 관련 코멘트에 답변하거나 변경 내용을 남긴다.
- 승인받고 병합할 준비가 되면 PR Description의 검토자/작성자 체크리스트 상태를 현재 상태와 맞춘다.

# 코드 리뷰 가이드
- 반드시 더 나은 풀이를 제시해야 하는 것은 아니다. 이해가 안 되는 부분은 질문으로 남긴다. 
- 피드백은 구체적으로 남긴다. 예: 경계 조건, 시간/공간 복잡도, 변수명, 중복 로직, 설명이 필요한 부분.
- 작성자로서 받은 리뷰에는 존중 있게 답하고, 이해가 안 되면 추가 설명을 요청한다.
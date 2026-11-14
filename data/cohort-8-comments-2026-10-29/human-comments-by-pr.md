# 8기 사람이 작성한 댓글·리뷰 원문
PR별 생성 시각 순서. 원문을 보존하며 공식 규칙 여부는 판정하지 않는다.

## [#2640 [DaleSeo] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2640)

### review_comment · dolphinflow86 · 2026-06-22T09:52:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2640#discussion_r3451265629
- ID: review_comment:3451265629
- 파일: top-k-frequent-elements/DaleSeo.rs, 줄: 12, 원래 줄: 12

````text
로직은 버킷소트로 선형시간 만족하게 잘 작성해주신 것 같아요 :)

러스트는 제가 처음 접해봐서 코드를 분석해보다가, 문득 궁금한게 생겨서 질문드려봅니다.
C++에서는 동적배열인 vector를 힙에 할당하는데, 러스트는 Vec::new()를 하게되면 마찬가지로 힙에 할당하게 될지, 메모리 해제는 어떤식으로 관리될지 궁금합니다. 

추가로 동적배열의 시간/공간 복잡도는 아마 구현체 방식이 언어마다 비슷하리라 생각되어서 동일하다고 생각되는데 러스트도 마찬가지이겠죠?
````

### review_comment · DaleSeo · 2026-06-22T23:59:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2640#discussion_r3456171150
- ID: review_comment:3456171150
- 파일: top-k-frequent-elements/DaleSeo.rs, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3451265629

````text
@dolphinflow86 님, 좋은 질문 감사합니다.

Rust의 `Vec<T>`도 C++의 `vector`처럼 동적 배열이고, 원소를 저장하는 버퍼는 힙에 할당됩니다. 다만 `Vec::new()` 자체는 보통 아직 버퍼를 할당하지 않고, 길이/용량이 0인 `Vec` 값을 만드는 것으로 이해하시면 됩니다. 실제 힙 할당은 `push` 등으로 원소가 들어가면서 용량이 필요해질 때 발생합니다.

메모리 해제는 Rust의 ownership/RAII 방식으로 관리됩니다. `buckets`나 `freqs`가 스코프를 벗어나면 `Drop`이 자동으로 호출되고, 내부 원소들을 정리한 뒤 힙 메모리도 해제됩니다.

시간/공간 복잡도도 일반적인 동적 배열과 거의 동일하게 봐도 될 것 같습니다.
````

### review_comment · dolphinflow86 · 2026-06-23T12:00:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2640#discussion_r3459528602
- ID: review_comment:3459528602
- 파일: top-k-frequent-elements/DaleSeo.rs, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3451265629

````text
@DaleSeo 자세한 답변 감사합니다 👍 
````

### review · dolphinflow86 · 2026-06-23T12:01:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2640#pullrequestreview-4552987343
- ID: review:4552987343
- 리뷰 상태: APPROVED

````text
LGTM!
````

## [#2641 [dolphinflow86] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2641)

### review_comment · dolphinflow86 · 2026-06-22T10:00:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2641#discussion_r3451320462
- ID: review_comment:3451320462
- 파일: contains-duplicate/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
@DaleStudy/coach 풀이 3에서 파이썬의 정렬 알고리즘인 팀소트는 내부적으로 최악의 경우 O(n)의 공간복잡도를 가지는 것으로 알고 있는데 혹시 그 부분이 평가에 고려되었을까요?
````

### review_comment · dolphinflow86 · 2026-06-22T10:02:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2641#discussion_r3451334241
- ID: review_comment:3451334241
- 파일: contains-duplicate/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3451320462

````text
@DaleStudy/coach 아! 풀이3에 검토해주신 공간복잡도 분석이 실패로 표기되어 있어서 질문드렸습니다.
````

### review · jahyun-dev · 2026-06-27T03:10:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2641#pullrequestreview-4583867901
- ID: review:4583867901
- 리뷰 상태: APPROVED

````text
리뷰가 늦어서 죄송합니다! 금주 계획된 일정이 있던걸 깜빡했습니다 ㅠ_ㅠ 상세하게 다양한 케이스까지 구현해주셔서 읽어보면서 너무 많이 배웠습니다. 
````

### issue_comment · dolphinflow86 · 2026-06-27T03:13:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2641#issuecomment-4814972924
- ID: issue_comment:4814972924

````text
> 리뷰가 늦어서 죄송합니다! 금주 계획된 일정이 있던걸 깜빡했습니다 ㅠ_ㅠ 상세하게 다양한 케이스까지 구현해주셔서 읽어보면서 너무 많이 배웠습니다.

아 그러셨군요!
리뷰 감사합니다~ 🙏 
````

## [#2643 [jahyun-dev] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2643)

### review_comment · dolphinflow86 · 2026-06-26T14:04:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2643#discussion_r3481887600
- ID: review_comment:3481887600
- 파일: contains-duplicate/jahyun-dev.rs, 줄: 13, 원래 줄: 13

````text
@jahyun-dev 안녕하세요. 바로 아래 PR에 살고있는 스터디원입니다 :)

러스트로 풀어주셨네요! 요즘 러스트가 대세인가봐요? 많이들 보여서 신기합니다~
이번 풀이는 정렬 후 비교 방식으로 풀어주셨는데, 여기서 시간복잡도를 좀 더 줄일 수 있는 풀이도 있어서 궁금하시면 한번 보셔도 좋을 것 같아요! 

추가로, 원래 자신의 밑에 있는 사람의 PR을 리뷰해주는게 룰로 알고 있어서 제 PR에 일단은 임의로 리뷰어로 지정해드렸는데 한번 놀려오셔서 보시고 코멘트 남겨주시거나, 없으시면 승인 해주시면 감사하겠습니다. 🙏 
````

### review_comment · dolphinflow86 · 2026-06-26T14:07:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2643#discussion_r3481906364
- ID: review_comment:3481906364
- 파일: top-k-frequent-elements/jahyun-dev.rs, 줄: 4, 원래 줄: 4

````text
@jahyun-dev 정렬로 간단하게 풀어주셨네요! 요 문제는 O(nlogn)보다 더 빠르게 푸는 follow up도 있어서 해당 방법도 한번 보고 넘어가시면 도움이 되실 것 같아서 남겨봅니다.
````

### review_comment · dolphinflow86 · 2026-06-26T14:10:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2643#discussion_r3481922842
- ID: review_comment:3481922842
- 파일: two-sum/jahyun-dev.rs, 줄: 12, 원래 줄: 12

````text
@jahyun-dev v와 r이 어떤 의미인지 변수명에서 드러나면 좀 더 좋지 않을까 합니다.
````

### review_comment · daehyun99 · 2026-06-27T08:49:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2643#discussion_r3485705106
- ID: review_comment:3485705106
- 파일: contains-duplicate/jahyun-dev.rs, 줄: 1, 원래 줄: 1

````text
안녕하세요!
이번 PR 리뷰를 맡은 스터디원입니다!

저는 Rust를 처음봐서, GPT를 활용해서 Python으로 번역된 코드를 기준으로 리뷰하겠습니다!

sorting 알고리즘은 시간 복잡도가 O(N log N)으로 알고 있습니다.
아래 분의 코멘트처럼 set 자료형의 조회 시간 복잡도는 O(N)이라, set을 활용한다면 시간 복잡도를 더 줄일 수 있을 것 같습니다!
````

### review_comment · daehyun99 · 2026-06-27T08:50:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2643#discussion_r3485706826
- ID: review_comment:3485706826
- 파일: longest-consecutive-sequence/jahyun-dev.rs, 줄: 1, 원래 줄: 1

````text
특정 수보다 1 작은 값이 없는 것으로 연속된 값 중에 최솟값을 찾으신 후, 연속된 길이를 측정하셨군요!
코드가 직관적이라 이해하기 좋았습니다!
````

### issue_comment · DaleSeo · 2026-06-27T14:10:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2643#issuecomment-4818300826
- ID: issue_comment:4818300826

````text
@DaleStudy 승인
````

## [#2644 [daehyun99] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2644)

### review_comment · dolphinflow86 · 2026-06-26T14:23:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3481995608
- ID: review_comment:3481995608
- 파일: house-robber/daehyun99.py, 줄: 20, 원래 줄: 20

````text
@daehyun99 제가 리뷰 담당한 PR은 아니지만, 지나가다가 코멘트 한번 남겨봅니다 :)
이 풀이는 bottom up dp를 iterative하게 풀어주신 것 같아서 저도 다음번엔 콜스택 메모리 부담이 있는 재귀방식 대신 요 방식으로 풀어보고 싶네요.  잘 보고갑니다 🙏 
````

### review_comment · dolphinflow86 · 2026-06-26T15:05:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3482261956
- ID: review_comment:3482261956
- 파일: longest-consecutive-sequence/daehyun99.py, 줄: 23, 원래 줄: 23

````text
@daehyun99 오.. 이 풀이도 생각해보지 못한 방법인데, 오히려 제가 푼 것 보다 더 좋은 것 같습니다. val을 왼쪽과 오른쪽으로 각 방향으로 진행시키면서 구하는 방식이라 중복 체크 될 여지도 없어서 깔끔해 보이네요. 이 방식은 어떻게 떠올리셨는지 궁금합니다.
````

### review · JAEKWANG97 · 2026-06-27T01:19:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#pullrequestreview-4583567322
- ID: review:4583567322
- 리뷰 상태: APPROVED

````text
안녕하세요! 이번 주 코드 리뷰를 맡은 유재광입니다 ㅎㅎ

전체적으로 풀이가 직관적이라 따라가기 좋았습니다. 보면서 궁금했던 부분과 시간복잡도 측면에서 생각해볼 만한 부분에 코멘트 남겼습니다.

수고하셨습니다!
````

### review_comment · JAEKWANG97 · 2026-06-27T01:22:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3484855424
- ID: review_comment:3484855424
- 파일: two-sum/daehyun99.py, 줄: 9, 원래 줄: 9

````text
이 풀이 흐름 자체는 이해하기 쉬웠습니다!

여기서 `nums.index(val)`은 리스트를 한 번 더 탐색하다 보니, 주석처럼 완전한 O(n)으로 보기는 조금 어려울 수도 있을 것 같아요. 값이랑 인덱스를 같이 `dict`에 저장하면 이 부분도 상수 시간에 처리할 수 있을 것 같습니다.

예를 들면 이런 식으로도 풀 수 있을 것 같아요.

```python
seen = {}

for i, num in enumerate(nums):
    target_num = target - num

    if target_num in seen:
        return [seen[target_num], i]

    seen[num] = i
```
````

### review_comment · JAEKWANG97 · 2026-06-27T01:22:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3484855763
- ID: review_comment:3484855763
- 파일: top-k-frequent-elements/daehyun99.py, 줄: 13, 원래 줄: 13

````text
빈도수를 먼저 세고, 큰 값부터 하나씩 뽑는 방식이라 흐름이 직관적으로 잘 읽혔습니다.

현재는 `k`번 반복하면서 매번 전체 딕셔너리를 다시 훑고 있어서, `k`가 커질수록 비용이 커질 것 같아요. `heapq`로 크기 `k`짜리 heap만 유지하면 반복 탐색을 줄일 수 있을 것 같습니다.
````

### review_comment · daehyun99 · 2026-06-27T08:26:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3485670574
- ID: review_comment:3485670574
- 파일: longest-consecutive-sequence/daehyun99.py, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3482261956

````text
@dolphinflow86  안녕하세요! 리뷰해주셔서 감사합니다ㅎㅎ
이전에 비슷한 문제를 Neetcode에서 푼 다음에, 해설 영상을 봤었는데 해설에서 이런 방식으로 풀더라고요.
그거 보고 벽을 느껴서... 이 풀이 방법이 자연스럽게 떠올랐습니다!
````

### review_comment · daehyun99 · 2026-06-27T08:30:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3485675581
- ID: review_comment:3485675581
- 파일: two-sum/daehyun99.py, 줄: 9, 원래 줄: 9
- 답글 대상: review_comment:3484855424

````text
@JAEKWANG97 안녕하세요! 리뷰해주셔서 감사해요!
`dict`으로 처리하는 방법은 생각 못했었는데, 좋은 것 같군요ㅎㅎ
````

### review_comment · daehyun99 · 2026-06-27T08:38:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2644#discussion_r3485687117
- ID: review_comment:3485687117
- 파일: top-k-frequent-elements/daehyun99.py, 줄: 13, 원래 줄: 13
- 답글 대상: review_comment:3484855763

````text
오호.. `heapq`는 생각 못했었는데 좋은 것 같습니다. 감사합니다ㅎㅎ
````

## [#2645 [jaekwang97] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2645)

### review_comment · JeonJe · 2026-06-25T13:53:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2645#discussion_r3474925883
- ID: review_comment:3474925883
- 파일: top-k-frequent-elements/jaekwang97.java, 줄: 4, 원래 줄: 4

````text
안녕하세요! 1주차 코드 리뷰 진행하게 된 이전제입니다.

혹시 여러 조건의 정렬을 객체를 생성하는 것을 선호하시나요?
저는 Comparator로 짧게 코드를 작성하는 걸 선호하는데, 이번 풀이에 Item 객체를 만드신 이유가 궁금합니다!
````

### review_comment · JAEKWANG97 · 2026-06-26T08:00:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2645#discussion_r3479978322
- ID: review_comment:3479978322
- 파일: top-k-frequent-elements/jaekwang97.java, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3474925883

````text
@JeonJe 님 안녕하세요! 저의 첫 PR 리뷰를 맡아주셔서 매우 감사합니다 ㅎㅎ!

 저는 알고리즘을 풀 때 구현부가 좀 간단하면 좋겠다는 생각을 하면서 코드를 작성합니다. 이 문제에서는 Item을 정렬 기준이 있는 객체로 보았고, 값과 빈도를 하나의 단위로 묶어두면 실제 풀이 흐름에서는 더 읽기 쉽다고 생각했습니다.

 물론 Comparator를 사용하면 더 짧게 작성할 수 있다는 장점도 있는 것 같습니다. 다만 저는 정렬 기준이 구현부에 길게 드러나는 것보다는, 정렬 대상 자체에 의미를 부여하는 방식이 더 편하게 느껴져서 이렇게 해왔습니다 ㅎㅎ 만약 정렬 기준이 상황에 따라 다르다면 Comparator를 활용하는 방식이 더 좋을 것 같습니다.

 좋은 의견 감사합니다! 덕분에 어떤 경우에 객체로 분리하고, 어떤 경우에 Comparator로 간단히 처리할지 다시 생각해보게 됐습니다.
````

### review_comment · JeonJe · 2026-06-26T15:27:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2645#discussion_r3482419330
- ID: review_comment:3482419330
- 파일: top-k-frequent-elements/jaekwang97.java, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3474925883

````text
답변 감사합니다!

구현부를 깔끔하게 유지하려는 의도로 작성하신 것이었군요.
이번 리뷰를 통해 저도 Comparator를 너무 당연하게 사용하고 있었던 건 아닌지 다시 생각해보게 되었습니다.

수고하셨습니다!
````

## [#2646 [JeonJe] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2646)

### issue_comment · JeonJe · 2026-06-27T05:29:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2646#issuecomment-4815395125
- ID: issue_comment:4815395125

````text
@DaleStudy 리뷰
````

### review_comment · essaysir · 2026-06-27T07:34:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2646#discussion_r3485576037
- ID: review_comment:3485576037
- 파일: top-k-frequent-elements/JeonJe.java, 줄: 17, 원래 줄: 17

````text
안녕하십니까. 1주차 코드 리뷰를 맡은 손주선 입니다.
stream으로 정렬하는 방식이 읽기 깔끔해서 좋았습니다.

저는 PriorityQueue로 size-k heap을 유지하는 방식으로 풀었습니다.

```java
PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> count.get(a) - count.get(b));
for (int key : count.keySet()) {
    heap.offer(key);
    if (heap.size() > k) {
        heap.poll();
    }
}
```
전체 정렬이 O(m log m)이라면 size-k heap은 O(m log k)라 k가 작을 때 살짝 이득이 있는 것 같습니다.
(찾아보니 bucket sort로는 시간복잡도가 O(n)까지도 가능하더라구요!)

대신 k가 m에 가까우면 둘이 비슷해지거나 오히려 정렬이 읽기 깔끔해서 나을 수도 있을 것 같은데,
혹시 정렬 방식을 선택하신 특별한 이유가 있으셨을까요?
````

### review_comment · JeonJe · 2026-06-28T03:55:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2646#discussion_r3487319478
- ID: review_comment:3487319478
- 파일: top-k-frequent-elements/JeonJe.java, 줄: 17, 원래 줄: 17
- 답글 대상: review_comment:3485576037

````text
안녕하세요,
이번 문제는 값의 범위가 -10^4 ~ 10^4라 unique 원소가 최대 20,001개라서 실제 정렬 비용이 생각보다 크지 않다고 판단했고, 자료 구조형 없이 스트림만으로 풀이가 가능해보여 이 방식을 선택했습니다.

제약 조건의 범위가 더 크다면 size-k heap(O(m log k))이 더 좋은 선택이라고 생각합니다. 리트코드 Follow up에서도 전체 정렬더 보다 주선님처럼 힙을 사용하는 풀이 방식을 유도 했던 것 같습니다.

> Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

생각지도 못한 부분이었는데, 좋은 리뷰 감사합니다!
````

## [#2648 [essaysir] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2648)

### issue_comment · DaleSeo · 2026-06-26T13:52:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#issuecomment-4810197331
- ID: issue_comment:4810197331

````text
@essaysir https://github.com/DaleStudy/leetcode-study/pull/2648#issuecomment-4768686074
````

### review_comment · njngwn · 2026-06-27T09:42:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#discussion_r3485777020
- ID: review_comment:3485777020
- 파일: longest-consecutive-sequence/essaysir.java, 줄: 8, 원래 줄: 8

````text
Arrays.sort()의 시간복잡도는 O(nlogn) 이라서, 결국 전체 시간 복잡도는 O(nlogn)으로 봐야할 것 같습니다!
````

### review_comment · njngwn · 2026-06-27T09:44:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#discussion_r3485781962
- ID: review_comment:3485781962
- 파일: top-k-frequent-elements/essaysir.java, 줄: 4, 원래 줄: 4

````text
시간 복잡도를 수정해야할 것 같습니다. 
````

### review_comment · njngwn · 2026-06-27T09:45:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#discussion_r3485783994
- ID: review_comment:3485783994
- 파일: top-k-frequent-elements/essaysir.java, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3485781962

````text
저도 풀지는 못했는데, 버킷 정렬을 이용해서 최적화할 수 있는 문제더라구요. 버킷 정렬 방법도 고민해보면 좋을 것 같습니다.
````

### review_comment · njngwn · 2026-06-27T09:46:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#discussion_r3485787149
- ID: review_comment:3485787149
- 파일: two-sum/essaysir.java, 줄: 9, 원래 줄: 9

````text
정답을 찾았을 경우엔, break를 줘서 불필요하게 for 문을 돌지 않게 해도 좋을 것 같습니다
````

### review · njngwn · 2026-06-27T09:46:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#pullrequestreview-4584862118
- ID: review:4584862118
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

### review_comment · essaysir · 2026-06-29T08:48:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2648#discussion_r3490401597
- ID: review_comment:3490401597
- 파일: top-k-frequent-elements/essaysir.java, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3485781962

````text
버킷 정렬 한 번 알아보도록 하겠습니다. 감사합니다
````

## [#2649 [njngwn] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2649)

### review_comment · namuuCY · 2026-06-25T15:36:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2649#discussion_r3475651442
- ID: review_comment:3475651442
- 파일: contains-duplicate/njngwn.py, 줄: 11, 원래 줄: 11

````text
안녕하세요!
공통적으로 같이 푼 문제들부터 순서대로 리뷰를 드리겠습니다!

저는 다른 방식으로 풀었는데, 이 방식으로 정렬 후 인접 숫자끼리 같을 경우를 따져도 되겠다는 생각이 듭니다.
제 방식은 정렬없이 각 숫자를 순회하면서 set에 있는지 확인한 후 없으면 set에 집어넣고 있으면 true를 반환하는 식으로 풀이했습니다.

이러면 시간복잡도 O(n), 공간복잡도 O(n)이 나오는데
njngwn님의 풀이와 이렇게 비교해보니 trade-off가 명확한것 같네요
````

### review_comment · namuuCY · 2026-06-27T13:14:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2649#discussion_r3486063391
- ID: review_comment:3486063391
- 파일: longest-consecutive-sequence/njngwn.py, 줄: 10, 원래 줄: 10

````text
length 보다 좀 더 명확하게 변수명을 설정하는건 어떨까요?
````

### review_comment · namuuCY · 2026-06-27T13:16:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2649#discussion_r3486067298
- ID: review_comment:3486067298
- 파일: top-k-frequent-elements/njngwn.py, 줄: 14, 원래 줄: 14

````text
dict의 value순 정렬하고, k개 뽑을때 파이썬 문법을 사용해서 깔끔하게 잘 마무리하신것 같습니다!
````

### review · namuuCY · 2026-06-27T13:22:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2649#pullrequestreview-4572502221
- ID: review:4572502221
- 리뷰 상태: APPROVED

````text
한주동안 고생하셨습니다!
````

### review_comment · njngwn · 2026-06-27T14:02:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2649#discussion_r3486151833
- ID: review_comment:3486151833
- 파일: contains-duplicate/njngwn.py, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3475651442

````text
시간복잡도를 고려했을 때, set을 이용한 것도 좋은 방법이네요! 감사합니다!
````

## [#2650 [namuuCY] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2650)

### review_comment · yuseok89 · 2026-06-26T00:16:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#discussion_r3478444187
- ID: review_comment:3478444187
- 파일: contains-duplicate/namuuCY.java, 줄: None, 원래 줄: 1

````text
```suggestion
// TC: O(N)
// SC: O(N)
/**
```
````

### review_comment · yuseok89 · 2026-06-26T00:17:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#discussion_r3478447511
- ID: review_comment:3478447511
- 파일: house-robber/namuuCY.java, 줄: None, 원래 줄: 1

````text
```suggestion
// TC: O(N)
// SC: O(1)
class Solution {
```
````

### review · yuseok89 · 2026-06-26T00:25:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#pullrequestreview-4575915689
- ID: review:4575915689
- 리뷰 상태: COMMENTED

````text
> 💡 풀이에 시간/공간 복잡도를 주석으로 남겨보세요!

여전히 위와 같은 코멘트가 보이는데요.
제 풀이에서 여러가지 해봤을 때,
앞 줄에 이렇게 주석으로 남기면 봇이 인식하는 것 같았습니다 !
````

### review_comment · namuuCY · 2026-06-26T01:59:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#discussion_r3478735242
- ID: review_comment:3478735242
- 파일: contains-duplicate/namuuCY.java, 줄: None, 원래 줄: 1
- 답글 대상: review_comment:3478444187

````text
조언 감사드립니다!
방금 수정했고, 오늘 2문제 추가 풀이 후 commit 올리겠습니다.
````

### review_comment · yuseok89 · 2026-06-27T13:57:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#discussion_r3486144463
- ID: review_comment:3486144463
- 파일: top-k-frequent-elements/namuuCY.java, 줄: 22, 원래 줄: 22

````text
정렬 대신 빈도수를 배열 인덱스로 활용하는 버킷 정렬을 쓰면 시간 복잡도를 O(NlogN)에서 O(N)으로 줄일 수 있습니다.
빈도수의 최댓값은 배열 길이 N 을 넘지 않으므로, List<Integer>[] buckets = new List[nums.length + 1] (혹은, 빈도수의 최대값 만큼)을 선언해 빈도별로 숫자를 담은 뒤, 역순으로 K 개를 꺼내면 정렬 없이 빠르게 처리할 수 있어 제안해 드립니다.
````

### review_comment · yuseok89 · 2026-06-27T13:59:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#discussion_r3486148591
- ID: review_comment:3486148591
- 파일: longest-consecutive-sequence/namuuCY.java, 줄: 13, 원래 줄: 13

````text
HashSet 을 활용하면 정렬 없이 O(N) 시간 복잡도로 풀이할 수 있습니다.
````

### review · yuseok89 · 2026-06-27T14:01:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2650#pullrequestreview-4585386085
- ID: review:4585386085
- 리뷰 상태: APPROVED

````text
1주차 고생 많으셨습니다 !
생각의 흐름을 주석에 남겨 놓는 부분은 매우 좋은 습관인 것 같습니다 👍 
````

## [#2651 [yuseok89] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2651)

### review_comment · dahyeong-yun · 2026-06-24T00:06:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2651#discussion_r3463699357
- ID: review_comment:3463699357
- 파일: two-sum/yuseok89.py, 줄: None, 원래 줄: 5

````text
반복을 한번만 돌면서, target을 만드는 두번째 수에 도달할 때 쌍을 찾을 수도 있을 것 같아요!
````

### review_comment · dahyeong-yun · 2026-06-24T14:01:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2651#discussion_r3467673404
- ID: review_comment:3467673404
- 파일: house-robber/yuseok89.py, 줄: 6, 원래 줄: 4

````text
저는 dp 테이블을 만들었는데, 변수 두 개만 선언해서 공간 복잡도를 최소화 할 수 있네요 👍🏼 
````

### review_comment · dahyeong-yun · 2026-06-24T14:27:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2651#discussion_r3467856206
- ID: review_comment:3467856206
- 파일: top-k-frequent-elements/yuseok89.py, 줄: None, 원래 줄: 15

````text
애초에 자료구조 자체가 정렬을 처리하는 것을 사용해서 빈도 수를 넣는 방법도 있네요 👍🏼 
````

### review · dahyeong-yun · 2026-06-24T14:36:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2651#pullrequestreview-4558009453
- ID: review:4558009453
- 리뷰 상태: APPROVED

````text
가독성을 위한 개행 처리나 최소한의 변수 선언을 지향하시는 것 같아요. 👍🏼👍🏼 파이썬은 잘 모르지만, 굉장히 간결하고 깔끔해 보이네요! 첫 주차 고생하셨습니다!
````

### issue_comment · yuseok89 · 2026-06-25T07:22:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2651#issuecomment-4796844175
- ID: issue_comment:4796844175

````text
@DaleStudy 리뷰
````

### review_comment · yuseok89 · 2026-06-25T15:05:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2651#discussion_r3475436291
- ID: review_comment:3475436291
- 파일: two-sum/yuseok89.py, 줄: None, 원래 줄: 5
- 답글 대상: review_comment:3463699357

````text
리뷰 감사합니다!
대충 생각한 부분이 있었네요.
덕분에 개선한 내용으로 수정했습니다. 🙏 
````

## [#2652 [dahyeong-yun] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2652)

### review_comment · okyungjin · 2026-06-25T10:32:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#discussion_r3473691116
- ID: review_comment:3473691116
- 파일: top-k-frequent-elements/dahyeong-yun.java, 줄: 23, 원래 줄: 23

````text
문제 코멘트에 보면 시간 복잡도 O(nlogn)보다 더 효율적으로 풀어보라는 내용이 있어서, 다른 풀이도 고민해보면 좋을 것 같습니다!
````

### review_comment · okyungjin · 2026-06-25T10:41:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#discussion_r3473744503
- ID: review_comment:3473744503
- 파일: two-sum/dahyeong-yun.java, 줄: 12, 원래 줄: 12

````text
시간 복잡도 O(1)은 hashMap 탐색하는 비용을 적어주신게 맞을까요? for문이 있어서 O(N)이라 질문드립니다.
> 자바의 HashMap은 O(1)에 값을 찾을 수 있으므로 시간 복잡도는 O(1), 공간 복잡도는 최악의 경우에 O(N)이 된다.


````

### review · okyungjin · 2026-06-25T11:01:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#pullrequestreview-4570057489
- ID: review:4570057489
- 리뷰 상태: APPROVED

````text
아래 두개는 저도 푼 다음에 리뷰 남기겠습니다. 설명 자세히 적어주셔서 감사합니다.

https://github.com/DaleStudy/leetcode-study/issues/240
https://github.com/DaleStudy/leetcode-study/issues/264
````

### review_comment · dahyeong-yun · 2026-06-27T09:06:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#discussion_r3485728043
- ID: review_comment:3485728043
- 파일: two-sum/dahyeong-yun.java, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3473744503

````text
그렇네요. 말씀 주신대로 시간복잡도는 루프를 배열 크기 만큼 돌기 때문에 O(n)이 맞습니다.
````

### review_comment · dahyeong-yun · 2026-06-27T09:07:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#discussion_r3485729457
- ID: review_comment:3485729457
- 파일: top-k-frequent-elements/dahyeong-yun.java, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3473691116

````text
버킷 정렬이라는 개념이 있군요. 덕분에 더 알게 됐네요. 감사합니다 :)
````

### review_comment · okyungjin · 2026-06-27T09:31:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#discussion_r3485760801
- ID: review_comment:3485760801
- 파일: house-robber/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
@dahyeong-yun 안녕하세요! 코멘트가 늦었습니다.
dp로 풀어주셨는데 현재 로직에서 조금 변경하면 공간 복잡도 O(1)로 최적화가 가능한 것 같아요👍
````

### review_comment · okyungjin · 2026-06-27T09:37:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2652#discussion_r3485768799
- ID: review_comment:3485768799
- 파일: top-k-frequent-elements/dahyeong-yun.java, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3473691116

````text
오 버킷 정렬이라는 개념도 있군요
힙 자료구조 사용하는 풀이도 있는 것 같습니다. 알려주셔서 감사합니다🍀
````

## [#2653 [okyungjin] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2653)

### issue_comment · DaleSeo · 2026-06-27T14:11:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#issuecomment-4818302458
- ID: issue_comment:4818302458

````text
@DaleStudy 승인
````

### review_comment · parkhojeong · 2026-06-27T15:32:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#discussion_r3486300664
- ID: review_comment:3486300664
- 파일: house-robber/okyungjin.py, 줄: 27, 원래 줄: 27

````text
```suggestion
        prev2 = 0 # 앞앞집 최대 수익
        prev1 = 0 # 앞집 최대 수익
        
        for num in nums:
            # 현재 최대 수익
            curr = max(prev1, prev2 + num)
            
            prev2 = prev1
            prev1 = curr
```

로직이 직관적이어서 좋네요! prev1, prev2에 대한 주석은 선언 시점에만 있어도 잘 전달되는 것 같고 슬라이딩 관련된 로직은 주석이 없어도 충분히 의미가 전달되는 거 같습니다 :)


````

### review_comment · parkhojeong · 2026-06-27T15:39:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#discussion_r3486314497
- ID: review_comment:3486314497
- 파일: top-k-frequent-elements/okyungjin.py, 줄: 1, 원래 줄: 1

````text
다양한 풀이 시도해보신 것 멋지네요! most_common 은 몰랐는데 이런게 있군요! 덕분에 배워갑니다 

제공되는 함수들이 실제로 어떻게 구현되어 있는지 살펴보는 것 좋은 거 같아요. 저도 파이썬의 sorted 구현체를 살펴보려고 합니다 :)
````

### review_comment · parkhojeong · 2026-06-27T15:40:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#discussion_r3486316724
- ID: review_comment:3486316724
- 파일: contains-duplicate/okyungjin.py, 줄: 1, 원래 줄: 1

````text
두 풀이가 함께 있어서 가독성 비교하기 좋았던 거 같습니다!
````

### review · parkhojeong · 2026-06-27T15:42:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#pullrequestreview-4585590839
- ID: review:4585590839
- 리뷰 상태: COMMENTED

````text
다양한 방식으로 풀어보시려고 하신 것이 느껴져서 좋았던 거 같습니다. 수고하셨습니다 :)
````

### review_comment · okyungjin · 2026-06-28T00:16:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#discussion_r3487047494
- ID: review_comment:3487047494
- 파일: top-k-frequent-elements/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3486314497

````text
오 구현체 살펴볼 생각은 못 했는데 저도 확인해보겠습니다🔥
````

### review_comment · okyungjin · 2026-06-28T00:17:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2653#discussion_r3487047691
- ID: review_comment:3487047691
- 파일: house-robber/okyungjin.py, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3486300664

````text
감사합니다🙂
````

## [#2654 [parkhojeong] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2654)

### review_comment · seongmin36 · 2026-06-26T07:39:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2654#discussion_r3479876764
- ID: review_comment:3479876764
- 파일: two-sum/parkhojeong.py, 줄: 18, 원래 줄: 18

````text
python은 기본 지식밖에 모르지만, dictionary를 사용하셔서 잘 해결하신 것 같습니다.
`enumerate()`라는 함수를 찾아보았는데, js의 forEach처럼 사용해서 가시성이 좋아지는 것 같습니다. 좋은 코드 공유 감사합니다
````

### review_comment · seongmin36 · 2026-06-26T07:55:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2654#discussion_r3479955240
- ID: review_comment:3479955240
- 파일: top-k-frequent-elements/parkhojeong.py, 줄: 16, 원래 줄: 16

````text
피드백에서도 그랬듯이 O(n log n)의 시간 복잡도를 가집니다.
저는 O(N)의 시간 복잡도를 위해 '버킷 정렬(bucket sort)' 방식을 사용하였는데요,
빈 배열을 만들고, 빈도수 자체를 배열의 인덱스로 삼아서 정렬없이 O(N)의 시간 복잡도만으로 해결이 가능합니다.

저도 이 방법을 새로 알게 되어서 적용해보시는 것을 추천드립니다!
````

### review · seongmin36 · 2026-06-26T07:55:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2654#pullrequestreview-4577611793
- ID: review:4577611793
- 리뷰 상태: APPROVED

````text
1주차도 정말 수고하셨습니다. 다음 주차도 화이팅입니다!
````

### review_comment · parkhojeong · 2026-06-26T14:16:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2654#discussion_r3481957447
- ID: review_comment:3481957447
- 파일: top-k-frequent-elements/parkhojeong.py, 줄: 16, 원래 줄: 16
- 답글 대상: review_comment:3479955240

````text
리뷰 감사합니다! 덕분에 알려주신 버킷 정렬 방식으로도 풀어보았습니다 :)

이론적으로는 시간복잡도가 O(n) 으로 개선되는데 실제 성능은 어떻게 변화되는지 한 번 살펴보고 공유해드리도록 하겠습니다!

````

### review_comment · parkhojeong · 2026-06-26T14:18:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2654#discussion_r3481971321
- ID: review_comment:3481971321
- 파일: two-sum/parkhojeong.py, 줄: 18, 원래 줄: 18
- 답글 대상: review_comment:3479876764

````text
푸신 거 봤는데 js로 문제를 푸신 거 같군요! python이 말씀하신대로 enumarte나 [::-1], list complehension 같은 문법이 깔끔한 거 같습니다 :)
````

## [#2655 [seongmin36] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2655)

### review_comment · Zero-1016 · 2026-06-26T09:23:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3480412374
- ID: review_comment:3480412374
- 파일: contains-duplicate/seongmin36.js, 줄: None, 원래 줄: 9

````text
다음처럼 조건을 다듬을수 있어보여요.

```suggestion
  return set_nums.size !== nums.length
```
````

### review_comment · Zero-1016 · 2026-06-26T09:26:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3480424364
- ID: review_comment:3480424364
- 파일: house-robber/seongmin36.js, 줄: None, 원래 줄: 18

````text
제약 조건에 nums.length != 0이 있기 때문에 해당 로직은 불필요한 로직으로 보여져요.

<img width="295" height="123" alt="Image" src="https://github.com/user-attachments/assets/adf329a0-50e7-4ace-a550-edc8cb6945fa" />

```suggestion
```
````

### review_comment · Zero-1016 · 2026-06-26T09:27:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3480432114
- ID: review_comment:3480432114
- 파일: house-robber/seongmin36.js, 줄: 32, 원래 줄: 34

````text
전 그냥 `Math.max(...arr)` 로 했는데, 마지막 두 개의 집만 비교해도 되겠군요. 👍 
````

### review_comment · Zero-1016 · 2026-06-26T09:32:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3480457866
- ID: review_comment:3480457866
- 파일: top-k-frequent-elements/seongmin36.js, 줄: None, 원래 줄: 40

````text
```tsx
  for (const [num, count] of Object.entries(frequency)) {
    bucket[count].push(Number(num));
  }
```

Number를 통해 형변환을 하는게 Object.entries로 가져온 key값이 String 형태이기 때문임을 이해했어요. 하지만, push할 때 형변환을 해서 넣어주기 때문에 문제가 없어 보여요.


```suggestion
      return result.slice(0, k);
```
````

### review_comment · Zero-1016 · 2026-06-26T09:33:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3480460979
- ID: review_comment:3480460979
- 파일: top-k-frequent-elements/seongmin36.js, 줄: None, 원래 줄: 41

````text
이거 if문 자체를 제거해도 될 것 같아요.
````

### review · Zero-1016 · 2026-06-26T09:37:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#pullrequestreview-4578307080
- ID: review:4578307080
- 리뷰 상태: APPROVED

````text
작성해주신 코드 전체적으로 잘 봤습니다.

Set을 정말 잘 활용하시는 것 같더라고요. 변수명도 그렇고 전반적으로 깔끔해서 읽기 좋았습니다.

코드에서 고민하셨던 부분이 추가로 작성한 로직으로 이미 해결되었거나, 요구사항 제약상 애초에 발생할 수 없는 케이스였던 부분들이 보이는데, 해당 흔적들은 정리하면서 마무리하셔도 좋을 것 같아요.

1주차 고생 많으셨습니다!
````

### review_comment · seongmin36 · 2026-06-26T11:47:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3481163156
- ID: review_comment:3481163156
- 파일: contains-duplicate/seongmin36.js, 줄: None, 원래 줄: 9
- 답글 대상: review_comment:3480412374

````text
아 그렇죠, 조건 자체가 true/false를 반환하니까 반환을 중복으로 하는 거였네요.. 좀 더 유연하게 해 버릇을 해야겠습니다. 좋은 피드백 감사합니다!!
````

### review_comment · seongmin36 · 2026-06-26T11:47:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3481164635
- ID: review_comment:3481164635
- 파일: house-robber/seongmin36.js, 줄: None, 원래 줄: 18
- 답글 대상: review_comment:3480424364

````text
그러네요 조건을 좀 더 꼼꼼히 읽어보도록 하곘습니다. 감사합니다!
````

### review_comment · seongmin36 · 2026-06-26T11:49:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3481172255
- ID: review_comment:3481172255
- 파일: top-k-frequent-elements/seongmin36.js, 줄: None, 원래 줄: 40
- 답글 대상: review_comment:3480457866

````text
오 네 맞습니다. 놓치고 있었네요 감사합니다!
````

### review_comment · seongmin36 · 2026-06-26T12:08:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2655#discussion_r3481268564
- ID: review_comment:3481268564
- 파일: top-k-frequent-elements/seongmin36.js, 줄: None, 원래 줄: 41
- 답글 대상: review_comment:3480460979

````text
아 맞네요. 중간에 `===k`로 억지로 반환 시키는게 부자연스러운 것 같습니다. 어차피 k만큼 자르니까..! @Zero-1016 님 말씀대로 제거하고 루프가 끝나면 반환하는 방식이 더 자연스러울 것 같습니다. 피드백 감사합니다!!
````

## [#2656 [Zero-1016] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2656)

### review_comment · ICE0208 · 2026-06-25T17:13:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2656#discussion_r3476264578
- ID: review_comment:3476264578
- 파일: house-robber/Zero-1016.ts, 줄: 1, 원래 줄: 1

````text
dp[i]를 `i번째 집을 반드시 털었을 때의 최대값`으로 정의하신 풀이로 이해했습니다. 코드 잘 읽었습니다!
````

### review_comment · ICE0208 · 2026-06-25T17:18:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2656#discussion_r3476293427
- ID: review_comment:3476293427
- 파일: house-robber/Zero-1016.ts, 줄: 26, 원래 줄: 26

````text
이 부분은 전체 배열의 최댓값을 구하지 않고 마지막 두 값만 비교해도 괜찮지 않을까 싶습니다.
최종 최댓값은 결국 `마지막 집을 턴 경우` 또는 `마지막에서 두 번째 집을 턴 경우` 중 하나로 결정되니까요!

혹시 제가 놓친 케이스가 있다면 알려주세요~!
````

### review · ICE0208 · 2026-06-25T17:27:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2656#pullrequestreview-4573274764
- ID: review:4573274764
- 리뷰 상태: APPROVED

````text
코드가 정말 예쁘게 작성되어 있고, 특히 시간 복잡도와 공간 복잡도에 대한 주석뿐만 아니라 로직 내에서도 조금이라도 복잡할 수 있는 부분을 주석으로 잘 설명해 주셔서 쉽게 이해하고 빠르고 편안하게 리뷰할 수 있었습니다. 👍

급하게 하느라 주석을 많이 작성하지 못한 제가 반성하게 되네요. 🤣 저도 2주 차 때는 리뷰어를 위해서 주석을 이쁘게 달아봐야겠습니다.

1주차 문제 풀이 고생하셨습니다. 2주차도 화이팅입니다!
````

### review_comment · Zero-1016 · 2026-06-26T09:38:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2656#discussion_r3480487221
- ID: review_comment:3480487221
- 파일: house-robber/Zero-1016.ts, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:3476293427

````text
아 아니에요~ 이거 제가 이전에 비슷한 알고리즘 문제를 풀었어서, value 값이 음수로 내려가는 경우까지 생각해서 이렇게 했었습니다. 말씀해주신대로 뒤에 2부분만 확인하면 될 것 같아요!
````

### issue_comment · DaleSeo · 2026-06-26T13:51:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2656#issuecomment-4810192620
- ID: issue_comment:4810192620

````text
@Zero-1016 다음부터 Week 설정 누락하지 않도록 주의 부탁드리겠습니다. 이번 PR은 제가 대신 해드렸습니다. 

<img width="1784" height="876" alt="2026-06-26 at 09 51 15" src="https://github.com/user-attachments/assets/1a7f8393-d780-4aac-a14e-a96feca0a2bf" />

````

## [#2657 [ICE0208] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2657)

### issue_comment · ICE0208 · 2026-06-26T15:19:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2657#issuecomment-4810899354
- ID: issue_comment:4810899354

````text
@DaleStudy 리뷰
````

### issue_comment · ICE0208 · 2026-06-26T15:22:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2657#issuecomment-4810925542
- ID: issue_comment:4810925542

````text
@DaleStudy 승인
````

### issue_comment · ICE0208 · 2026-06-26T15:23:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2657#issuecomment-4810935248
- ID: issue_comment:4810935248

````text
토요일에 확인할 시간이 없을 것 같아 부득이하게 셀프 승인 처리하였습니다.
````

## [#2658 [Chanz] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2658)

### review_comment · sonshn · 2026-06-26T13:30:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2658#discussion_r3481695111
- ID: review_comment:3481695111
- 파일: contains-duplicate/Chanz82.py, 줄: 10, 원래 줄: 10

````text
저는 Java로 주로 사용하고, Python은 기초적인 문법만 알고 있기 때문에 참고해서 읽어주시기 바랍니다!

우선, 전체적인 풀이 흐름은 저와 비슷한 것 같습니다! 다만, for문 안에 있는 if 조건문도 `if num in hashmap`처럼 작성하는 것이 더 좋아 보입니다! 그 외에 모든 flow를 처리할 수 있게 return 문을 정리하신 것은 좋아 보여요!
````

### review_comment · Chanz82 · 2026-06-26T22:36:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2658#discussion_r3484442566
- ID: review_comment:3484442566
- 파일: contains-duplicate/Chanz82.py, 줄: 10, 원래 줄: 10
- 답글 대상: review_comment:3481695111

````text
리뷰 감사합니다!!
````

### review_comment · Chanz82 · 2026-06-26T22:41:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2658#discussion_r3484457119
- ID: review_comment:3484457119
- 파일: two-sum/Chanz82.py, 줄: 1, 원래 줄: 1

````text
Bot님. 질문에 자동응답 하나요?
````

## [#2659 [sonshn] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2659)

### review_comment · xeulbn · 2026-06-26T08:00:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2659#discussion_r3479981219
- ID: review_comment:3479981219
- 파일: contains-duplicate/sonshn.java, 줄: 7, 원래 줄: 7

````text
현재 코드에서는 HashSet 고유 기능보다는 Set 인터페이스에서 제공하는 contains, add 메서드만 사용하고 있는 것 같습니다.

그래서 변수 타입을 HashSet<Integer>로 두기보다, 
인터페이스 타입인 Set<Integer>로 선언해도 괜찮을 것 같은데 
혹시 따로 HashSet 구현체로 명시하신 이유가 있을까요?
````

### review_comment · xeulbn · 2026-06-26T08:03:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2659#discussion_r3479994475
- ID: review_comment:3479994475
- 파일: two-sum/sonshn.java, 줄: 2, 원래 줄: 2

````text
이미 자동리뷰에도 달렸지만, 값을 더 빠르게 조회할 수 있는 자료구조를 활용하면 반복 횟수를 줄일 수 있을 것 같습니다!
````

### review_comment · xeulbn · 2026-06-26T08:05:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2659#discussion_r3480008820
- ID: review_comment:3480008820
- 파일: top-k-frequent-elements/sonshn.java, 줄: 19, 원래 줄: 8

````text
지금 풀어주신 풀이도 충분히 직관적이고 이해하기 좋은 것 같습니다.
다만 이 문제의 경우, 결과로 필요한 값은 상위 k개뿐이기 때문에 모든 고유 숫자를 정렬하지 않고 필요한 개수만 유지하는 방식도 고려해볼 수 있을 것 같습니다.

예를 들어 PriorityQueue를 활용하면 상위 k개의 후보만 관리할 수 있어서 고유 숫자의 개수가 많고 k가 상대적으로 작을 때 정렬 비용을 줄이는 데 도움이 될 수 있을 것 같습니다.
````

### review · xeulbn · 2026-06-26T08:07:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2659#pullrequestreview-4577758179
- ID: review:4577758179
- 리뷰 상태: COMMENTED

````text
전체적으로 문제 요구사항을 잘 반영했고, 풀이 흐름도 명확해서 이해하기 좋았습니다.

다만 일부 문제들은 다른 관점에서 한 번 더 고민해보시는 것도 좋을 것 같습니다!!
````

## [#2660 [xeulbn] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2660)

### review_comment · okyungjin · 2026-06-27T13:32:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2660#discussion_r3486098493
- ID: review_comment:3486098493
- 파일: house-robber/xeulbn.java, 줄: 1, 원래 줄: 1

````text
dp로 구현해주셨네요. 코드 조금 수정하면 공간 복잡도를 더 줄일 수 있을 것 같아요!👍
````

### review_comment · okyungjin · 2026-06-27T13:34:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2660#discussion_r3486102127
- ID: review_comment:3486102127
- 파일: longest-consecutive-sequence/xeulbn.java, 줄: 1, 원래 줄: 1

````text
hashSet 사용해서 효율적으로 잘 구현해주셨네요. 코드에 시간/공간 복잡도도 적어주시면 좋을 것 같습니다!
````

### review_comment · okyungjin · 2026-06-27T14:04:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2660#discussion_r3486154754
- ID: review_comment:3486154754
- 파일: top-k-frequent-elements/xeulbn.java, 줄: 1, 원래 줄: 1

````text
우선순위 큐 사용해서 풀이해주셨네요. 파이썬 사용하는데 자바 문법도 확인할 수 있어서 좋았습니다👍
````

### review · okyungjin · 2026-06-27T14:07:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2660#pullrequestreview-4585321052
- ID: review:4585321052
- 리뷰 상태: APPROVED

````text
안녕하세요. PR 승인이 안 되어 있어서 리뷰어로 피드백 남겼습니다.
코드에 시간/공간 복잡도나 풀이 과정도 적어주시면 좋을 것 같습니다. 
많이 배워갑니다👍👍
````

### review_comment · xeulbn · 2026-06-28T08:46:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2660#discussion_r3487608078
- ID: review_comment:3487608078
- 파일: house-robber/xeulbn.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3486098493

````text
넵 감사합니다!
````

## [#2661 [chapse57] Week 1](https://github.com/DaleStudy/leetcode-study/pull/2661)

### review_comment · togo26 · 2026-06-26T10:28:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2661#discussion_r3480756840
- ID: review_comment:3480756840
- 파일: contains-duplicate/chapse57.py, 줄: 11, 원래 줄: 11

````text
단순 중복 찾기는 Set을 활용할 수 있습니다. O(n) 최적화도 생각해보시면 좋을 것 같습니다.
````

### review_comment · togo26 · 2026-06-26T10:33:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2661#discussion_r3480774836
- ID: review_comment:3480774836
- 파일: top-k-frequent-elements/chapse57.py, 줄: 15, 원래 줄: 15

````text
AI가 말한 것처럼 구현은 좋습니다. 다만 정렬 없이 최적화 하는 방법도 생각해보면 좋을 것 같네요. (e.g. 빈도 값을 배열 인덱스로 사용)
````

### review · togo26 · 2026-06-26T10:35:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2661#pullrequestreview-4578715169
- ID: review:4578715169
- 리뷰 상태: APPROVED

````text
간결하게 잘 구현해주셨습니다 수고하셨습니다. LGTM👍
````

## [#2663 [hellojoyworldz] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2663)

### review_comment · seueooo · 2026-06-27T13:24:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2663#discussion_r3486084038
- ID: review_comment:3486084038
- 파일: house-robber/hellojoyworldz.py, 줄: 17, 원래 줄: 17

````text
dp 점화식을 변수로 두니까 공간복잡도가 많이 줄어드네요👍
````

### review_comment · seueooo · 2026-06-27T13:29:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2663#discussion_r3486093477
- ID: review_comment:3486093477
- 파일: two-sum/hellojoyworldz.py, 줄: 16, 원래 줄: 16

````text
for문 중첩으로 시간복잡도가 높은데, 해시맵으로 개선하는 것도 좋을 것 같아요👍
````

## [#2664 [seueooo] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2664)

### issue_comment · DaleSeo · 2026-06-27T14:11:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2664#issuecomment-4818304192
- ID: issue_comment:4818304192

````text
@DaleStudy 승인
````

## [#2665 [Yiseull] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2665)

### issue_comment · DaleSeo · 2026-06-27T14:12:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#issuecomment-4818310995
- ID: issue_comment:4818310995

````text
@Yiseull 린트 오류 조치 부탁드립니다!

<img width="924" height="894" alt="2026-06-27 at 10 12 11" src="https://github.com/user-attachments/assets/47233493-3c84-473a-87e0-7708d4e2285b" />

````

### review_comment · parkhojeong · 2026-06-27T16:02:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#discussion_r3486346223
- ID: review_comment:3486346223
- 파일: contains-duplicate/Yiseull.py, 줄: 3, 원래 줄: 3

````text
오 직관적이어서 좋네요!
````

### review_comment · parkhojeong · 2026-06-27T16:03:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#discussion_r3486347747
- ID: review_comment:3486347747
- 파일: top-k-frequent-elements/Yiseull.py, 줄: 14, 원래 줄: 14

````text
중복되는 주석이 들어간 거 같네요. 지워주셔도 좋을거 같습니다!
````

### review_comment · parkhojeong · 2026-06-27T16:07:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#discussion_r3486352596
- ID: review_comment:3486352596
- 파일: longest-consecutive-sequence/Yiseull.py, 줄: 14, 원래 줄: 14

````text
이해가 아주 잘되는 코드인 거 같습니다 👍 
````

### review_comment · parkhojeong · 2026-06-27T16:15:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#discussion_r3486363406
- ID: review_comment:3486363406
- 파일: top-k-frequent-elements/Yiseull.py, 줄: 21, 원래 줄: 21

````text
```suggestion
            counter[num] = counter.get(num, 0) + 1
```

fallback 값을 사용해볼 수도 있을 거 같네요 :)
````

### review · parkhojeong · 2026-06-27T16:16:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#pullrequestreview-4585646180
- ID: review:4585646180
- 리뷰 상태: APPROVED

````text
가독성이 높아서 쉽게 잘 읽혔던 거 같습니다. 수고하셨습니다! 
````

### review_comment · Yiseull · 2026-06-28T14:12:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#discussion_r3488005600
- ID: review_comment:3488005600
- 파일: top-k-frequent-elements/Yiseull.py, 줄: 14, 원래 줄: 14
- 답글 대상: review_comment:3486347747

````text
해당 문제에는 총 3개의 풀이가 있어서 1,2번 풀이는 주석 처리 해놓았습니다. 다음에는 리뷰어가 보시기 편하도록 주석은 제거해둬야겠네요! 감사합니다!
````

### review_comment · Yiseull · 2026-06-28T14:13:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2665#discussion_r3488007750
- ID: review_comment:3488007750
- 파일: top-k-frequent-elements/Yiseull.py, 줄: 21, 원래 줄: 21
- 답글 대상: review_comment:3486363406

````text
오! fallback 값 사용하니 더 간결하네요! 좋은 방안 제시해주셔서 감사합니다🙇🏻‍♀️ 
앞으로 활용 잘 할 것 같아요 :)
````

## [#2666 [hyunpill3] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2666)

### review_comment · sangbeenmoon · 2026-06-27T09:30:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2666#discussion_r3485759150
- ID: review_comment:3485759150
- 파일: house-robber/hyunpill3.java, 줄: 4, 원래 줄: 4

````text
공간복잡도를 O(1) 로 풀어내신 점이 인상적이네요! 👍 
````

## [#2667 [sangbeenmoon] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2667)

### review_comment · okyungjin · 2026-06-27T10:25:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2667#discussion_r3485840393
- ID: review_comment:3485840393
- 파일: house-robber/sangbeenmoon.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3485753542

````text
@sangbeenmoon 공간 복잡도를 O(1)로 최적화할 수 있는 풀이도 있는 것 같습니다!
````

### review_comment · okyungjin · 2026-06-27T10:26:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2667#discussion_r3485841883
- ID: review_comment:3485841883
- 파일: house-robber/sangbeenmoon.py, 줄: 40, 원래 줄: 40

````text
솔루션이 2개 있는데 마지막 라인만 다르네요. 혹시 max로 값을 추출하신 이유가 있을까요?
````

### review_comment · okyungjin · 2026-06-27T10:40:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2667#discussion_r3485857681
- ID: review_comment:3485857681
- 파일: longest-consecutive-sequence/sangbeenmoon.py, 줄: 1, 원래 줄: 1

````text
깔끔하네요 배워갑니다👍
````

### review_comment · okyungjin · 2026-06-27T10:45:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2667#discussion_r3485866178
- ID: review_comment:3485866178
- 파일: top-k-frequent-elements/sangbeenmoon.py, 줄: 1, 원래 줄: 1

````text
문제에 시간 복잡도 n log n보다 낮게 풀어보라는 코멘트가 있던 것 같아요! 시간 복잡도 최적화 고민해보시면 좋을 것 같습니다.

이미 아실 수도 있지만, 파이썬 collections 모듈에서 Counter를 제공하고 있어서 숫자 갯수 셀때 사용하시면 편리합니다.
https://wikidocs.net/233689
````

### review · okyungjin · 2026-06-27T10:46:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2667#pullrequestreview-4584952105
- ID: review:4584952105
- 리뷰 상태: APPROVED

````text
lgtm!
````

## [#2668 [JinuCheon] Week 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2668)

### review · jthw1005 · 2026-06-27T14:28:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2668#pullrequestreview-4585445965
- ID: review:4585445965
- 리뷰 상태: APPROVED

````text
문제 풀이 구현이 깔끔 명료하네요!
이번 주에는 조금 바쁘셨던거 같습니다ㅠ 다음주부터 다시 화이팅해서 모든 문제를 풀어보아요! 🤗 
````

### review_comment · okyungjin · 2026-06-27T14:30:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2668#discussion_r3486196266
- ID: review_comment:3486196266
- 파일: contains-duplicate/JinuCheon.java, 줄: 10, 원래 줄: 10

````text
LinkedHashSet 사용하면 약간의 성능 저하가 있는 이유를 알 수 있을까요?
링크드로 관리할 필요가 없는 정보라 그런지 궁금합니다!

감사합니다. 다음주도 파이팅입니다🍀
````

### review · okyungjin · 2026-06-27T14:32:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2668#pullrequestreview-4585451163
- ID: review:4585451163
- 리뷰 상태: APPROVED

````text
개선 전후 로직을 적어주셔서 좋았습니다~ 부가적인 설명 적어주신 것도요!
````

## [#2669 [jthw1005] WEEK 01 solutions](https://github.com/DaleStudy/leetcode-study/pull/2669)

### review · j2h30728 · 2026-06-27T14:22:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2669#pullrequestreview-4585434577
- ID: review:4585434577
- 리뷰 상태: APPROVED

````text
와우 문제 풀이들이 정말 깔끔하네요. 
얼리리턴을 잊고 풀었는데 덕분에 복기하고 갑니다!

한 주 동안 고생많으셨습니다~!
````

## [#2670 [j2h30728] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2670)

### review_comment · okyungjin · 2026-06-27T14:19:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#discussion_r3486180814
- ID: review_comment:3486180814
- 파일: house-robber/j2h30728.ts, 줄: 1, 원래 줄: 1

````text
재귀로도 풀이해주셨네요. 재귀는 못 떠올렸는데 잘 봤습니다.
dp는 prev1,2만 저장해서 효율적으로 잘 풀어주신 것 같습니다!
````

### review_comment · okyungjin · 2026-06-27T14:22:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#discussion_r3486183835
- ID: review_comment:3486183835
- 파일: longest-consecutive-sequence/j2h30728.ts, 줄: 1, 원래 줄: 1

````text
정렬하는 버전이랑 set으로 최적화한 버전이랑 두가지로 풀이해주셔서 좋았습니다.
````

### review_comment · okyungjin · 2026-06-27T14:23:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#discussion_r3486185550
- ID: review_comment:3486185550
- 파일: top-k-frequent-elements/j2h30728.ts, 줄: 1, 원래 줄: 1

````text
문제 팔로업으로 n log n 보다 좋은 알고리즘으로 풀어보라고 코멘트가 있어서, 최적화 고민해보면 좋을 것 같습니다~
````

### review · okyungjin · 2026-06-27T14:24:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#pullrequestreview-4585430468
- ID: review:4585430468
- 리뷰 상태: APPROVED

````text
최적화 전 로직이랑 후 로직을 같이 볼 수 있어서 좋았습니다👍
파이팅입니다!!
````

### review_comment · j2h30728 · 2026-06-27T14:29:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#discussion_r3486195044
- ID: review_comment:3486195044
- 파일: top-k-frequent-elements/j2h30728.ts, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3486185550

````text
오! 조언 감사합니다~!
````

### review_comment · alphaorderly · 2026-06-27T16:05:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#discussion_r3486351216
- ID: review_comment:3486351216
- 파일: house-robber/j2h30728.ts, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3486181723

````text
탑다운이랑 바텀업 둘다 깔끔하게 구현하셨네요
````

### issue_comment · alphaorderly · 2026-06-27T16:08:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2670#issuecomment-4819011674
- ID: issue_comment:4819011674

````text
전반적으로 깔끔하게 해결하셨네요! 다음주에도 힘내요~
````

## [#2671 [alphaorderly] WEEK 01 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2671)

### review_comment · okyungjin · 2026-06-27T14:36:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2671#discussion_r3486202360
- ID: review_comment:3486202360
- 파일: house-robber/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
dp로 잘 풀어주셨네요. 로직 조금 수정하면 공간복잡도를 O(1)로 최적화 가능할 것 같습니다!
````

### review_comment · okyungjin · 2026-06-27T14:39:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2671#discussion_r3486206502
- ID: review_comment:3486206502
- 파일: two-sum/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
해시맵 사용해서 효율적으로 구현해주셨네요!
````

### review_comment · okyungjin · 2026-06-27T14:40:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2671#discussion_r3486207852
- ID: review_comment:3486207852
- 파일: top-k-frequent-elements/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
오오 heapify 사용하는 로직 고민하다가 heappush pop으로 구현했었는데
배워갑니다!!👍
````

### review_comment · okyungjin · 2026-06-27T14:41:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2671#discussion_r3486208580
- ID: review_comment:3486208580
- 파일: top-k-frequent-elements/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3486207852

````text
근데 시간 복잡도가 어떻게 해서 n log k가 되는 걸까요? 풀면서 이 부분 이해가 잘 안 되더라구요
````

### review_comment · okyungjin · 2026-06-27T14:44:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2671#discussion_r3486212738
- ID: review_comment:3486212738
- 파일: longest-consecutive-sequence/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
달레 스터디 코멘트처럼 연속된 숫자의 시작점부터 탐색하도록 수정하면 더 효율적일 것 같습니다!
````

### review · okyungjin · 2026-06-27T14:44:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2671#pullrequestreview-4585456474
- ID: review:4585456474
- 리뷰 상태: APPROVED

````text
많이 배워갑니다. 다음주도 파이팅입니다🍀
````

## [#2673 [alphaorderly] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2673)

### review_comment · alphaorderly · 2026-06-28T05:10:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2673#discussion_r3487389576
- ID: review_comment:3487389576
- 파일: validate-binary-search-tree/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
BST가 in-order traversal 시 오름차순으로 정렬된다는 점을 이용해서, 정렬이 깨지는지 검사하는 방식도 괜찮을것 같네요
````

### review_comment · DaleSeo · 2026-06-28T13:34:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2673#discussion_r3487954522
- ID: review_comment:3487954522
- 파일: validate-binary-search-tree/alphaorderly.py, 줄: None, 원래 줄: 24

````text
둘 다 `"inf"`를 써야 하지 않나요?
````

### review_comment · DaleSeo · 2026-06-28T13:36:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2673#discussion_r3487957731
- ID: review_comment:3487957731
- 파일: product-of-array-except-self/alphaorderly.py, 줄: None, 원래 줄: 35

````text
이 문제의 follow-up은 나눗셈을 사용하지 말라고 하니, 제출을 일찍 하셔서 아직 시간이 많으니 도전해보시면 좋을 것 같습니다!
````

### review_comment · alphaorderly · 2026-06-28T13:48:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2673#discussion_r3487972992
- ID: review_comment:3487972992
- 파일: validate-binary-search-tree/alphaorderly.py, 줄: None, 원래 줄: 24
- 답글 대상: review_comment:3487954522

````text
leetcode에 math가 자동으로 import되니까 inf를 써서 된거네요
잘 작동해서 파악을 못했네요

````

### review_comment · alphaorderly · 2026-06-28T13:49:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2673#discussion_r3487974525
- ID: review_comment:3487974525
- 파일: product-of-array-except-self/alphaorderly.py, 줄: None, 원래 줄: 35
- 답글 대상: review_comment:3487957731

````text
오호 그렇네요, 코드를 수정해볼 필요가 있겠어요
````

### review_comment · alphaorderly · 2026-06-28T15:42:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2673#discussion_r3488123880
- ID: review_comment:3488123880
- 파일: product-of-array-except-self/alphaorderly.py, 줄: None, 원래 줄: 35
- 답글 대상: review_comment:3487957731

````text
prefix/suffix multiplication을 constant space로 구현하면 되는군요
너무 급하게 풀었네요 ㅎㅎ
````

## [#2674 [freemjstudio] WEEK 1 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2674)

### review · alphaorderly · 2026-06-28T08:42:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2674#pullrequestreview-4587274152
- ID: review:4587274152
- 리뷰 상태: APPROVED

````text
Top K Frequent element의 경우 maxheap을 쓰는것이 깔끔한 코드에 좀 더 낫지 않을까 싶네요
나머지는 엄청 깔끔하게 잘 해결하신것 같습니다.
````

### issue_comment · DaleSeo · 2026-06-28T11:35:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2674#issuecomment-4825963517
- ID: issue_comment:4825963517

````text
@freemjstudio 님, 린트 오류 조치 후 PR 병합 부탁드리겠습니다.

<img width="894" height="764" alt="2026-06-28 at 07 35 21" src="https://github.com/user-attachments/assets/6950bb17-4a47-42b3-8f0c-225cd56f2514" />

````

## [#2675 [DaleSeo] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2675)

### review_comment · alphaorderly · 2026-06-28T15:49:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2675#discussion_r3488134005
- ID: review_comment:3488134005
- 파일: 3sum/DaleSeo.rs, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3487943169

````text
아 이렇게 왼쪽에 포인터를 두고 오른쪽으로 이동하면서
오른쪽에 위치한 부분배열의 left/right 포인터로 접근하는 방법도 있겠네요
````

### issue_comment · DaleSeo · 2026-07-03T21:16:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2675#issuecomment-4879373133
- ID: issue_comment:4879373133

````text
@njngwn 님, 리뷰 안 해주셔서 셀프 승인합니다용~

@DaleStudy 승인
````

## [#2676 [njngwn] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2676)

### review_comment · dolphinflow86 · 2026-06-29T13:25:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2676#discussion_r3492024939
- ID: review_comment:3492024939
- 파일: valid-anagram/njngwn.py, 줄: 7, 원래 줄: 7

````text
안녕하세요 이번주 리뷰를 맡게되었습니다 :)

Counter라는게 있군요? 엄청 깔끔하네요!
찾아보니 이게 문자열 돌면서 맵을 만들어주는 함수인 것 같네요.

그런데 len로 길이가 다른 경우 리턴하도록 체크를 먼저 해 주면, 불필요하게 맵을 만드는 비용을 줄일 수 있을 것 같아요.

````

## [#2677 [dolphinflow86] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2677)

### review_comment · alphaorderly · 2026-07-01T13:41:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2677#discussion_r3506387615
- ID: review_comment:3506387615
- 파일: 3sum/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
오 이러면 왼쪽 포인터를 하나 두고
오른쪽 부분만 부분문제처럼 Two sum 문제로 푸신거리고 보면 될까요?
이런 방법도 있다니 너무 신기하네요! 고생하셨습니다!
````

### review_comment · dolphinflow86 · 2026-07-02T11:47:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2677#discussion_r3512752978
- ID: review_comment:3512752978
- 파일: 3sum/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3506387615

````text
@alphaorderly 리뷰해주셔서 감사합니다. 네 해당 방식이 맞아요.
하지만 구현해놓고 보니 투포인터 방식이 좀 더 깔끔한 것 같긴 하더라구요 :)
````

### review_comment · JeonJe · 2026-07-02T12:37:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2677#discussion_r3513041744
- ID: review_comment:3513041744
- 파일: valid-anagram/dolphinflow86.py, 줄: 4, 원래 줄: 4

````text
안녕하세요! 이번에 코드리뷰를 맡게 된 이전제입니다. 잘부탁드립니다.

solve 코드 너무 깔끔하게 잘 작성하셨네요!!

시간복잡도를 더 낮춰야한다는 제약조건이 있다면, 정렬이 아닌 어떤 다른 방식으로 문제 풀이 접근하실 지 궁금합니다!

````

### review_comment · JeonJe · 2026-07-02T12:44:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2677#discussion_r3513083854
- ID: review_comment:3513083854
- 파일: climbing-stairs/dolphinflow86.py, 줄: 4, 원래 줄: 4

````text
바텀업 + 메모라이제이션을 사용하셨네요!

각 전진 케이스에 대해서 이미 계산되어있으면 해당 값을 사용하고, 아니라면 계산해서 저장하는 방식으로 이해하였습니다.

저는 탑다운 + 메모라이제이션으로 문제를 접근했는데 이런 방식으로 생각을 해볼 수 있겠네요 ㅎㅎ 
이 문제를 푸실 때 어떤 식으로 접근해야겠다 생각하셨는지 궁금합니다!
````

### review_comment · dolphinflow86 · 2026-07-02T14:35:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2677#discussion_r3513883995
- ID: review_comment:3513883995
- 파일: valid-anagram/dolphinflow86.py, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3513041744

````text
@JeonJe 안녕하세요 전제님 :) 저도 잘 부탁드립니다.

이 문제는 시간복잡도를 더 낮춘다면 아래의 2번째 방법으로 푼 해시맵 사용하는 방법으로 접근하여 풀 것 같습니다.

다만 2번 솔루션에서도 s와 t가 영문 소문자 제한이 있어서 해시맵 대신에 26크기의 고정배열로 변경해서 푸는 것으로 조금 

더 최적화를 할 수 있을 것 같아요.
````

### review_comment · dolphinflow86 · 2026-07-02T15:08:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2677#discussion_r3514117820
- ID: review_comment:3514117820
- 파일: climbing-stairs/dolphinflow86.py, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3513083854

````text
@JeonJe 이 문제는 각 스탭마다 행할 수 있는 행동이 1칸 아니면 2칸의 점프라고 생각했고 피보나치나 house robber 문제에서 풀었던 풀이를 적용해볼 수 있겠다라는 생각이 들어서 재귀로 접근했습니다. 실행 흐름은 1층부터 n층까지 재귀적으로 올라가되, n층에서 베이스케이스에 걸려 내려오면서 memo를 채우는식으로 구현하였고, 저도 헷갈려서 결정트리 그려보면서 다시 리마인드 했네요 :)
````

## [#2678 [JeonJe] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2678)

### review_comment · namuuCY · 2026-07-03T04:12:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2678#discussion_r3517425357
- ID: review_comment:3517425357
- 파일: climbing-stairs/JeonJe.java, 줄: 6, 원래 줄: 6

````text
문제 조건에 맞춰서 46으로 미리 초기화해두신부분 꼼꼼해서 인상깊습니다!
````

### review_comment · namuuCY · 2026-07-03T04:14:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2678#discussion_r3517431117
- ID: review_comment:3517431117
- 파일: climbing-stairs/JeonJe.java, 줄: 28, 원래 줄: 28

````text
DFS로 문제를 푸셨는데, 언제 DFS로 풀고 언제 bottom-up으로 푸시는지 전제님만의 기준이 궁금합니다!
````

### review_comment · namuuCY · 2026-07-03T04:23:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2678#discussion_r3517455157
- ID: review_comment:3517455157
- 파일: validate-binary-search-tree/JeonJe.java, 줄: 7, 원래 줄: 7

````text
Double 최대, 최솟값 상수를 저렇게 썼군요 배워갑니다!
````

### review · namuuCY · 2026-07-03T04:25:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2678#pullrequestreview-4622738567
- ID: review:4622738567
- 리뷰 상태: APPROVED

````text
전제님 코드를 보면서 배워갑니다!
한 주동안 고생하셨습니다. 다음주도 화이팅이에요!
````

### review_comment · JeonJe · 2026-07-04T12:05:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2678#discussion_r3523170688
- ID: review_comment:3523170688
- 파일: climbing-stairs/JeonJe.java, 줄: 28, 원래 줄: 28
- 답글 대상: review_comment:3517431117

````text
DP 유형 문제 풀이가 익숙하지 않아서
이 문제는 바텀업 방식과 탑 다운 방식 모두 풀어보았고, 
덜 익숙한 탑 다운 방식으로 제출했습니다!

이번 문제를 통해 
- 탑 다운 방식이 문제 상황을 분할하면서 직관적으로 문제 상황을 이해하는데 도움이 된다는 것을 느꼈고, 
- 바텀 업 방식은 미리 계산한 값을 꼭 배열로 저장하는 것이 아니고, 두 변수를 사용하여 공간복잡도 최적화도 가능하다는 것을 알게되었습니다!
````

## [#2679 [tigermint] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2679)

### review_comment · alphaorderly · 2026-06-29T01:19:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2679#discussion_r3488873052
- ID: review_comment:3488873052
- 파일: climbing-stairs/tigermint.kt, 줄: 1, 원래 줄: 1

````text
이거 공간복잡도 O(1)에 시간복잡도 O(LogN)까지 줄일수 있어요!
나중에 시도해보시는것도 좋겠네요
배열이 아니라 필요한 정보만 저장하는 방식을 통해 확실하게 공간복잡도 줄이는건 쉽게 하실수 있으실거에요
````

### review · ICE0208 · 2026-07-03T16:09:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2679#pullrequestreview-4627017265
- ID: review:4627017265
- 리뷰 상태: COMMENTED

````text
코드 잘 보았습니다.
로직은 저와 비슷하게 짜신 것 같아서 딱히 남길 코멘트는 없는 것 같아요
(코틀린 문법 처음 봤는데 신기하네요🤣)

다음부터는 어떻게 구현하셨는지 간단하게라도 주석을 남겨주시면 더 좋을 것 같아요.
남은 두 문제도 올라오길 기다리겠습니다~
````

### review_comment · okyungjin · 2026-07-04T14:19:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2679#discussion_r3523328576
- ID: review_comment:3523328576
- 파일: product-of-array-except-self/tigermint.kt, 줄: 22, 원래 줄: 22

````text
코틀린이라 구경왔습니다! 코틀린은 until을 쓰는군요
````

### review_comment · okyungjin · 2026-07-04T14:29:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2679#discussion_r3523340473
- ID: review_comment:3523340473
- 파일: valid-anagram/tigermint.kt, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3490489965

````text
1. 맵을 하나만 선언하는 방법도 있을 것 같습니다! 코틀린은 타입으로 뮤터블/이뮤터블을 선언할 수 있군요!
2. map을 set으로 변환해주고 있는데 반드시 필요한 로직일까요? 그 다음 for문을 통해 검증해도 될 것 같은데 어떤 의도로 작성하셨는지 궁금합니다.
3. 함수 초반에 길이 비교를 통해 얼리리턴 하는 방법을 통해 최적화를 해주면 좋을 것 같습니다!
````

### review · okyungjin · 2026-07-04T14:29:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2679#pullrequestreview-4629740852
- ID: review:4629740852
- 리뷰 상태: APPROVED

````text
현대적인 언어로 작성된 알고리즘 잘 봤습니다! 문법이 신기하네요 ㅎㅎ 다음주도 파이팅입니다~!
````

## [#2680 [ICE0208] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2680)

### review_comment · essaysir · 2026-07-04T02:47:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2680#discussion_r3522444566
- ID: review_comment:3522444566
- 파일: climbing-stairs/ICE0208.java, 줄: 33, 원래 줄: 33

````text
안녕하세요. 이번 주 리뷰를 맡게된 손주선이라고 합니다. 
저는 memoization 방식으로 해결했는데, 
이렇게 푸는 방식이 있었네요. 이러한 생각을 어떠한 흐름으로 가지게  되셨던 것이지 궁금합니다. 
````

### review_comment · ICE0208 · 2026-07-04T05:26:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2680#discussion_r3522629581
- ID: review_comment:3522629581
- 파일: climbing-stairs/ICE0208.java, 줄: 33, 원래 줄: 33
- 답글 대상: review_comment:3522444566

````text
안녕하세요! 우선 코드 리뷰 감사합니다. 🙌

주선님께서 말씀해주신 memoization 방식의 Top-down 풀이와 제가 작성한 Bottom-up 풀이는 같은 점화식을 사용하고, 계산 방향과 구현 방식이 다른 접근이라고 생각했습니다.

저는 개인적으로 Bottom-up 방식을 선호해서 처음에는 배열을 활용한 `tabulation DP` 방식으로 구현했습니다. 이후 주석에 남긴 것처럼 `dp[i]`를 구하기 위해 필요한 값은 결국 `직전 값`과 `전전 값`뿐이라는 점을 보고, 정답을 구하기 위해 반드시 n만큼의 배열 공간이 필요한 것은 아니라고 생각했습니다.

그래서 `dp[i - 1]`, `dp[i - 2]`에 해당하는 값만 변수로 들고 가면서 `공간 복잡도를 줄이는 방식으로 구현`했습니다.

덕분에 제 풀이도 다시 한 번 정리해볼 수 있었습니다. 주말에 시간 내서 코멘트까지 달아주셔서 감사합니다! ☺️

````

## [#2681 [essaysir] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2681)

### review_comment · alphaorderly · 2026-06-29T08:38:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3490345782
- ID: review_comment:3490345782
- 파일: climbing-stairs/essaysir.java, 줄: 1, 원래 줄: 1

````text
제 생각에 dfs 함수에 적절한 cache만 추가해도 시간복잡도가 엄청나게 좋아질것 같네요 ( O(N) )!
````

### review_comment · essaysir · 2026-06-29T08:47:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3490394767
- ID: review_comment:3490394767
- 파일: climbing-stairs/essaysir.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3490345782

````text
한 번 그렇게 수정해보도록 하겠습니다!! 감사합니다!!
````

### review_comment · alphaorderly · 2026-06-30T08:52:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3497424104
- ID: review_comment:3497424104
- 파일: climbing-stairs/essaysir.java, 줄: 1, 원래 줄: 1

````text
오 이제 적절한 시간복잡도네요!
정답이 피보나치 수열인것까지 아신다면 공간복잡도도 훨씬 줄이실수 있으실것 같아요!
고생하셨습니다.
````

### review_comment · alphaorderly · 2026-06-30T08:54:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3497438145
- ID: review_comment:3497438145
- 파일: climbing-stairs/essaysir.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3497424104

````text
이런 DP를 쓰는 문제의 경우 Top-down이 생각해내긴 훨씬 쉽지만 몇몇 문제들은 시간제한이 애매하게 걸려 있어서
재귀 호출할때 오버헤드가 생기는것 때문에 TLE가 될수도 있기 때문에
Bottom-up으로 변환하는것도 연습해보시면 좋을거에요!
````

### review_comment · Yiseull · 2026-07-04T13:18:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3523252586
- ID: review_comment:3523252586
- 파일: climbing-stairs/essaysir.java, 줄: 23, 원래 줄: 23

````text
전 DP로 풀었는데 재귀로도 접근할 수 있겠네요!

단순한거지만 아래처럼 쓰면 단순해질 것 같아요!
```
        if ( n <= 2) return n;
```
````

### review_comment · Yiseull · 2026-07-04T13:22:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3523257873
- ID: review_comment:3523257873
- 파일: valid-anagram/essaysir.java, 줄: 19, 원래 줄: 19

````text
약간의 성능 개선인데 맨 처음 s와 t의 길이가 다른 경우, 조기 종료할 수도 있습니다!

평소 파이썬으로 풀다가 요즘 자바로 푸려고 하고 있는데 풀이 배워갑니다👍
````

### review_comment · Yiseull · 2026-07-04T13:27:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3523265180
- ID: review_comment:3523265180
- 파일: product-of-array-except-self/essaysir.java, 줄: 25, 원래 줄: 25

````text
나중에 기회되시면 나눗셈 없이 푸는 방법도 한 번 고민해보시면 좋을 것 같습니다!
곱하기로만 푸는 방법이 참신하더라구요!
````

### review · Yiseull · 2026-07-04T13:29:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#pullrequestreview-4629664543
- ID: review:4629664543
- 리뷰 상태: COMMENTED

````text
리뷰를 늦게 달아서 죄송합니다🙇🏻‍♀️ 수정 없이 바로 머지하시면 될 것 같습니다!

자바 풀이 보면서 많이 얻어갑니다! 이번 한 주도 고생하셨습니다😊
````

### review_comment · essaysir · 2026-07-05T02:15:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2681#discussion_r3524176087
- ID: review_comment:3524176087
- 파일: product-of-array-except-self/essaysir.java, 줄: 25, 원래 줄: 25
- 답글 대상: review_comment:3523265180

````text
안녕하세요~ 전반적인 코드 리뷰에 대해서 감사합니다.
제가 생각 못했던 부분도 많이 집어주셔서 감사합니다.!! 
이번 주 한 주도 고생하셨습니다!!! 
````

## [#2682 [Yiseull] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2682)

### review_comment · okyungjin · 2026-07-04T12:03:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2682#discussion_r3523168029
- ID: review_comment:3523168029
- 파일: climbing-stairs/Yiseull.py, 줄: 1, 원래 줄: 1

````text
공간 복잡도를 O(1)으로 최적화할 수 있을 것 같습니다!
````

### review_comment · okyungjin · 2026-07-04T12:08:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2682#discussion_r3523173347
- ID: review_comment:3523173347
- 파일: product-of-array-except-self/Yiseull.py, 줄: None, 원래 줄: 11

````text
개인적으로 저는 이렇게 작성하는거를 선호합니다!

```py
for i in reversed(range(n)):
```

````

### review_comment · okyungjin · 2026-07-04T12:09:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2682#discussion_r3523174823
- ID: review_comment:3523174823
- 파일: product-of-array-except-self/Yiseull.py, 줄: 1, 원래 줄: 1

````text
answer[0]을 1로 할당하니까 로직이 잘 읽히네요. 잘 봤습니다.

공간/시간 복잡도를 코드에 적어주시면 좋을 것 같아요!

````

### review_comment · okyungjin · 2026-07-04T12:12:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2682#discussion_r3523177782
- ID: review_comment:3523177782
- 파일: valid-anagram/Yiseull.py, 줄: 1, 원래 줄: 1

````text
파이썬의 언어적인 특성을 잘 활용하신 것 같습니다!

저는 성능에 도움이 될 것 같아서, 아래와 같이 길이가 다를 경우 얼리리턴을 해주었습니다. 참고 부탁드립니다~

```py
if len(s) != len(t):
  return False
```
````

### issue_comment · okyungjin · 2026-07-04T12:14:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2682#issuecomment-4881958316
- ID: issue_comment:4881958316

````text
@Yiseull 먼저 풀어주신 3개 먼저 리뷰 남겼습니다! 
````

### review_comment · Yiseull · 2026-07-04T14:18:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2682#discussion_r3523326908
- ID: review_comment:3523326908
- 파일: climbing-stairs/Yiseull.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523168029

````text
변수 2개로도 충분히 풀 수 있군요! 피드백 감사합니다~!
````

## [#2683 [okyungjin] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2683)

### review_comment · dahyeong-yun · 2026-07-04T06:06:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3522680057
- ID: review_comment:3522680057
- 파일: climbing-stairs/okyungjin.py, 줄: 22, 원래 줄: 22

````text
```suggestion
            prev2, prev1 = prev1, prev2 + prev1
```
파이썬이니까 동시 할당을 활용하는 방법도 있을 것 같아요.
````

### review_comment · dahyeong-yun · 2026-07-04T06:07:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3522681875
- ID: review_comment:3522681875
- 파일: climbing-stairs/okyungjin.py, 줄: 19, 원래 줄: 19

````text
개인적으로는 3번째 계단에서 시작하는 거면, 3이라고 명시하는 걸 더 선호해서요. 이렇게도 쓸 수 있을 것 같아요.
```suggestion
        for _ in range(3, n+1):
```
````

### review_comment · dahyeong-yun · 2026-07-04T06:24:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3522699716
- ID: review_comment:3522699716
- 파일: valid-anagram/okyungjin.py, 줄: 32, 원래 줄: 32

````text
`Counter` 라는 것은 처음 보는데 아주 편리하게 쓸 수 있네요. 어차피 `Counter` 객체를 쓴다면 비교 연산으로 더 간단히 표현이 가능한 것 같아요. 찾아보니 `Counter`가 내부적으로 각 문자의 등장 횟 수를 dict 타입으로 반환하고, dict 타입은 `==` 연산자로 동일 비교가 가능하네요. 
```suggestion
        # s가 "apple" 일 때, Counter({'p': 2, 'a': 1, 'l': 1, 'e': 1})
        return Counter(s) == Counter(t)
```
````

### issue_comment · okyungjin · 2026-07-04T11:49:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#issuecomment-4881867396
- ID: issue_comment:4881867396

````text
### 238. Product of Array Except Self

AI의 도움을 받아 prefix, suffix 이해를 돕는 그림을 그렸습니다.

<img width="600" alt="image" src="https://github.com/user-attachments/assets/4cc2981d-b146-4bc1-bf49-4184b9c92e36" />

````

### review_comment · dahyeong-yun · 2026-07-04T11:56:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3523158186
- ID: review_comment:3523158186
- 파일: product-of-array-except-self/okyungjin.py, 줄: 40, 원래 줄: 38

````text
깔끔한 풀이네요 👍🏼 
````

### review_comment · okyungjin · 2026-07-04T11:56:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3523158686
- ID: review_comment:3523158686
- 파일: valid-anagram/okyungjin.py, 줄: 32, 원래 줄: 32
- 답글 대상: review_comment:3522699716

````text
@dahyeong-yun 오오 이런 방법도 있네요. 파이썬은 == 으로 비교하면 참조가 아니라 값으로 비교하는 특성이 있군요. 감사합니다 ㅎㅎ!!
````

### review_comment · okyungjin · 2026-07-04T11:58:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3523162777
- ID: review_comment:3523162777
- 파일: climbing-stairs/okyungjin.py, 줄: 22, 원래 줄: 22
- 답글 대상: review_comment:3522680057

````text
감사합니다! 개인적으로 curr로 작성해주는게 가독성이 더 좋다고 생각해서 풀어서 작성했습니다.
````

### review_comment · okyungjin · 2026-07-04T11:59:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3523164188
- ID: review_comment:3523164188
- 파일: product-of-array-except-self/okyungjin.py, 줄: 40, 원래 줄: 38
- 답글 대상: review_comment:3523158186

````text
시간이 얼마 안 남아서 남은 것들 후딱 풀겠습니다. 늦은 시간인데도 확인해주셔서 감사해요ㅠㅠ!
````

### review · dahyeong-yun · 2026-07-04T12:22:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#pullrequestreview-4629584178
- ID: review:4629584178
- 리뷰 상태: APPROVED

````text
한번에 올리려고 했는데, comment를 올리면 바로 올라가 버리는군요 ^^; 코드 살펴보면서 파이썬이나 간결함에 대해 배울 수 있어서 좋았습니다. 늦은 시간 까지 고생 많으세요! 오늘 더 확인은 어려울 것 같아 미리 승인 드립니다. 남은 문제도 화이팅이에요!
````

### issue_comment · okyungjin · 2026-07-04T12:25:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#issuecomment-4881987282
- ID: issue_comment:4881987282

````text
> 한번에 올리려고 했는데, comment를 올리면 바로 올라가 버리는군요 ^^; 코드 살펴보면서 파이썬이나 간결함에 대해 배울 수 있어서 좋았습니다. 늦은 시간 까지 고생 많으세요! 오늘 더 확인은 어려울 것 같아 미리 승인 드립니다. 남은 문제도 화이팅이에요!

@dahyeong-yun 파이썬 재치있는 언어 같아요. 다 풀고 자바 코드도 구경하러 가겠습니다! 늦은 시간인데도 검토해주셔서 감사합니다. 다음주도 파이팅하세요!!
````

### review_comment · okyungjin · 2026-07-04T13:25:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2683#discussion_r3523262007
- ID: review_comment:3523262007
- 파일: 3sum/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523260791

````text
결과는 공간 복잡도에 포함시키지 않나보네요
````

## [#2684 [dahyeong-yun] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2684)

### review_comment · parkhojeong · 2026-07-04T05:57:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522663927
- ID: review_comment:3522663927
- 파일: climbing-stairs/dahyeong-yun.java, 줄: 35, 원래 줄: 35

````text
가독성 좋은 코드인 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-04T05:58:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522665306
- ID: review_comment:3522665306
- 파일: valid-anagram/dahyeong-yun.java, 줄: 27, 원래 줄: 27

````text
n log(n) 의 복잡도를 빈도 카운트를 이용해 개선해볼 수도 있을 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-04T05:59:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522666173
- ID: review_comment:3522666173
- 파일: validate-binary-search-tree/dahyeong-yun.java, 줄: None, 원래 줄: 27

````text
잘못된 파일이 업로드 된 거 같습니다! 확인 부탁드려요 :)
````

### review_comment · parkhojeong · 2026-07-04T06:04:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522678312
- ID: review_comment:3522678312
- 파일: product-of-array-except-self/dahyeong-yun.java, 줄: 39, 원래 줄: 39

````text
prefix, suffix의 변수명이 값이 직관적이지는 않아서 값의 의미를 담으면 좋을 거 같습니다!
참고로 answer을 활용하면 prefix 제거하는 것도 가능할 거 같습니다~
````

### review_comment · parkhojeong · 2026-07-04T06:05:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522679423
- ID: review_comment:3522679423
- 파일: 3sum/dahyeong-yun.java, 줄: 34, 원래 줄: 34

````text
nums[i] > 0 인 부분부터는 `양수 + 양수 + 양수` 가 되서 이 조건도 고려해보시면 좋을 거 같습니다!
ex: [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
````

### review_comment · parkhojeong · 2026-07-04T06:09:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522683618
- ID: review_comment:3522683618
- 파일: 3sum/dahyeong-yun.java, 줄: 47, 원래 줄: 47

````text
while(`left+1 < right` ..), while(`right > 0` ..) 에서 right > 0도 left처럼 평가하는 것이 좋을 거 같습니다!
````

### review · parkhojeong · 2026-07-04T06:11:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#pullrequestreview-4628978180
- ID: review:4628978180
- 리뷰 상태: DISMISSED

````text
수고하셨습니다! 몇 가지 커멘트 남겼습니다 :)
validate-binary-search-tree가 잘못 올라와 있어서 request changes 남깁니다!
````

### review_comment · dahyeong-yun · 2026-07-04T08:32:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3522862198
- ID: review_comment:3522862198
- 파일: valid-anagram/dahyeong-yun.java, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3522665306

````text
빈도 카운트를 이용해서 개선한다는 의미신거죠? 말씀주신대로 문자열의 Character 단위로 빈도 카운트 하는 방법도 있겠네요.
````

### review_comment · dahyeong-yun · 2026-07-04T11:59:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3523164292
- ID: review_comment:3523164292
- 파일: 3sum/dahyeong-yun.java, 줄: 34, 원래 줄: 34
- 답글 대상: review_comment:3522679423

````text
```suggestion
        for(int i=0; i < nums.length - 2; i++) {
            if (nums[i] > 0) {
                break; 
            }
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

```
이런 식으로 조기 종료를 할 수 있겠네요
````

### review_comment · dahyeong-yun · 2026-07-04T12:04:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3523168749
- ID: review_comment:3523168749
- 파일: 3sum/dahyeong-yun.java, 줄: 47, 원래 줄: 47
- 답글 대상: review_comment:3522683618

````text
```suggestion
            while(left < right) {
                if(nums[i] + nums[left] + nums[right] == 0) {
                    List<Integer> triple = List.of(nums[i], nums[left], nums[right]);
                    answer.add(triple);
                    while(left < right && nums[left] == nums[left + 1]) left++;
                    while(left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if(nums[i] + nums[left] + nums[right] > 0) right--;
                else left++;
```
좌측 포인터가 우측을 넘어가지 않는 선에서 끝내려는 거니, 해당 조건을 공통으로 넣는 식으로 가독성을 개선할 수 있을 것 같네요.
````

### review · ICE0208 · 2026-07-04T14:41:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#pullrequestreview-4629763563
- ID: review:4629763563
- 리뷰 상태: APPROVED

````text
담당 리뷰어님께서 너무 잘 해주셔서 따로 코멘트는 남기지는 않았습니다.
`validate-binary-search-tree` 파일 정상적으로 수정된 것 확인했습니다!

주석을 상세하게 달아주셔서 어떤 방식으로 접근하고 풀었는지, 풀이 의도까지 쉽게 파악할 수 있었습니다. 주석 설명을 보면서 저도 다시 한 번 복습할 수 있었던 것 같습니다. 👍👍

2주차 문제 풀이 고생하셨습니다!
````

### issue_comment · dahyeong-yun · 2026-07-04T15:00:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#issuecomment-4882599036
- ID: issue_comment:4882599036

````text
@ICE0208 늦은 시간에 확인 감사드립니다! 다음 주도 화이팅이에요~
````

### review_comment · parkhojeong · 2026-07-04T15:04:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3523389899
- ID: review_comment:3523389899
- 파일: valid-anagram/dahyeong-yun.java, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3522665306

````text
네 맞습니다! 정렬 안하고 빈도를 카운트하면 O(n) 으로 개선이 가능할 거 같아요 :)
````

### review_comment · parkhojeong · 2026-07-04T15:05:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#discussion_r3523390974
- ID: review_comment:3523390974
- 파일: 3sum/dahyeong-yun.java, 줄: 34, 원래 줄: 34
- 답글 대상: review_comment:3522679423

````text
네 맞습니다 :) 
````

### review · parkhojeong · 2026-07-04T15:10:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2684#pullrequestreview-4629812141
- ID: review:4629812141
- 리뷰 상태: COMMENTED

````text
확인했습니다. 수고하셨습니다!
````

## [#2685 [JinuCheon] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2685)

### issue_comment · DaleSeo · 2026-07-01T13:29:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#issuecomment-4855450822
- ID: issue_comment:4855450822

````text
@JinuCheon https://github.com/DaleStudy/leetcode-study/pull/2685#issuecomment-4833352839
````

### issue_comment · JinuCheon · 2026-07-01T13:36:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#issuecomment-4855511829
- ID: issue_comment:4855511829

````text
@DaleSeo 
앗! 감사합니다!
````

### review_comment · yuseok89 · 2026-07-04T05:41:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#discussion_r3522645126
- ID: review_comment:3522645126
- 파일: climbing-stairs/JinuCheon.py, 줄: None, 원래 줄: 32

````text
```suggestion
        return self.memo[n]

```
뒤에 개행을 추가하셔야 할거에요
````

### review_comment · yuseok89 · 2026-07-04T05:41:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#discussion_r3522645391
- ID: review_comment:3522645391
- 파일: valid-anagram/JinuCheon.py, 줄: None, 원래 줄: 39

````text
```suggestion
        return sorted(s) == sorted(t)

```
뒤에 개행을 추가하셔야 할거에요
````

### review_comment · yuseok89 · 2026-07-04T05:43:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#discussion_r3522647694
- ID: review_comment:3522647694
- 파일: climbing-stairs/JinuCheon.py, 줄: 31, 원래 줄: 31

````text
이 부분이 핵심인데요.
재귀 호출 없이 이 점화식 구현하시면 될 것 같습니다.
````

### review · yuseok89 · 2026-07-04T05:45:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#pullrequestreview-4628959729
- ID: review:4628959729
- 리뷰 상태: COMMENTED

````text
아직 푸시는 중인 것 같지만, 일단 토요일이 되어서 현재까지 버전에 리뷰 남겨드립니다.
2주차 고생많으셨습니다 !
````

### review_comment · JinuCheon · 2026-07-04T06:31:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#discussion_r3522706599
- ID: review_comment:3522706599
- 파일: climbing-stairs/JinuCheon.py, 줄: 31, 원래 줄: 31
- 답글 대상: review_comment:3522647694

````text
@yuseok89 유석님 감사합니다!
점화식.. 어떤 뜻인지도 정확하게 모르고 있었는데 덕분에 찾아보고 공부할 기회가 되었네요.

따뜻한 리뷰 감사합니다 :)

```python
# yuseok89 님 피드백 반영.
# 점화식(recursive relation): 수열의 항을 그 이전 항들을 이용해서 정의하는 식.
# 함수 호출 오버헤드 제거 & 안정성
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0] * (n+1)

        # set init values
        dp[1] = 1
        dp[2] = 2

        # i 번째 계단 오르는 경우의 수: 1칸 + 2칸 경우의 수의 합
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n];
```
````

### review · yuseok89 · 2026-07-04T13:10:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2685#pullrequestreview-4629638068
- ID: review:4629638068
- 리뷰 상태: APPROVED

````text
마지막날까지 달리시네요 !
````

## [#2686 [yuseok89] WEEK02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2686)

### review · daehyun99 · 2026-07-03T11:47:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2686#pullrequestreview-4625523624
- ID: review:4625523624
- 리뷰 상태: APPROVED

````text
안녕하세요.
이번 주차 리뷰를 맡은 김대현입니다!!

문제를 너무 잘 풀어주셔서... 크게 리뷰할 것은 없는 것 같아요.

개인적으론 `climbing-stairs`를 피보나치로 푸는 것은 생각 못했었는데, 코드도 깔끔하고 좋은 것 같습니다...!

고생하셨습니다!!
````

### issue_comment · yuseok89 · 2026-07-03T12:23:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2686#issuecomment-4876175109
- ID: issue_comment:4876175109

````text
> 안녕하세요. 이번 주차 리뷰를 맡은 김대현입니다!!
> 
> 문제를 너무 잘 풀어주셔서... 크게 리뷰할 것은 없는 것 같아요.
> 
> 개인적으론 `climbing-stairs`를 피보나치로 푸는 것은 생각 못했었는데, 코드도 깔끔하고 좋은 것 같습니다...!
> 
> 고생하셨습니다!!

리뷰 감사합니다 !
2주차 고생하셨습니다
````

## [#2687 [daehyun99] WEEK02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2687)

### review_comment · alphaorderly · 2026-06-30T08:59:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3497464286
- ID: review_comment:3497464286
- 파일: valid-anagram/daehyun99.py, 줄: 1, 원래 줄: 1

````text
collections 의 Counter가 기본적으로 defaultdict(int) 처럼 없는 키값에 대해 0을 보낸다는것을 알고 계실까요?
그걸 쓰시면 훨씬 간단하게 작성하실수 있으실거에요!
````

### review_comment · daehyun99 · 2026-06-30T11:27:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3498340115
- ID: review_comment:3498340115
- 파일: valid-anagram/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3497464286

````text
> Counter는 해시 가능 객체를 세기 위한 dict 서브 클래스입니다.

@alphaorderly 
오호 코테 풀면서 `Counter`을 자세히 알아본 적은 없었는데, `dict`의 한 종류였군요!
많이 유용할 것 같아요. 코멘트 감사합니다!
````

### review_comment · parkhojeong · 2026-07-04T05:49:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3522653355
- ID: review_comment:3522653355
- 파일: 3sum/daehyun99.py, 줄: 25, 원래 줄: 25

````text
while 문 사용해서 스킵하는 로직이 r 은 빼신 이유가 궁금하네요!

````

### review_comment · parkhojeong · 2026-07-04T05:50:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3522654889
- ID: review_comment:3522654889
- 파일: climbing-stairs/daehyun99.py, 줄: 19, 원래 줄: 19

````text
dp를 사용하시면 `arr[i] = arr[i-1] + arr[i-2]` 과 같이 직관적인 코드로 개선해볼 수 있을 거 같습니다!


````

### review_comment · parkhojeong · 2026-07-04T05:51:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3522658209
- ID: review_comment:3522658209
- 파일: product-of-array-except-self/daehyun99.py, 줄: 18, 원래 줄: 18

````text
문제에서 division을 사용하지 않고 풀도록 나와있어서 곱셈만을 이용해서 풀어보시면 좋을 거 같습니다 :)
````

### review_comment · parkhojeong · 2026-07-04T05:54:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3522661050
- ID: review_comment:3522661050
- 파일: validate-binary-search-tree/daehyun99.py, 줄: 20, 원래 줄: 20

````text
가독성이 좋은 코드인 거 같습니다 !
````

### review · parkhojeong · 2026-07-04T05:55:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#pullrequestreview-4628966921
- ID: review:4628966921
- 리뷰 상태: APPROVED

````text
수고하셨습니다~! 몇가지 커멘트 남겼습니다 :)
````

### review_comment · daehyun99 · 2026-07-05T06:31:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3524420796
- ID: review_comment:3524420796
- 파일: 3sum/daehyun99.py, 줄: 25, 원래 줄: 25
- 답글 대상: review_comment:3522653355

````text
안녕하세요! 리뷰해주셔 감사합니다!
단순, 중복 조합이 안생기게 하기 위해서 `l`만 고려했는데, `r`도 추가하면 좋을 것 같네요!
````

### review_comment · daehyun99 · 2026-07-05T06:31:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3524421282
- ID: review_comment:3524421282
- 파일: climbing-stairs/daehyun99.py, 줄: 19, 원래 줄: 19
- 답글 대상: review_comment:3522654889

````text
네, 저도 다른 분이 피보나치 수열로 푸는 것을 봤는데, 엄청 깔끔해지고 좋은 것 같더라고요!
````

### review_comment · daehyun99 · 2026-07-05T06:34:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2687#discussion_r3524423652
- ID: review_comment:3524423652
- 파일: product-of-array-except-self/daehyun99.py, 줄: 18, 원래 줄: 18
- 답글 대상: review_comment:3522658209

````text
앗 제가 문제를 제대로 안 읽었었군요.. 지적 감사합니다!!
````

## [#2688 [jthw1005] WEEK02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2688)

### review_comment · okyungjin · 2026-07-04T13:47:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#discussion_r3523290270
- ID: review_comment:3523290270
- 파일: valid-anagram/jthw1005.js, 줄: 1, 원래 줄: 1

````text
> Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

팔로업에 소문자 알파벳 외 문자열에 대해서도 처리할 수 있는 로직을 고민해보라고 적혀있습니다!
확장된 코드로 작성해보면 좋을 것 같습니다.

---
저도 알파벳 소문자만 한정해서 최적화하는 로직으로 작성해봐야겠네요 👍
````

### review_comment · okyungjin · 2026-07-04T13:51:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#discussion_r3523295307
- ID: review_comment:3523295307
- 파일: valid-anagram/jthw1005.js, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523290270

````text
저는 함수 시작부에 길이 비교를 통해 성능을 조금 최적화해줬습니다.
```js
if (s.length !== t.length) {
   return false;
}
```


<br>
<br>

for가 2번 반복되는데, for문을 하나로 합치는 방법도 있을 것 같습니다!

```js
for (let i = 0; i < s.length; i++) {
    data[s.charCodeAt(i) - a_ascii]++;
    data[t.charCodeAt(i) - a_ascii]--;
}
```

재밌는 풀이 잘 봤습니다 ㅎㅎ!
````

### review_comment · okyungjin · 2026-07-04T13:55:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#discussion_r3523299834
- ID: review_comment:3523299834
- 파일: climbing-stairs/jthw1005.js, 줄: 1, 원래 줄: 1

````text
~재귀라서 n이 조금 더 커지면 호출 스택이 많이 쌓일 것 같습니다. 논 재귀로 작성해보시면 좋을 것 같아요!~

생각해보니 메모이제이션 재귀라서 아주 비효율적이진 않네요. n이 작아서 지금 풀이로도 충분한 것 같아요.
잘 봤습니다 👍
````

### review · okyungjin · 2026-07-04T13:56:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#pullrequestreview-4629696232
- ID: review:4629696232
- 리뷰 상태: APPROVED

````text
고생 많으셨습니다! 다음주도 파이팅입니다!!
````

### review_comment · okyungjin · 2026-07-04T14:16:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#discussion_r3523324788
- ID: review_comment:3523324788
- 파일: 3sum/jthw1005.js, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523320736

````text
저랑 같은 로직으로 작성하셨네요. 잘 봤습니다.
주석으로 공간/시간 복잡도 적어주시면 더 좋을 것 같습니다!
````

### review_comment · jthw1005 · 2026-07-04T14:23:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#discussion_r3523332874
- ID: review_comment:3523332874
- 파일: 3sum/jthw1005.js, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523320736

````text
오 잘 생각 안 하고 풀고 있었는데, 다음부턴 주석에 남겨보겠습니다! 👍
````

### review_comment · jthw1005 · 2026-07-04T14:26:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2688#discussion_r3523336435
- ID: review_comment:3523336435
- 파일: valid-anagram/jthw1005.js, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523290270

````text
소문자 알파벳이 아닌 조건이 추가되니까 더 생각할거리가 생기네요,, 감사합니다!
````

## [#2689 [chapse57] Week 2](https://github.com/DaleStudy/leetcode-study/pull/2689)

### review_comment · seongmin36 · 2026-07-02T01:15:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#discussion_r3509879191
- ID: review_comment:3509879191
- 파일: valid-anagram/chapse57.py, 줄: 1, 원래 줄: 1

````text
s와 t를 서로 정렬해서 비교하는 방식을 선택하셨네요! 코드가 직관적이고 깔끔합니다.
다만 이 방식은 sort를 사용하기 때문에 `O(n log n)`만큼의 시간복잡도가 발생합니다.
저는 주언어가 js기 때문에 Map을 사용해서 해결했고, python에서는 이와 유사한 dictionary를 사용해 `O(n)`으로 최적화해볼 수 있을 것 같습니다.

- 해결 방식 : { 문자(key) : 개수(value) }의 형태의 Dictionary를 사용합니다. s와 t를 순회하면서 각 문자의 등장 횟수를 count에 넣어 갯수만으로 두 Dictionary가 일치한지 판별하는 방법입니다.
````

### review_comment · seongmin36 · 2026-07-02T01:21:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#discussion_r3509896038
- ID: review_comment:3509896038
- 파일: valid-anagram/chapse57.py, 줄: None, 원래 줄: 11

````text
지금 `valid-anagram/chapse57.py` 파일 끝에 개행(줄바꿈)이 3줄 이상이라서 ci레벨에서 오류가 발생하고 있습니다. 불필요한 공백을 줄이고 1줄만 남겨주시면 됩니다. 이 부분을 코드 로직과 함께 수정해주시면 될 것 같습니다.
````

### review · seongmin36 · 2026-07-02T01:24:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#pullrequestreview-4613804282
- ID: review:4613804282
- 리뷰 상태: COMMENTED

````text
2주차도 수고많으셨습니다! 제가 드린 피드백이 도움이 되시길 바랍니다.
````

### review_comment · parkhojeong · 2026-07-04T05:29:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#discussion_r3522632588
- ID: review_comment:3522632588
- 파일: contains-duplicate/chapse57.py, 줄: 10, 원래 줄: 10

````text
bruth force로 시간복잡도가 O(n^2) 이라서 해시 맵/셋 등을 활용해서 개선해보셔도 좋을 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-04T05:38:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#discussion_r3522642755
- ID: review_comment:3522642755
- 파일: top-k-frequent-elements/chapse57.py, 줄: 14, 원래 줄: 14

````text
fallback 값을 사용해보셔도 좋을 거 같습니다!
`count[n] = count.get(n, 1) + 1`
````

### review_comment · parkhojeong · 2026-07-04T05:40:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#discussion_r3522644860
- ID: review_comment:3522644860
- 파일: group-anagrams/chapse57.py, 줄: 1, 원래 줄: 1

````text
이 문제는 5주차 문제인 거 같네요. 주차별 문제는 참고로 여기서 보실 수 있습니다 http://github.com/orgs/DaleStudy/projects/6/
````

### review · parkhojeong · 2026-07-04T05:42:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2689#pullrequestreview-4628947109
- ID: review:4628947109
- 리뷰 상태: APPROVED

````text
수고하셨습니다~! 
지난 주차도 함께 풀어주신 거 같네요! PR 설명에 푸신 문제와 1주차도 포함되었다는 내용을 추가해주시면 좋을 거 같습니다~
````

## [#2690 [seongmin36] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2690)

### review · JAEKWANG97 · 2026-07-04T02:00:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2690#pullrequestreview-4628671079
- ID: review:4628671079
- 리뷰 상태: APPROVED

````text
리뷰했습니다! 전반적으로 풀이들이 문제 조건에 맞게 잘 작성되어 있고, 3Sum 중복 처리나 Product of Array Except Self의 prefix/suffix 누적 방식도 깔끔하게 동작하는 것 확인했습니다.

로컬에서 주요 예제와 몇 가지 경계 케이스도 같이 확인했습니다.
- 3Sum: 중복 원소/0만 있는 케이스
- Climbing Stairs: n=1,2,3,4,5,10
- Product of Array Except Self: 0 포함/0 두 개 포함 케이스
- Valid Anagram: 길이 동일하지만 문자 수가 다른 케이스
- Validate BST: subtree bound 위반, duplicate 케이스

가벼운 코멘트로는 `climbStairs`는 현재 배열을 `n + 1`까지 만들고 `arr[n - 1]`을 반환하고 있는데, 동작에는 문제 없지만 인덱스 기준을 `dp[1] = 1`, `dp[2] = 2`처럼 맞추거나 변수 2개만 쓰는 방식으로 줄이면 더 직관적으로 읽힐 것 같습니다.

고생하셨습니다 👍
````

### review_comment · JAEKWANG97 · 2026-07-04T02:43:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2690#discussion_r3522438565
- ID: review_comment:3522438565
- 파일: validate-binary-search-tree/seongmin36.js, 줄: 31, 원래 줄: 31

````text
`min`, `max` 범위를 함께 넘기면서 검증한 점이 좋았습니다!

단순히 현재 노드와 자식 노드만 비교하지 않고, 서브트리 전체가 가져야 하는 값의 범위를 유지해서 검사하기 때문에 BST의 함정 케이스도 잘 처리할 수 있는 구조로 보입니다.
````

### review_comment · JAEKWANG97 · 2026-07-04T02:43:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2690#discussion_r3522438567
- ID: review_comment:3522438567
- 파일: climbing-stairs/seongmin36.js, 줄: 17, 원래 줄: 17

````text
점화식을 배열로 풀어주셔서 풀이 흐름을 따라가기 좋았습니다!

저는 계단 수와 인덱스를 맞추는 방식이 더 직관적으로 보여서 선호하는 편입니다. 현재는 `arr[0]`이 1칸, `arr[1]`이 2칸을 의미하고 `arr[n - 1]`을 반환하는 구조인데, `dp[1] = 1`, `dp[2] = 2`처럼 맞추면 점화식이 더 자연스럽게 읽힐 것 같아요.

가독성 관점의 가벼운 의견으로 봐주시면 좋겠습니다 🙂
````

### review · JAEKWANG97 · 2026-07-04T02:43:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2690#pullrequestreview-4628731797
- ID: review:4628731797
- 리뷰 상태: APPROVED

````text
전체적으로 잘 봤습니다! 풀이 흐름이 잘 읽혔고, 가독성 관점에서 같이 보면 좋을 부분만 짧게 코멘트 남겼습니다. 고생하셨습니다 🙂
````

### review_comment · seongmin36 · 2026-07-04T13:17:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2690#discussion_r3523250673
- ID: review_comment:3523250673
- 파일: climbing-stairs/seongmin36.js, 줄: 17, 원래 줄: 17
- 답글 대상: review_comment:3522438567

````text
아 그렇네요, 인덱스랑 계단 수와 맞추면 좀 더 가독성이 좋아지겠네요! 피드백 감사합니다!!
````

## [#2691 [jaekwang97] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2691)

### issue_comment · DaleSeo · 2026-07-01T13:29:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2691#issuecomment-4855446573
- ID: issue_comment:4855446573

````text
@JAEKWANG97 https://github.com/DaleStudy/leetcode-study/pull/2691#issuecomment-4848925487
````

### review_comment · namuuCY · 2026-07-02T08:05:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2691#discussion_r3511433061
- ID: review_comment:3511433061
- 파일: climbing-stairs/jaekwang97.java, 줄: 16, 원래 줄: 15

````text
DP 정석적인 풀이대로 잘 하신것 같습니다!
다만 
- 몇 번째 항이 초기항이고, 이후 어느 항부터 점화식이 적용되는지 다시 한번 살펴보시는 것도 좋을것 같습니다.
- 지금 이 풀이에서는 n 이하의 모든 값을 다 저장하고 있는데, 굳이 다 저장할 필요가 있을까요? 저장하지 않는 풀이도 한번 생각해보시는거 어떨까요?
````

### review_comment · namuuCY · 2026-07-02T08:06:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2691#discussion_r3511439012
- ID: review_comment:3511439012
- 파일: product-of-array-except-self/jaekwang97.java, 줄: 26, 원래 줄: 26

````text
저는 처음에 잘못된 풀이(나눗셈을 사용한)로 풀었었는데,
@JAEKWANG97 님 풀이를 보고 제가 틀렸다는걸 알게됐어요.
````

### review · namuuCY · 2026-07-02T08:07:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2691#pullrequestreview-4615593232
- ID: review:4615593232
- 리뷰 상태: APPROVED

````text
우선 지금 풀린 문제들까지의 리뷰를 달아두었습니다!
````

### review_comment · JAEKWANG97 · 2026-07-04T02:48:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2691#discussion_r3522446596
- ID: review_comment:3522446596
- 파일: climbing-stairs/jaekwang97.java, 줄: 16, 원래 줄: 15
- 답글 대상: review_comment:3511433061

````text
리뷰 감사합니다!

말씀해주신 것처럼 직전 두 값만 있으면 다음 값을 계산할 수 있어서, 전체 `dp` 배열을 저장하지 않는 방식으로 수정해봤습니다. 초기항도 `n <= 2`를 먼저 처리하고, 이후에는 `prev`, `cur` 두 변수로 점화식 흐름이 보이도록 정리했습니다.
````

### review_comment · JAEKWANG97 · 2026-07-04T02:48:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2691#discussion_r3522446620
- ID: review_comment:3522446620
- 파일: product-of-array-except-self/jaekwang97.java, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:3511439012

````text
감사합니다!

저도 처음에는 전체 곱을 구해서 나누는 방식을 먼저 떠올렸는데, 문제 조건 때문에 왼쪽 누적 곱과 오른쪽 누적 곱을 따로 계산하는 방식으로 접근했습니다. 이렇게 나누면 0이 포함된 케이스도 자연스럽게 처리돼서 좋았던 것 같습니다.
````

## [#2692 [namuuCY] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2692)

### review_comment · alphaorderly · 2026-07-02T02:03:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2692#discussion_r3510007770
- ID: review_comment:3510007770
- 파일: product-of-array-except-self/namuuCY.java, 줄: 1, 원래 줄: 1

````text
이거 저도 잘 몰랐었는데요, 제대로 풀면 0의 갯수별로 엣지 케이스를 분리할 필요가 없더라고요

그리고 문제에서 보시면 아시다시피 나눗셈 연산자는 사용하지 말라고 되어 있어서요

`You must write an algorithm that runs in O(n) time and without using the division operation.`

그렇게 한번 시도해보시는것도 좋을것 같아요!
````

### review · alphaorderly · 2026-07-02T07:23:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2692#pullrequestreview-4615326581
- ID: review:4615326581
- 리뷰 상태: APPROVED

````text
상당히 잘 해결하신것 같아요!
````

### review_comment · namuuCY · 2026-07-02T08:01:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2692#discussion_r3511408654
- ID: review_comment:3511408654
- 파일: product-of-array-except-self/namuuCY.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3510007770

````text
말씀하신 것처럼, 제가 요구사항을 지키지 않은 풀이라 틀린풀이라고 보는게 맞는거 같습니다!
확인해서 새 풀이를 풀어보고, 추가했습니다. 

또 리트코드 다른 분 풀이를 보니 

static 영역을 추가하고 
미리 작은 단위(길이가 2인 nums 배열)로 웜업을 해서 조금이나마 속도를 올리려고 꼼수를 쓴 게 있더라고요. 
재미있어서 넣어봤습니다.
````

## [#2693 [xeulbn] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2693)

### review_comment · namuuCY · 2026-07-02T08:13:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3511477781
- ID: review_comment:3511477781
- 파일: 3sum/xeulbn.java, 줄: 3, 원래 줄: 3

````text
혹시 이거 왜 공간복잡도가 `O(n log n)`이 되는지 설명해주실 수 있나요?
sort에 쓰이는 추가 공간복잡도가 logn 정도는 될 것 같은데.. 그것외에는 nlogn까지 올라가는 이유가 코드상으로는 와닿지 않아서 여쭤봅니다!
````

### review_comment · namuuCY · 2026-07-02T08:14:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3511482042
- ID: review_comment:3511482042
- 파일: climbing-stairs/xeulbn.java, 줄: 4, 원래 줄: 4

````text
공간 최적화가 잘 되어서 좋은 것 같습니다!
````

### review_comment · namuuCY · 2026-07-02T08:17:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3511497063
- ID: review_comment:3511497063
- 파일: house-robber/xeulbn.java, 줄: 21, 원래 줄: 21

````text
이 문제도 위의 climb stairs 문제와 비슷하게 최적화가 가능할것 같아요!
````

### review_comment · namuuCY · 2026-07-02T08:19:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3511511333
- ID: review_comment:3511511333
- 파일: top-k-frequent-elements/xeulbn.java, 줄: 12, 원래 줄: 12

````text
우선순위큐를 둬서 나중에 순서정렬 안한 것은 좋은 아이디어 같습니다!
이렇게 풀이를 할 때, 시공간 복잡도가 어떻게 될지 주석으로 적어두면 좋을 것 같습니다!
````

### review · namuuCY · 2026-07-02T08:20:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#pullrequestreview-4615648537
- ID: review:4615648537
- 리뷰 상태: COMMENTED

````text
2주차까지 수고하셨습니다!
````

### review_comment · Zero-1016 · 2026-07-02T15:58:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3514446587
- ID: review_comment:3514446587
- 파일: top-k-frequent-elements/xeulbn.java, 줄: 10, 원래 줄: 10

````text
Java에는 우선순위 큐라는 개념이 존재하군요. 새롭게 알아갑니다.
````

### review_comment · Zero-1016 · 2026-07-02T16:06:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3514499318
- ID: review_comment:3514499318
- 파일: 3sum/xeulbn.java, 줄: 8, 원래 줄: 8

````text
TMI) js는 기본이 문자열 정렬이라 이 풀이를 그대로 js로 옮기면 틀려요 java 좋네요

```js
[10, 2, 1].sort();            // → [1, 10, 2]  😱  비교자 없으면 문자열 정렬
[10, 2, 1].sort((a,b)=>a-b);  // → [1, 2, 10]  이렇게 해야 함
```
````

### review · Zero-1016 · 2026-07-02T16:08:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#pullrequestreview-4619193121
- ID: review:4619193121
- 리뷰 상태: APPROVED

````text
고생하셨습니다 :) java 코드로 풀이하신거보니 재밌네요.

DaleStudy 레포지토리가 기본적으로 Squash Merge를 지원하고 있어서 지난주에 풀이하신 문제 5개가 변경사항으로 들어왔어요.
````

### review_comment · parkhojeong · 2026-07-04T14:14:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3523322292
- ID: review_comment:3523322292
- 파일: 3sum/xeulbn.java, 줄: 32, 원래 줄: 32

````text
List.of를 사용하면 tmpList 를 사용 안해도 될거 같고, 정답추가와 left++, right-- 주석은 코드로 충분히 설명이 되어서 없어도 괜찮을 거 같습니다! :)

```suggestion
                if(sum==0){
                    answer.add(List.of(nums[i], nums[leftIndex], nums[rightIndex]));
                    leftIndex+=1;
                    rightIndex-=1;
```
````

### review_comment · parkhojeong · 2026-07-04T14:15:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3523323502
- ID: review_comment:3523323502
- 파일: climbing-stairs/xeulbn.java, 줄: 12, 원래 줄: 12

````text
대체로 할당/산술 연산자 좌우로 스페이스를 한 칸 쓰시는 게 많은게 일관되게 맞춰주시면 좋을 거 같습니다! 문제마다 조금씩 다르네요 :)
```suggestion
        int[] dp = new int[n+1];
```
````

### review_comment · parkhojeong · 2026-07-04T14:18:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3523326818
- ID: review_comment:3523326818
- 파일: two-sum/xeulbn.java, 줄: 8, 원래 줄: 8

````text
변수 명을 공들여서 쓰시는 느낌이 드는 거 같습니다! 좋네요 :)
````

### review_comment · parkhojeong · 2026-07-04T14:21:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3523330549
- ID: review_comment:3523330549
- 파일: valid-anagram/xeulbn.java, 줄: 30, 원래 줄: 30

````text
`characterMap.get(c)<0`은 조건식을 합쳐도 좋을 거 같습니다 :)
```suggestion
            if(!characterMap.containsKey(c) || characterMap.get(c)<=0){
                return false;
            }

            characterMap.put(c, characterMap.get(c) - 1);
        }
```
````

### review_comment · parkhojeong · 2026-07-04T14:22:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#discussion_r3523331398
- ID: review_comment:3523331398
- 파일: validate-binary-search-tree/xeulbn.java, 줄: 39, 원래 줄: 39

````text
코드가 매우 깔끔해서 좋은 거 같습니다 :)
````

### review · parkhojeong · 2026-07-04T14:24:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2693#pullrequestreview-4629720533
- ID: review:4629720533
- 리뷰 상태: COMMENTED

````text
다른 분들이 리뷰 꼼꼼하게 해주셨네요! 몇가지 커멘트 남겼습니다~ 수고하셨습니다! 
````

## [#2694 [Zero-1016] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2694)

### review_comment · Chanz82 · 2026-07-03T01:39:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2694#discussion_r3516958269
- ID: review_comment:3516958269
- 파일: valid-anagram/Zero-1016.ts, 줄: None, 원래 줄: 22

````text
혹시 has() 체크가 없어도 동작하지 않을까요? key가 없을 때 get()은 undefined를 반환하고, value는 number이므로 value !== undefined가 true가 되어 return false가 반환될 것 같습니다. 조건을 하나 줄이면 더 간결해질 것 같아서 의견드려봅니다.
````

### review_comment · Chanz82 · 2026-07-03T02:00:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2694#discussion_r3517026840
- ID: review_comment:3517026840
- 파일: climbing-stairs/Zero-1016.ts, 줄: 11, 원래 줄: 11

````text
dp[i]가 0부터 시작하다보니, 마치 0개 계단의 경우 1칸 이동을 나타내는 것처럼 느껴집니다. 
저도 인덱스를 0부터 자주 사용하는데요. 이 경우, 인덱스를 1부터 사용하면 dp[i] = i칸 계단의 답으로 읽혀 더 직관적이고, base case 설정에 따라 early return도 자연스럽게 제거할 수 있을 것 같다는 의견을 드려봅니다..!
````

### review_comment · Zero-1016 · 2026-07-03T02:06:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2694#discussion_r3517042621
- ID: review_comment:3517042621
- 파일: 3sum/Zero-1016.ts, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3517029747

````text
제가 작성한 복잡도랑 다르게 표기가 되어있네요 :(
````

### review_comment · Zero-1016 · 2026-07-03T02:10:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2694#discussion_r3517055208
- ID: review_comment:3517055208
- 파일: climbing-stairs/Zero-1016.ts, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3517026840

````text
의견 감사합니다! 사실 저도 dp[1] 부터 사용하는걸 생각하긴 했는데요. dp[0]을 비워두면 실제로 쓰이지 않는 값이 배열에 남는 게 어색해서, 슬롯을 전부 의미 있게 채우는 쪽(dp[i] = i+1칸의 답)으로 작성했어요. 공간 차이는 미미하지만, "배열의 모든 원소가 유효한 답"이라는 일관성을 유지하고 싶었습니다.
````

### review_comment · Zero-1016 · 2026-07-03T02:10:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2694#discussion_r3517055996
- ID: review_comment:3517055996
- 파일: valid-anagram/Zero-1016.ts, 줄: None, 원래 줄: 22
- 답글 대상: review_comment:3516958269

````text
해당 부분 간결하게 수정이 가능했네요 확인 감사합니다 :) [refactor: has 검사 제거 리뷰 반영](https://github.com/DaleStudy/leetcode-study/pull/2694/commits/aea363abd55bb25007fa0d3a368e869f1b5bb9b5)
````

### review · alphaorderly · 2026-07-04T13:29:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2694#pullrequestreview-4629665189
- ID: review:4629665189
- 리뷰 상태: APPROVED

````text
전반적으로 깔끔하게 잘 해결하셨네요!

````

## [#2695 [Chanz] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2695)

### review_comment · alphaorderly · 2026-07-03T07:42:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2695#discussion_r3518260537
- ID: review_comment:3518260537
- 파일: climbing-stairs/Chanz82.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3516915027

````text
공간복잡도 맞긴 하신데, 재귀를 하면 메모리 스택에 Function call이 계속 쌓이기 때문에 배열을 쓰는것보단 좋진 않을거에요!

쉬운것부터 바텀업으로 구현하시는것도 저는 DP를 공부하기 좋은 선택이라고 생각합니다.
````

### review_comment · alphaorderly · 2026-07-03T07:43:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2695#discussion_r3518269725
- ID: review_comment:3518269725
- 파일: product-of-array-except-self/Chanz82.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3516915183

````text
Follow up 에 공간복잡도 O(1)로 해결해 보라는게 있어서요 ( 출력 배열 1개 제외 )

한번 시도해 보시는것도 좋을것 같아요!

힌트는 left, right 이 두개는 사실 배열이 아니여도 됩니다!
````

### review_comment · Chanz82 · 2026-07-03T15:36:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2695#discussion_r3520816693
- ID: review_comment:3520816693
- 파일: climbing-stairs/Chanz82.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3516915027

````text
아아 그러네요 스택 메모리도 감안을 해야 하는군요.. n이 커지면 메모리 점유가 엄청나게 많아지겠군요..!
좋은 인사이트 감사합니다!! 👍
````

### review_comment · Hoonjichoi1 · 2026-07-03T18:38:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2695#discussion_r3521431318
- ID: review_comment:3521431318
- 파일: climbing-stairs/Chanz82.py, 줄: 17, 원래 줄: 17

````text
이미 계산했던 값인지 체크하고 바로 반환해 주는거 좋은 거 같아요! 
````

### review_comment · Hoonjichoi1 · 2026-07-03T18:40:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2695#discussion_r3521441830
- ID: review_comment:3521441830
- 파일: climbing-stairs/Chanz82.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3516915027

````text
저도 앞에 피드백 주신 분과 같이 n이 커지면 recursion error가 날 수 도 있을 거 같아서 바텀업 구현을 고려해보시는 것도 좋을 거 같다는 의견입니다!
````

### review_comment · Hoonjichoi1 · 2026-07-03T18:47:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2695#discussion_r3521472699
- ID: review_comment:3521472699
- 파일: valid-anagram/Chanz82.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3516915276

````text
처음에 string s랑 string t랑 길이가 다르면 반복문을 아예 돌지 않고 바로 false를 반환하는 base가 있으면 더 좋을 거 같아요! 
````

## [#2696 [Hoonjichoi] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2696)

### review_comment · hellojoyworldz · 2026-07-03T04:54:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#discussion_r3517545220
- ID: review_comment:3517545220
- 파일: climbing-stairs/hoonjichoi.java, 줄: 14, 원래 줄: 13

````text
n이 1, 2일 때는 이미 답이 정해져 있으니, 반복문 타지 않게 미리 걸러주는 부분이 좋은 것 같아요..!


````

### review_comment · hellojoyworldz · 2026-07-03T04:57:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#discussion_r3517552844
- ID: review_comment:3517552844
- 파일: climbing-stairs/hoonjichoi.java, 줄: 24, 원래 줄: 25

````text
맨 마지막줄을 비워 컨벤션에 맞춰야할거같아요
````

### review_comment · hellojoyworldz · 2026-07-03T05:02:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#discussion_r3517568989
- ID: review_comment:3517568989
- 파일: valid-anagram/hoonjichoi1.java, 줄: 30, 원래 줄: 36

````text
이 반복문은 2번째 반복문에서 처리해줘도 좋을 듯 싶습니다..!
````

### review_comment · parkhojeong · 2026-07-04T13:48:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#discussion_r3523290996
- ID: review_comment:3523290996
- 파일: valid-anagram/hoonjichoi1.java, 줄: 24, 원래 줄: 30

````text
개선해보면 좋을 거 같은 포인트 적어보았어요.
- getOrDefault 와 early return 을 사용하면 가독성을 높일 수 있을 거 같습니다.  
- 변수명도 c, c2로 다른데 c로 사용해도 괜찮을 거 같습니다! 사소하지만 c로 읽다가 c2가 나오는 것보다 c->c 또는 c1 -> c2의 흐름이 조금 더 자연스러울 거 같습니다. 개인적으로는 이 문제에선 c -> c 로 임시 변수는 같은 네이밍이 좋을 거 같습니닷
- 마지막 루프 조건식은 두번 째 조건식으로 합쳐도 될 거 같습니다

코드는 이런 식으로 될 거 같습니다 :) 
```suggestion
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        for (int j = 0; j < t.length(); j++) {
            Character c = t.charAt(j);
            if (!map.containsKey(c) || map.get(c) <= 0) {
                return false;
            }

            map.put(c, map.get(c) - 1);
        }
```
````

### review_comment · parkhojeong · 2026-07-04T13:52:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#discussion_r3523296739
- ID: review_comment:3523296739
- 파일: climbing-stairs/hoonjichoi1.java, 줄: None, 원래 줄: 24

````text
몇 가지 생각나는 것들 적어봅니다 :)
- temp는 포문 안에서만 사용되니 스코프를 안쪽으로 옮겨서 필요한 스코프에 변수 선언해도 좋을 거 같아요.
- result가 의미하는게 현재 포인터 느낌이라 prev와 유사한 성격으로 cur 으로 네이밍해봐도 좋을 거 같습니다.  
- prev, cur 은 한 줄에 쓰는 것도 괜찮아 보이네요

코드는 요런 스타일을 생각했습니다!
```suggestion
        int prev = 1, cur = 2;
        for (int i = 2; i < n ; i++) {
            int temp = cur;
            cur += prev;
            prev = temp;
        }     
        return cur;
```
````

### review · parkhojeong · 2026-07-04T13:55:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#pullrequestreview-4629687756
- ID: review:4629687756
- 리뷰 상태: DISMISSED

````text
수고하셨습니다 :) 커멘트 몇 가지 남겨보았어요!

파일 마지막 개행이 없어 request changed 남겨놓습니다. 관련 가이드도 참고차 남겨드려요. [링크](https://github.com/DaleStudy/leetcode-study/wiki/%EB%8B%B5%EC%95%88-%EC%A0%9C%EC%B6%9C-%EA%B0%80%EC%9D%B4%EB%93%9C#3-%ED%8C%8C%EC%9D%BC%EC%9D%98-%EB%A7%88%EC%A7%80%EB%A7%89%EC%97%90-%EA%B0%9C%ED%96%89%EB%AC%B8%EC%9E%90%EB%A5%BC-%EC%B6%94%EA%B0%80)
````

### issue_comment · Hoonjichoi1 · 2026-07-05T23:40:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#issuecomment-4887997394
- ID: issue_comment:4887997394

````text
피드백 반영했습니다! 개행문자 추가 완료했고, 리뷰 주신 다른 부분도 수정했습니다. 확인 부탁드립니다!
````

### issue_comment · DaleSeo · 2026-07-06T01:56:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2696#issuecomment-4888475501
- ID: issue_comment:4888475501

````text
리뷰 반영이 완료되어(개행 수정 → linelint 통과) 일괄 병합을 위해 승인 처리합니다. 리뷰 감사합니다! 🙇

@DaleStudy 승인
````

## [#2697 [hellojoyworldz] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2697)

### review_comment · parkhojeong · 2026-07-04T04:18:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522550872
- ID: review_comment:3522550872
- 파일: valid-anagram/hellojoyworldz.py, 줄: 8, 원래 줄: 8

````text
간결하고 좋네요!
````

### review_comment · parkhojeong · 2026-07-04T04:19:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522552258
- ID: review_comment:3522552258
- 파일: product-of-array-except-self/hellojoyworldz.py, 줄: 21, 원래 줄: 21

````text
reversed(range(n)) 사용하신거 간결하고 좋네요~
````

### review_comment · parkhojeong · 2026-07-04T04:54:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522593125
- ID: review_comment:3522593125
- 파일: climbing-stairs/hellojoyworldz.py, 줄: 10, 원래 줄: 10

````text
개인적으로는 이런 부분들이 읽으면서 생각을 한 번 더 하게 되었던 거 같습니다! 
- prev2, prev1에 1, 1 이 할당된 것도 문제의 조건과 어떻게 연결되는건지 
- n = 1, n = 2 일때 어떻게 처리되는지 
- prev1이 리턴하는게 n 값 까지 계산한 후 prev1 을 리턴하는 것인지

가독성을 고려한다면 배열을 사용해봐도 괜찮을 거 같습니다~ 
```py
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        arr = [0] * n
        arr[0], arr[1] = 1, 2

        for i in range(2, n):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[-1]

```
````

### review_comment · parkhojeong · 2026-07-04T04:59:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522598739
- ID: review_comment:3522598739
- 파일: 3sum/hellojoyworldz.py, 줄: 15, 원래 줄: 15

````text
정렬되어 있는 상태라 nums[i] > 0 인 부분은 break해도 좋을 거 같습니다!
ex. [-1, 0, 1, 2, 3, 4, 5, 6, 7], i = 2 부터는 `양수 + 양수 + 양수`
````

### review_comment · parkhojeong · 2026-07-04T05:04:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522608149
- ID: review_comment:3522608149
- 파일: validate-binary-search-tree/hellojoyworldz.py, 줄: 21, 원래 줄: 21

````text
(log < node.val < high) 사용하신거 좋네요!
````

### review · parkhojeong · 2026-07-04T05:08:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#pullrequestreview-4628863856
- ID: review:4628863856
- 리뷰 상태: APPROVED

````text
코드가 간결해서 읽기 좋았던 거 같습니다. 수고하셨습니다~!
````

### review_comment · hellojoyworldz · 2026-07-04T09:50:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522951540
- ID: review_comment:3522951540
- 파일: climbing-stairs/hellojoyworldz.py, 줄: 10, 원래 줄: 10
- 답글 대상: review_comment:3522593125

````text
안 그래도 가독성 부분이 고민이였는데, 
제안해 주신 것처럼 배열을 쓰니까 흐름이 훨씬 직관적이고 좋네요!
````

### review_comment · hellojoyworldz · 2026-07-04T09:54:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2697#discussion_r3522957658
- ID: review_comment:3522957658
- 파일: 3sum/hellojoyworldz.py, 줄: 15, 원래 줄: 15
- 답글 대상: review_comment:3522598739

````text
아 그러네요, 제가 놓쳤습니다
세심한 피드백 정말 감사합니다! 🙇‍♂️
````

## [#2699 [seueooo] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2699)

### review_comment · togo26 · 2026-07-03T16:13:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2699#discussion_r3520956992
- ID: review_comment:3520956992
- 파일: climbing-stairs/seueooo.js, 줄: 19, 원래 줄: 19

````text
`dp[i - 1]`, `dp[i - 2]` 이외의 배열 값들은 기억할 필요 없기 때문에 필요한 값들만 변수로 처리해서 공간 복잡도 낮출 수 있을 것 같습니다.
````

### review · togo26 · 2026-07-03T16:20:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2699#pullrequestreview-4627033018
- ID: review:4627033018
- 리뷰 상태: APPROVED

````text
풀이 잘 담아주셨네요. 수고하셨습니다 LGTM👍
````

## [#2700 [togo26] WEEK 02 solutions](https://github.com/DaleStudy/leetcode-study/pull/2700)

### review_comment · parkhojeong · 2026-07-03T17:31:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3521227896
- ID: review_comment:3521227896
- 파일: validate-binary-search-tree/togo26.js, 줄: 10, 원래 줄: 10

````text
가독성 좋게 잘 풀어주신 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-03T17:38:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3521248292
- ID: review_comment:3521248292
- 파일: product-of-array-except-self/togo26.js, 줄: 37, 원래 줄: 37

````text
첫번째 풀이가 left, right, result를 각각 집중해서 처리하는 로직이라 쉽게 이해가 가는 것 같네요! 
````

### review_comment · parkhojeong · 2026-07-03T17:44:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3521264025
- ID: review_comment:3521264025
- 파일: climbing-stairs/togo26.js, 줄: 27, 원래 줄: 27

````text
첫 번째 풀이가 점화식이 한 눈에 보여서 가독성은 더 좋은 거 같네요! 

두번 째 풀이도 공간복잡도가 유리해서 좋은데요. pre1, pre2가 단순히 선언 순서에 따라 1, 2 인지 현재 포인터 기준으로 1,2 번째 전인건지 간단한 주석이 있어도 좋을 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-03T17:46:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3521272399
- ID: review_comment:3521272399
- 파일: 3sum/togo26.js, 줄: 57, 원래 줄: 57

````text
막히는 지점 없이 잘 읽히는 코드인 거 같습니다! 👍 
````

### review_comment · parkhojeong · 2026-07-03T17:56:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3521299747
- ID: review_comment:3521299747
- 파일: valid-anagram/togo26.js, 줄: 25, 원래 줄: 25

````text
reduce 로직에서 key가 없는 경우 `undefined + 1 || 1` -> `NaN || 1` -> `1` 의 순서로 평가되는데 `(undifiend ?? 0) + 1` 과 같이 undefined에 대한 fallback을 사용해보셔도 좋을 거 같습니다!

```suggestion
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;
  const sCount = [...s].reduce((acc, cur) => {
    acc[cur] = (acc[cur] ?? 0) + 1;
    return acc;
  }, {});
  const tCount = [...t].reduce((acc, cur) => {
    acc[cur] = (acc[cur] ?? 0) + 1 ;
    return acc;
  }, {});
  return Object.keys(sCount).every(key => sCount[key] === tCount[key]);
};
```
````

### review · parkhojeong · 2026-07-03T18:02:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#pullrequestreview-4627327726
- ID: review:4627327726
- 리뷰 상태: APPROVED

````text
수고하셨습니다~! 가독성이 좋은 코드 작성해주셔서 쉽게 읽혔던 거 같습니다! 
커멘트 남겨보았습니다 :)
````

### review_comment · togo26 · 2026-07-04T09:18:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3522916516
- ID: review_comment:3522916516
- 파일: climbing-stairs/togo26.js, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3521264025

````text
좋은 의견 감사합니다! 변수명이 애매하긴했는데 다음번에는 주석으로 보조 설명 붙여보겠습니다.
````

### review_comment · togo26 · 2026-07-04T09:20:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2700#discussion_r3522917964
- ID: review_comment:3522917964
- 파일: valid-anagram/togo26.js, 줄: 25, 원래 줄: 25
- 답글 대상: review_comment:3521299747

````text
의견 감사합니다. 암시적 변환으로 두었는데 제안 주신 방향이 더 좋네요. 업데이트하겠습니다 감사합니다.
````

## [#2701 [parkhojeong] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2701)

### review_comment · alphaorderly · 2026-07-03T17:58:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2701#discussion_r3521311055
- ID: review_comment:3521311055
- 파일: product-of-array-except-self/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
1. 해당 문제에는 나눗셈을 쓰지 않도록 권장하고 있어요! 한번 시도해보시면 좋을 것 같아요
2. 나눗셈을 쓰지 않는 방식을 사용하시면 자연스럽게 0의 갯수에 따른 edge case들을 신경쓰지 않아도 됩니다!
````

### issue_comment · parkhojeong · 2026-07-03T18:32:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2701#issuecomment-4878630328
- ID: issue_comment:4878630328

````text
> 1. 해당 문제에는 나눗셈을 쓰지 않도록 권장하고 있어요! 한번 시도해보시면 좋을 것 같아요
> 2. 나눗셈을 쓰지 않는 방식을 사용하시면 자연스럽게 0의 갯수에 따른 edge case들을 신경쓰지 않아도 됩니다!

@alphaorderly 오 해당 내용을 놓쳤네요. 다시 풀어서 업데이트 해두었습니다. https://github.com/DaleStudy/leetcode-study/commit/f1fa20ec552d2b1051d9de3eeeef18e7426ec783 리뷰 감사합니다! :) 

````

### review · sonshn · 2026-07-04T05:23:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2701#pullrequestreview-4628941804
- ID: review:4628941804
- 리뷰 상태: APPROVED

````text
전체적으로 문제의 의도에 맞게 잘 풀이해주신 것 같습니다! 개인적으로 3sum 문제에서 two pointer 알고리즘을 사용하신 것과, Validate BST 문제에서 DFS 함수를 구현하신 것에서 많이 배워갑니다! 이번 주도 고생 많으셨습니다!
````

### issue_comment · parkhojeong · 2026-07-04T07:18:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2701#issuecomment-4881112502
- ID: issue_comment:4881112502

````text
> 전체적으로 문제의 의도에 맞게 잘 풀이해주신 것 같습니다! 개인적으로 3sum 문제에서 two pointer 알고리즘을 사용하신 것과, Validate BST 문제에서 DFS 함수를 구현하신 것에서 많이 배워갑니다! 이번 주도 고생 많으셨습니다!

리뷰 감사합니다! 3sum이 까다로워서 시간을 많이 투자했던 거 같습니다.
이번 주도 고생하셨습니다 :)
````

## [#2702 [sonshn] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2702)

### review_comment · okyungjin · 2026-07-04T13:57:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2702#discussion_r3523301972
- ID: review_comment:3523301972
- 파일: climbing-stairs/sonshn.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523255408

````text
깔끔한 풀이 잘 봤습니다. 공간 복잡도를 O(1)으로 최적화 해볼 수 있을 것 같습니다~
````

### review_comment · okyungjin · 2026-07-04T14:03:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2702#discussion_r3523308889
- ID: review_comment:3523308889
- 파일: valid-anagram/sonshn.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523255454

````text
정렬을 제거해서 O(N log N)을 O(N)으로 최적화해보면 좋을 것 같습니다!
````

### review · okyungjin · 2026-07-04T14:03:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2702#pullrequestreview-4629707359
- ID: review:4629707359
- 리뷰 상태: APPROVED

````text
깔끔한 풀이 잘 봤습니다! 다음주도 파이팅입니다~
````

## [#2704 [sangbeenmoon] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2704)

### issue_comment · DaleSeo · 2026-07-04T13:01:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#issuecomment-4882088575
- ID: issue_comment:4882088575

````text
@sangbeenmoon https://github.com/DaleStudy/leetcode-study/pull/2704#issuecomment-4881159532
````

### review_comment · parkhojeong · 2026-07-04T14:32:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#discussion_r3523346423
- ID: review_comment:3523346423
- 파일: validate-binary-search-tree/sangbeenmoon.py, 줄: None, 원래 줄: 74

````text
None은 is 로 비교하는 것으로 권장되어서 참고하시면 좋을 거 같아요! 
`Comparisons to singletons like None should always be done with is or is not, never the equality operators.`
https://peps.python.org/pep-0008/#programming-recommendations

그리고 변수명은 mm, MM이 어떤 값인지 알기가 어려워서 의미를 담아 보아도 좋을 거 같습니다 :)
```suggestion
        def isValid(max_val, min_val, cur: TreeNode) -> bool:
            if cur is None:
                return True

            if max_val is not None and cur.val <= max_val:
                return False

            if min_val is not None and cur.val >= min_val:
                return False

            return isValid(max_val, cur.val, cur.left) and isValid(cur.val, min_val, cur.right)

        return isValid(None, None, root)
```
````

### review_comment · parkhojeong · 2026-07-04T14:38:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#discussion_r3523356350
- ID: review_comment:3523356350
- 파일: 3sum/sangbeenmoon.py, 줄: 57, 원래 줄: 57

````text
해시맵을 사용해서 candidate를 담아서 중복을 체크하셨군요! 
이미 정렬이 된 상태라서 nums[left] == nums[left+1] 인 케이스를 스킵해주면(right도 동일) candidate를 사용하지 않고 not in 로직을 안타기 때문에 더 최적화가 가능할 거 같아요! 

````

### review_comment · parkhojeong · 2026-07-04T14:47:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#discussion_r3523365693
- ID: review_comment:3523365693
- 파일: 3sum/sangbeenmoon.py, 줄: 58, 원래 줄: 58

````text
성공한 경우 right -= 1 도 함께 해주면 좋을 거 같아요!
````

### review_comment · parkhojeong · 2026-07-04T14:49:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#discussion_r3523368163
- ID: review_comment:3523368163
- 파일: 3sum/sangbeenmoon.py, 줄: 50, 원래 줄: 50

````text
정렬이 된 상태라 nums[i] 와 nums[i - 1] 이 같은 경우는 스킵해주고 nums[i] > 0 이 된 상태에서는 break 해주면 최적화가 가능할 거 같습니다 :) 

ex. [ -2, -1, -1, -1, 0, 1, 2, 3] , -1이 한번인 경우만 실행하고 이후는 스킵, nums[i]가 0보다 커지면 `양수 + 양수 + 양수` 이기 때문에 종료
````

### review · parkhojeong · 2026-07-04T14:53:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#pullrequestreview-4629746963
- ID: review:4629746963
- 리뷰 상태: COMMENTED

````text
수고하셨습니다! 몇 가지 개선 포인트 커멘트로 남겨보았어요 :)
달레님 커멘트(프로젝트 주차 설정) 확인해주시면 될 거 같습니다~
````

### review · alphaorderly · 2026-07-05T05:05:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#pullrequestreview-4630786404
- ID: review:4630786404
- 리뷰 상태: APPROVED

````text
깔끔하게 잘 해결하신것 같습니다! 고생하셨어요!
````

### review_comment · sangbeenmoon · 2026-07-05T08:59:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#discussion_r3524592617
- ID: review_comment:3524592617
- 파일: validate-binary-search-tree/sangbeenmoon.py, 줄: None, 원래 줄: 74
- 답글 대상: review_comment:3523346423

````text
오 이런 권장사항이 있는지는 몰랐네요 ㅎㅎ 공식문서까지 찾아서 제안해주셔서 감사합니다 👍 
````

### review_comment · sangbeenmoon · 2026-07-05T09:00:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2704#discussion_r3524593709
- ID: review_comment:3524593709
- 파일: 3sum/sangbeenmoon.py, 줄: 57, 원래 줄: 57
- 답글 대상: review_comment:3523356350

````text
좀 더 깔끔하게 중복 체크할 수 있는 방법이 있었네요. 짚어주셔서 감사합니다
````

## [#2705 [j2h30728] WEEK 02 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2705)

### review_comment · ICE0208 · 2026-07-04T13:21:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2705#discussion_r3523256775
- ID: review_comment:3523256775
- 파일: valid-anagram/j2h30728.ts, 줄: 1, 원래 줄: 1

````text
공간 복잡도를 O(n)으로 적어주셨는데,
문제 조건에 `s and t consist of lowercase English letters.`라고 나와 있으니
Map에 저장되는 key 개수가 최대 26개라서 O(1)이 맞는 것 같습니다!

혹은 가능한 문자 집합의 크기를 k라고 본다면,  봇이 제안한 대로 O(k)도 맞는 표현인 듯합니다!
````

### review · ICE0208 · 2026-07-04T13:27:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2705#pullrequestreview-4629653499
- ID: review:4629653499
- 리뷰 상태: APPROVED

````text
2주차 문제풀이 고생하셨습니다~
````

### review_comment · ICE0208 · 2026-07-04T13:34:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2705#discussion_r3523274481
- ID: review_comment:3523274481
- 파일: valid-anagram/j2h30728.ts, 줄: 1, 원래 줄: 1

````text
저는 각각 따로 개수를 세서 비교하는 방식만 생각했는데,
하나는 증가시키고 다른 하나는 감소시켜서 최종 값이 0인지 확인하는 방법도 있었네요!

좋은 접근 방식 배워갑니다~

````

### review_comment · j2h30728 · 2026-07-04T17:07:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2705#discussion_r3523567423
- ID: review_comment:3523567423
- 파일: valid-anagram/j2h30728.ts, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3523256775

````text
오 감사합니다!
````

## [#2707 [alphaorderly] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2707)

### review_comment · Zero-1016 · 2026-07-05T06:28:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524418006
- ID: review_comment:3524418006
- 파일: combination-sum/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
답 둘 다 정확한 풀이네요. 👍

한 가지 궁금한 게, 실제 제출은 DP로 하고 백트래킹을 주석으로 남기신 이유가 있을까요?

이 문제(모든 조합 나열)는 출력 자체가 지수적으로 커질 수 있어서, DP 쪽에 적힌 `O(N*target) / O(target)`이 실제보다 낙관적으로 보여요. 

`dp[j].append(partial + [c])` 부분이 매번 리스트를 통째로 복사하고, `dp[0..target]` 각 칸에 중간 조합들을 다 들고 있어서 시간/공간 모두 그 표기보단 커질 것 같아요. 오히려 주석 처리된 백트래킹이 `path` 하나를 `push/pop`으로 재활용해서 메모리 면에선 더 유리해 보이는데, 혹시 DP를 고른 특별한 이유가 있으면 궁금합니다!
````

### review_comment · Zero-1016 · 2026-07-05T06:28:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524418526
- ID: review_comment:3524418526
- 파일: decode-ways/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
👍 
````

### review_comment · Zero-1016 · 2026-07-05T06:31:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524421456
- ID: review_comment:3524421456
- 파일: valid-palindrome/alphaorderly.py, 줄: 42, 원래 줄: 42

````text
바깥 while True: + break 구조가 동작은 완벽한데, 조건을 위로 올리면 흐름이 더 읽기 쉬워질 것 같아요.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
```
````

### review · Zero-1016 · 2026-07-05T06:34:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#pullrequestreview-4630862015
- ID: review:4630862015
- 리뷰 상태: APPROVED

````text
안녕하세요 금주 리뷰를 맡게 되었습니다 잘 부탁드려요 :)

코드를 보면 전체적으로 로직이 잘 써져있고 여러 방면으로 풀어보신 게 인상적이었습니다.

저도 여러 방면으로 풀어보는 걸 연습해 봐야겠네요.
````

### review_comment · alphaorderly · 2026-07-05T06:37:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524426263
- ID: review_comment:3524426263
- 파일: combination-sum/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524418006

````text
맞아요, 리스트를 통으로 복사하는 과정에서 오버헤드가 생깁니다!
다만 백트래킹은 target의 값이 커지면 커질수록 exponential하게 시간복잡도가 커지기 때문에 사실상 큰 값에서는 사용하기 어려울것이 있고, 그에 비해서 trade-off를 고려했을때 DP가 좀 더 낫다고 판단했어요!
````

### review_comment · alphaorderly · 2026-07-05T06:38:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524427098
- ID: review_comment:3524427098
- 파일: valid-palindrome/alphaorderly.py, 줄: 42, 원래 줄: 42
- 답글 대상: review_comment:3524421456

````text
그렇네요, 차라리 얼리 리턴을 하는게 나았긴 하네요
````

### review_comment · alphaorderly · 2026-07-05T06:42:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524430760
- ID: review_comment:3524430760
- 파일: combination-sum/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524418006

````text
또한 백트래킹과 달리 재귀를 쓰지 않으니 재귀 호출에 의한 스택 오버헤드도 피할수 있겠죠
````

### review_comment · Zero-1016 · 2026-07-05T06:48:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524436816
- ID: review_comment:3524436816
- 파일: combination-sum/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524418006

````text
재귀 스택 회피는 고려할만한 트레이드오프인 것 같네요 파이썬은 기본 재귀 한도가 1000으로 알고있어 target이 아주 크면 백트래킹이 RecursionError를 낼 수도 있으니, 이건 DP가 분명히 이득 보는 지점으로 생각됩니다. 🥇 

다만 두 가지만 덧붙이면요. (1) 메모리는 재귀 스택 O(depth)보다 DP가 지는 짐(중간 조합 전부 저장 + partial 복사)이 더 커서, 총량은 백트래킹이 가볍습니다. (2) 시간은 결과 조합 수가 지수적이라 둘 다 같은 지수 하한이에요 — 이 부분엔 DP도 이득이 없어요. 그래서 강점이 서로 다른 쪽(DP=스택 안정, 백트래킹=메모리/상수)이라고 보는 게 정확할 것 같아요.
````

### review_comment · alphaorderly · 2026-07-05T07:24:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2707#discussion_r3524474567
- ID: review_comment:3524474567
- 파일: combination-sum/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524418006

````text
1. 그건 확실히 그렇겠네요, 백트래킹은 정답을 바로바로 쌓아나가니 사실상 쓸모없이 쓰이는 메모리 공간이 거의 없을테니까요
2. 그렇군요
````

## [#2708 [Zero-1016] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2708)

### review_comment · namuuCY · 2026-07-05T02:43:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2708#discussion_r3524200783
- ID: review_comment:3524200783
- 파일: number-of-1-bits/Zero-1016.ts, 줄: 14, 원래 줄: 14

````text
비트연산자로 하는 풀이 배워갑니다!
````

### review · namuuCY · 2026-07-05T02:45:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2708#pullrequestreview-4630634652
- ID: review:4630634652
- 리뷰 상태: APPROVED

````text
안녕하세요! 이번 주차 리뷰를 맡게된 장철영이라고 합니다.

우선 현재 푸신 문제까지 리뷰를 남겨놨고, 
나머지 문제들 업데이트되면 추가 리뷰 드리도록 하겠습니다!
````

### issue_comment · DaleSeo · 2026-07-10T22:31:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2708#issuecomment-4940052787
- ID: issue_comment:4940052787

````text
@Zero-1016 다음 PR부터는 Week 설정 누락되지 않도록 부탁드리겠습니다 🙏

<img width="1784" height="868" alt="2026-07-10 at 18 30 20" src="https://github.com/user-attachments/assets/0d61c44b-a9f6-4e3c-89bb-88d8366e3c6a" />

````

## [#2709 [namuuCY] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2709)

### review_comment · dolphinflow86 · 2026-07-05T03:51:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3524261001
- ID: review_comment:3524261001
- 파일: valid-palindrome/namuuCY.java, 줄: 46, 원래 줄: 46

````text
@namuuCY 안녕하세요 이번 주 리뷰를 맡게 된 최성호 입니다.

전체적으로 함수화를 잘 해주셨네요! Character.isLetterOrDigit()도 직접 구현해주셔서
나중에 좀 더 복잡한 조건이 나오면 다양하게 응용이 가능해서 좋아 보입니다.
````

### review_comment · alphaorderly · 2026-07-05T05:17:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3524354532
- ID: review_comment:3524354532
- 파일: combination-sum/namuuCY.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524197525

````text
해당 문제는 생각보다 DP로 구현했을때 이점이 많고, 또 아이디어가 그렇게 어렵지 않아서 한번 시도해보시는것도 좋을것 같네요!

백트래킹은 전반적으로 엄청 잘 구현하신것 같아요
````

### review_comment · alphaorderly · 2026-07-05T05:18:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3524355234
- ID: review_comment:3524355234
- 파일: decode-ways/namuuCY.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524197551

````text
1개 파싱이랑 2개 파싱하는 부분 함수로 따로 빼서 코드 깔끔하게 하신거 인상적이네요!
````

### review_comment · alphaorderly · 2026-07-05T05:20:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3524357012
- ID: review_comment:3524357012
- 파일: maximum-subarray/namuuCY.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524197579

````text
해당 문제 깔끔하게 해결하시긴 했는데
1. 매직 넘버 ( - 200000 ) 안 써도 되고
2. O(1) 공간 복잡도

로 해결하는 방법도 있어서 어차피 시간 많이 남았으니 천천히 한번 찾아 보시는 것도 좋을 것 같습니다!
````

### review_comment · alphaorderly · 2026-07-05T05:22:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3524358359
- ID: review_comment:3524358359
- 파일: number-of-1-bits/namuuCY.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524197599

````text
% 연산보다 & 비트연산자가 보통 조금 빠르죠, 이걸 이용해서 해결하시면 정말 쥐똥만큼 최적화가 되긴 하겠지만 
제 생각에 면접관에게 어느정도 비트연산에 익숙하다는 느낌을 주기 좋을것 같다고 생각해요!
문제에 사용하신 %, / 연산자 모두 비트연산자로 해결 가능하니 한번 시도 해 보시는 것도 좋을 것 같아요!
````

### review_comment · alphaorderly · 2026-07-05T05:24:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3524359874
- ID: review_comment:3524359874
- 파일: decode-ways/namuuCY.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3524197551

````text
해당 문제도 공간복잡도 O(1)에 해결 가능하니 나중에 시도 해보시면 좋겠네요
````

### review_comment · dolphinflow86 · 2026-07-09T14:27:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2709#discussion_r3552388479
- ID: review_comment:3552388479
- 파일: combination-sum/namuuCY.java, 줄: 19, 원래 줄: 19

````text
@namuuCY 벡트래킹 하기 전에 미리 candidates 배열 정렬을 하면, base case까지 가기 전에 미리 종료되어서 조금 더 효율적일 것 같습니다.
````

## [#2710 [dolphinflow86] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2710)

### review_comment · dolphinflow86 · 2026-07-09T14:29:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3552400574
- ID: review_comment:3552400574
- 파일: combination-sum/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
@DaleStudy/coach 주석에 복잡도 추가 완료
````

### review_comment · okyungjin · 2026-07-11T07:28:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3563577553
- ID: review_comment:3563577553
- 파일: combination-sum/dolphinflow86.py, 줄: 7, 원래 줄: 7

````text
저는 `path.copy()`와 같이 작성했는데 이렇게도 쓸 수 있군요
````

### review_comment · okyungjin · 2026-07-11T07:36:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3563592123
- ID: review_comment:3563592123
- 파일: number-of-1-bits/dolphinflow86.py, 줄: 10, 원래 줄: 10

````text
`n & 1`이랑 `n >> 1` 처럼 비트 연산으로만 접근하려 했는데, 결국 2로 나눈 나머지를 확인하고 2로 나누는 과정과 같다는 것을 깨달았습니다...
````

### review_comment · okyungjin · 2026-07-11T07:43:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3563601699
- ID: review_comment:3563601699
- 파일: combination-sum/dolphinflow86.py, 줄: 14, 원래 줄: 14

````text
`candidates.sort()` 정렬한 다음에 이렇게 멈추도록 하면 최적화가 가능하군요!
풀면서 최적화  가능할 것 같은데 .. 하다가 그냥 넘겼는데 하나 배워갑니다. 감사합니다.
````

### review_comment · okyungjin · 2026-07-11T07:46:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3563608662
- ID: review_comment:3563608662
- 파일: combination-sum/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3560147991

````text
@dolphinflow86 이 문제 시간 복잡도 계산이 까다로운 것 같은데 한번만 풀어서 설명해주실 수 있나요? 이해를 도와주시면 감사하겠습니다 ㅎㅎ
````

### issue_comment · okyungjin · 2026-07-11T07:49:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#issuecomment-4943687978
- ID: issue_comment:4943687978

````text
@dolphinflow86 풀이 잘 봤습니다! 최적화와 복잡도까지 꼼꼼하게 고민하신 점이 인상적이었어요 👍

이번 주 일정에 포함된 Decode Ways와 Maximum Subarray는 제가 아직 풀지 못해서, 먼저 풀어본 세 문제에만 코멘트를 남겼습니다. 두 문제도 풀이를 완료하면 다시 확인하고 코멘트 남기겠습니다.

이번 주도 고생 많으셨습니다! 다음 주도 파이팅하세요.
````

### review_comment · dolphinflow86 · 2026-07-11T12:47:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3564175356
- ID: review_comment:3564175356
- 파일: combination-sum/dolphinflow86.py, 줄: 7, 원래 줄: 7
- 답글 대상: review_comment:3563577553

````text
@okyungjin 네 이렇게 하는방법도 있더라고요? 근데 path.copy가 더 명시적인 것 같아서 경진님 방법이 더 가독성이 좋을 것 같아요!
````

### review_comment · dolphinflow86 · 2026-07-11T12:49:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3564178325
- ID: review_comment:3564178325
- 파일: number-of-1-bits/dolphinflow86.py, 줄: 10, 원래 줄: 10
- 답글 대상: review_comment:3563592123

````text
@okyungjin 비트연산자가 성능면에서는 더 좋을 것 같아요. 이번에는 숫자로 한번 나눠보는 건 어떨까 해서 한번 해봤는데 나름 재미있더라고요 ㅎㅎ
````

### review_comment · dolphinflow86 · 2026-07-11T12:51:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3564180424
- ID: review_comment:3564180424
- 파일: combination-sum/dolphinflow86.py, 줄: 14, 원래 줄: 14
- 답글 대상: review_comment:3563601699

````text
@okyungjin 아 이 부분은 사실 저도 찾아보면서 최적화로 적용했는데, 중복으로 조합을 만들지 않고 이렇게 early return이 가능하더라고요. 
````

### review_comment · dolphinflow86 · 2026-07-11T13:01:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2710#discussion_r3564194080
- ID: review_comment:3564194080
- 파일: combination-sum/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3560147991

````text
@okyungjin 맞아요, 복잡도 분석이 까다로웠는데, 기본적으로 모든 조합을 탐색하면 보통 O(2^N)이잖아요? 그런데 이 문제의 경우 같은 숫자를 무제한으로 넣을 수 있기 때문에, 조금 까다로워집니다. 그래서 target 숫자에 도달할때까지 숫자를 계속 선택해서 내려가야하는데, 가장 깊게 내려가는 최악의 경우를 생각 해 보면, 배열에서 가장 작은 숫자(M)만 계속 골라서 target(T) 숫자를 만드는 경우입니다. 따라서 이 경우 트리의 최대 깊이가 T/M이 되고, 우리는 매 노드에서 다음 자식노드로 나갈 수 있는 선택지인 최대 N개를 가지므로, 최종 시간복잡도가 N^(T/M)이 됩니다. 저도 이거 문제 풀면서 분석하면서 이해하게 되었습니다.
````

## [#2711 [okyungjin] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2711)

### review_comment · ICE0208 · 2026-07-11T08:31:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2711#discussion_r3563693378
- ID: review_comment:3563693378
- 파일: combination-sum/okyungjin.py, 줄: 40, 원래 줄: 40

````text
주석에 `배열이 매번 깊은 복사되는 비효율`을 개선했다고 적혀 있는데, 첫 번째 풀이에서 실제로 깊은 복사가 발생하는 부분이 어디인지 궁금합니다!

혹시 `combination + [num]`에서 매번 새로운 리스트가 생성되는 비용을 깊은 복사라고 표현하신 걸까요? 👀

````

### review · ICE0208 · 2026-07-11T08:38:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2711#pullrequestreview-4677145692
- ID: review:4677145692
- 리뷰 상태: APPROVED

````text
코드가 직관적이고 주석도 상세하게 작성되어 있어 빠르게 리뷰할 수 있었습니다!

이번 주도 고생 많으셨고, 다음 주 문제 풀이도 파이팅입니다! 🙌
````

### review_comment · okyungjin · 2026-07-11T12:43:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2711#discussion_r3564168820
- ID: review_comment:3564168820
- 파일: combination-sum/okyungjin.py, 줄: 40, 원래 줄: 40
- 답글 대상: review_comment:3563693378

````text
얕은 복사라고 적어야 하는데 깊은 복사라고 잘못 적었습니다.
dfs 재귀 호출 시에 매번 새로운 리스트가 생성되는 비용을 표현한게 맞습니다!



````

## [#2712 [ICE0208] WEEK 03 solutions](https://github.com/DaleStudy/leetcode-study/pull/2712)

### review_comment · JeonJe · 2026-07-11T08:30:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2712#discussion_r3563691717
- ID: review_comment:3563691717
- 파일: valid-palindrome/ICE0208.java, 줄: 20, 원래 줄: 20

````text
필터링된 문자열을 새로 만들지 않고 투 포인터로 in-place 비교해서 공간 O(1)로 풀 수 있었군요!
안쪽 while에 left < right 가드를 둬서 포인터가 만나는(교차) 케이스에서도 안전하게 처리된 것도 꼼꼼하네요. 복잡도 주석까지 정확하게 달려 있어서 읽기 편했습니다.
````

### review_comment · JeonJe · 2026-07-11T08:41:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2712#discussion_r3563719804
- ID: review_comment:3563719804
- 파일: maximum-subarray/ICE0208.java, 줄: 13, 원래 줄: 13

````text
분할 정복으로도 풀 수 있다는 걸 처음 알았네요!!

제가 이해한 이 풀이 방식은 
배열을 가운데로 자르면 최대 부분배열은 완전히 왼쪽, 완전히 오른쪽, 가운데를 걸치는 경우 셋 중 하나이다.  앞의 둘은 재귀로 구하고, 걸치는 경우는 mid에서 좌우로 뻗어가며 최대 누적합을 더해 구한 뒤, 이 셋의 최댓값을 고른다. 로 이해하였습니다

이렇게 믄제를 "분해"하는 사고틀은 다른 문제에도 응용할 수 있을 것 같습니다. 👍👍👍 
````

### review · JeonJe · 2026-07-11T08:54:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2712#pullrequestreview-4677142992
- ID: review:4677142992
- 리뷰 상태: APPROVED

````text
안녕하세요 이번주차 코드 리뷰를 맡게 된 이전제입니다!
  
5문제 모두 복잡도 주석까지 꼼꼼히 정리해주셔서 읽기 편했어요. 특히 maximum-subarray 분할정복 풀이는 저도 이번에 처음 봐서 잘 배워갑니다. 고생하셨습니다!
````

### review_comment · ICE0208 · 2026-07-11T09:48:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2712#discussion_r3563888156
- ID: review_comment:3563888156
- 파일: maximum-subarray/ICE0208.java, 줄: 13, 원래 줄: 13
- 답글 대상: review_comment:3563719804

````text
저도 이번에 처음으로 분할 정복 방식으로 풀어봐서 오류도 많이 나고, 이해하는 데 시간도 꽤 걸렸습니다ㅎㅎ 🤣
그래도 직접 구현해보면서 많이 배울 수 있었던 문제였던 것 같아요.
꼼꼼하게 리뷰해주셔서 감사합니다! 이번 주도 고생 많으셨습니다 🙌

````

## [#2713 [JeonJe] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2713)

### review_comment · seongmin36 · 2026-07-10T11:23:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3558501563
- ID: review_comment:3558501563
- 파일: number-of-1-bits/JeonJe.java, 줄: 12, 원래 줄: 12

````text
이건 정말 단순한 재미 요소긴 한데요, 간단한 증감연산의 경우에는 이렇게도 표현해볼 수 있을 것 같습니다.
```suggestion
            answer += n & 1;
```
````

### review_comment · seongmin36 · 2026-07-10T11:38:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3558597212
- ID: review_comment:3558597212
- 파일: valid-palindrome/JeonJe.java, 줄: 13, 원래 줄: 13

````text
우와, 문자를 배열로 나눠서 하나씩 비교하는 거군요. 내장함수 `isLetterOrDigit()`으로 쉽게 비교할 수 있는 방식인가보네요.. java는 뭔가 투박해보여도 꽤 친절한 언어인 것 같습니다!
````

### review_comment · seongmin36 · 2026-07-10T11:54:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3558683156
- ID: review_comment:3558683156
- 파일: combination-sum/JeonJe.java, 줄: 12, 원래 줄: 12

````text
```suggestion
```

이 변수는 실제로 사용되지않는 데드코드인 것 같습니다. 없어도 될 것 같습니다!
````

### review_comment · seongmin36 · 2026-07-10T12:29:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3558869118
- ID: review_comment:3558869118
- 파일: maximum-subarray/JeonJe.java, 줄: 16, 원래 줄: 16

````text
직관적으로 잘 구현하신 것 같습니다. 여기서 SC를 O(1)로 최적화해볼 수 있을 것 같습니다.

현재 점화식이 참조중인 값이 이전값을 담는 것 하나라서 dp[] 대신에 int 변수를 사용해도(현재 상태 하나만으로도) 구현이 가능합니다!

```suggestion
        int current_max = nums[n - 1];
        int answer = current_max;

        for (int i = n - 2; i >= 0; i--) {
            current_max = Math.max(current_max + nums[i], nums[i]);
            answer = Math.max(answer, current_max);
        }
```
````

### review · seongmin36 · 2026-07-10T12:31:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#pullrequestreview-4670961117
- ID: review:4670961117
- 리뷰 상태: APPROVED

````text
전체적으로 코드를 직관적으로 잘 구현하신 것 같습니다.
3주차도 정말 고생많으셨고, 다음 4주차도 화이팅입니다! 😊
````

### review_comment · JeonJe · 2026-07-11T08:47:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3563739230
- ID: review_comment:3563739230
- 파일: combination-sum/JeonJe.java, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3558683156

````text
불필요 변수가 들어가버렸네요. 피드백 감사합니다!
````

### review_comment · JeonJe · 2026-07-11T08:48:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3563741694
- ID: review_comment:3563741694
- 파일: maximum-subarray/JeonJe.java, 줄: 16, 원래 줄: 16
- 답글 대상: review_comment:3558869118

````text
오호 dp 배열이 아닌, 변수 두개로 공간복잡도를 최적화 할 수도 있겠네요. 
다음 DP문제에 바로 적용해봐야곘습니다 감사합니다 👍 
````

### review_comment · JeonJe · 2026-07-11T08:51:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3563748862
- ID: review_comment:3563748862
- 파일: number-of-1-bits/JeonJe.java, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3558501563

````text
오호 ㅎㅎ +1, +0 으로도 작성이 가능하겠네요. 여기까진 미처 생각하지못했습니다 좋은 팁 감사합니다
````

### review_comment · JeonJe · 2026-07-11T08:52:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2713#discussion_r3563754079
- ID: review_comment:3563754079
- 파일: valid-palindrome/JeonJe.java, 줄: 13, 원래 줄: 13
- 답글 대상: review_comment:3558597212

````text
저도 이번 문제 풀면서 새로 알게 된 함수인데,
자바에도 이런 편리한 함수가 은근히 있는 것 같습니다 ㅎㅎ 
````

## [#2715 [seongmin36] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2715)

### review_comment · togo26 · 2026-07-11T17:36:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2715#discussion_r3564709640
- ID: review_comment:3564709640
- 파일: decode-ways/seongmin36.js, 줄: 40, 원래 줄: 40

````text
로직 상 가장 위에서 `0`을 필터하기 때문에 첫번째 문자가 한가지 케이스라는 걸 보장합니다. 그래서 상단에 `dp[1] = 1`도 같이 초기화 할 수 있습니다. 그러면 루프 인덱스를 2로 시작할 수 있어 자연스럽게 `i >= 2` 삭제할 수 있습니다. (+ `i` 최대 범위도 조정해야 합니다)
````

### review_comment · togo26 · 2026-07-11T17:39:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2715#discussion_r3564714012
- ID: review_comment:3564714012
- 파일: decode-ways/seongmin36.js, 줄: 35, 원래 줄: 35

````text
사소하지만 재할당이 없기 때문에 `const` 사용 가능합니다 :)
```suggestion
    const one_char = s.substring(i - 1, i);
    const two_char = s.substring(i - 2, i);
```
````

### review_comment · togo26 · 2026-07-11T17:40:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2715#discussion_r3564716464
- ID: review_comment:3564716464
- 파일: maximum-subarray/seongmin36.js, 줄: 21, 원래 줄: 21

````text
이렇게 축약할 수 있을 것 같네요.
```suggestion
    cur_sum = Math.max(nums[i], cur_sum + nums[i]);
```
````

### review_comment · togo26 · 2026-07-11T17:50:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2715#discussion_r3564733435
- ID: review_comment:3564733435
- 파일: valid-palindrome/seongmin36.js, 줄: 12, 원래 줄: 12

````text
공간복잡도 관점에서 `toLowerCase()`는 내부적으로 문자열 길이만큼 새로운 문자열을 생성하기 때문에 문자열 n만큼 공간을 사용할 수 있습니다. 따라서 파라미터 값`s` 범위에 따라 현재 구현의 공간 사용은 선형적으로 증가하기 때문에 해당 메소드를 단일 문자열 검증에서 사용하면 복잡도를 상수로 낮출 수 있을 것 같습니다.
````

### review · togo26 · 2026-07-11T17:53:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2715#pullrequestreview-4678450803
- ID: review:4678450803
- 리뷰 상태: APPROVED

````text
전반적으로 로직 잘 구현해주셨습니다. 구현 노트도 함께 있어서 이해하기 쉬웠습니다. 시간/공간 복잡도도 남겨두시면 최적화 검토에 도움이 되실 것 같습니다. 3주차 수고하셨습니다👍
````

## [#2716 [hoonjichoi1] WEEK 03 solutions](https://github.com/DaleStudy/leetcode-study/pull/2716)

### review_comment · parkhojeong · 2026-07-11T18:12:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3564767425
- ID: review_comment:3564767425
- 파일: decode-ways/hoonjichoi1.java, 줄: 22, 원래 줄: 22

````text
`twoDigit >= 10` 인 케이스만 존재해서 > 0 보다는 >= 10 으로 좁혀주는게 좋을 거 같습니다!
```suggestion
        for (int i = n-1; i > -1; i--) { 
            if (s.charAt(i) != '0') {
                dp[i] += dp[i+1];
            }
            if (s.charAt(i) != '0' && i+1 < n) {
                int twoDigit = Integer.valueOf(s.substring(i, i+2));
                if (twoDigit >= 10 && twoDigit < 27) {
                    dp[i] += dp[i+2];
                }
            }
        }
```
````

### review_comment · parkhojeong · 2026-07-11T18:16:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3564774416
- ID: review_comment:3564774416
- 파일: number-of-1-bits/hoonjichoi1.java, 줄: 17, 원래 줄: 17

````text
루프 조건을 조금 바꿔주면 n == 1 처리를 별도로 해주지 않아도 될 거 같습니다!

```suggestion
    public int hammingWeight(int n) {
        int curr = n, result = 0;
        while (curr > 0) {
            if (curr % 2 == 1) {
                result++;
            }
            curr = curr / 2;
        }

        return result;
    }
```
````

### review_comment · parkhojeong · 2026-07-11T18:19:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3564777356
- ID: review_comment:3564777356
- 파일: valid-palindrome/hoonjichoi1.java, 줄: 5, 원래 줄: 5

````text
오타가 있네요
```suggestion
        String converted = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
```
````

### review_comment · parkhojeong · 2026-07-11T18:28:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3564792431
- ID: review_comment:3564792431
- 파일: valid-palindrome/hoonjichoi1.java, 줄: 5, 원래 줄: 5

````text
실제로 돌려보니 replaceAll 비용이 비싸서 runtime 성능이 좋지는 않게 나오는 거 같아요. 
직접 순회하는 방식이나 투포인터 등 다른 방식으로도 풀어보시면 좋을 거 같습니다.

구현체도 참고차 남겨드려요!
https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/regex/Matcher.java#L1221-L1234
````

### review · parkhojeong · 2026-07-11T18:30:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#pullrequestreview-4678515668
- ID: review:4678515668
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 마이너한 커멘트 남겼어요~
````

### review_comment · Hoonjichoi1 · 2026-07-12T00:18:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3565309110
- ID: review_comment:3565309110
- 파일: number-of-1-bits/hoonjichoi1.java, 줄: 17, 원래 줄: 17
- 답글 대상: review_comment:3564774416

````text
일부러 1이면 루프를 돌지 않게 base case를 추가한건데 없는게 더 효율적인 코드일까요?!
````

### review_comment · Hoonjichoi1 · 2026-07-12T00:18:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3565309992
- ID: review_comment:3565309992
- 파일: decode-ways/hoonjichoi1.java, 줄: 22, 원래 줄: 22
- 답글 대상: review_comment:3564767425

````text
아 그렇네요! 피드백 감사합니다!
````

### review_comment · parkhojeong · 2026-07-14T16:57:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2716#discussion_r3581027878
- ID: review_comment:3581027878
- 파일: number-of-1-bits/hoonjichoi1.java, 줄: 17, 원래 줄: 17
- 답글 대상: review_comment:3564774416

````text
1인 경우를 별도로 처리해서 얻는 이점보다 로직의 일관성을 가져가는게 더 좋다고 생각했습니다. modular 연산(%)의 결과를 더해주는 로직이기 때문에 따로 처리해야할 이유는 잘 모르곘습니다.
````

## [#2717 [essaysir] WEEK 03 solutions](https://github.com/DaleStudy/leetcode-study/pull/2717)

### issue_comment · DaleSeo · 2026-07-12T14:15:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#issuecomment-4951494223
- ID: issue_comment:4951494223

````text
@essaysir 님, `combination-sum/essaysir.java`에 줄바꿈이 누락되어서 CI가 실패하고 있습니다. 조치 부탁드려요.
````

### issue_comment · essaysir · 2026-07-13T00:17:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#issuecomment-4953369501
- ID: issue_comment:4953369501

````text
> @essaysir 님, `combination-sum/essaysir.java`에 줄바꿈이 누락되어서 CI가 실패하고 있습니다. 조치 부탁드려요.

조치 완료했습니다..
````

### review_comment · parkhojeong · 2026-07-14T16:41:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#discussion_r3580918199
- ID: review_comment:3580918199
- 파일: combination-sum/essaysir.java, 줄: 29, 원래 줄: 29

````text
removeLast() 사용하셔도 될 것 같습니다
````

### review_comment · parkhojeong · 2026-07-14T16:43:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#discussion_r3580930185
- ID: review_comment:3580930185
- 파일: number-of-1-bits/essaysir.java, 줄: 4, 원래 줄: 4

````text
bitCount로 바로 풀리긴 하는데 알고리즘 풀이 목적으로는 직접 구현해보시는게 좋을 것 같아요. 추가로 bitCount에 대한 내부 구현도 안 보셨다면 이해해보시면 좋을 것 같습니다.
````

### review_comment · parkhojeong · 2026-07-14T16:43:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#discussion_r3580934780
- ID: review_comment:3580934780
- 파일: valid-palindrome/essaysir.java, 줄: 11, 원래 줄: 11

````text
result 변수는 인라인 해도 될 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-14T16:48:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#discussion_r3580963696
- ID: review_comment:3580963696
- 파일: valid-palindrome/essaysir.java, 줄: 8, 원래 줄: 8

````text
StringBuilder를 쓰셨군요. 이 방식은 공간 복잡도 O(n) 을 필요로 하는데요. 별도의 공간을 사용하지 않고 투 포인터로도 풀어보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-14T16:49:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#discussion_r3580973865
- ID: review_comment:3580973865
- 파일: valid-palindrome/essaysir.java, 줄: 16, 원래 줄: 16

````text
변수명 x는 가독성이 안 좋아서 의미 있는 이름을 사용하시는게 좋을 거 같습니다. 
````

### review · parkhojeong · 2026-07-14T16:52:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2717#pullrequestreview-4696558795
- ID: review:4696558795
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 마이너한 커멘트 몇 개 남겼습니다.
````

## [#2718 [jinaSEO] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2718)

### review_comment · yuseok89 · 2026-07-10T11:15:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2718#discussion_r3558451588
- ID: review_comment:3558451588
- 파일: valid-palindrome/jinaSE0.ts, 줄: 1, 원래 줄: 1

````text
틀리지 않게 잘 푸신 것 같네요.
추가적인 공간(cleaned, reserved) 없이도 풀이가 가능한 문제니 참고하세요 ~
````

### review · yuseok89 · 2026-07-10T11:15:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2718#pullrequestreview-4670897529
- ID: review:4670897529
- 리뷰 상태: COMMENTED

````text
금요일이라,
일단 푸신 문제까지 리뷰해드렸습니다.
추가로 더 풀게 되시면 내일도 리뷰해드리겠습니다 !
````

### issue_comment · DaleSeo · 2026-07-12T14:16:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2718#issuecomment-4951496675
- ID: issue_comment:4951496675

````text
@DaleStudy 승인
````

## [#2719 [yuseok89] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2719)

### review_comment · alphaorderly · 2026-07-08T06:11:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3541609663
- ID: review_comment:3541609663
- 파일: valid-palindrome/yuseok89.py, 줄: 1, 원래 줄: 1

````text
해당 풀이는 Immutable 한 string을 하나 더 만들기 때문에 O(N)의 공간복잡도를 가질거에요!
[설명](https://0xffffffff.tistory.com/75)
regex없이 two pointer로 접근해보시는것도 좋은 경험이 되실겁니다.
````

### review_comment · alphaorderly · 2026-07-08T06:13:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3541616304
- ID: review_comment:3541616304
- 파일: number-of-1-bits/yuseok89.py, 줄: 1, 원래 줄: 1

````text
깔끔하게 잘 해결하신거 같아요!
````

### review_comment · alphaorderly · 2026-07-08T06:17:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3541645703
- ID: review_comment:3541645703
- 파일: maximum-subarray/yuseok89.py, 줄: 1, 원래 줄: 1

````text
아주 개인적인 의견으로는 

1. for loop안의 if-else 부분도 max로 한줄로 깔끔하게 정리하면 보기 좋을것 같아요!
2. sum과 ans를 nums[0]으로 설정하셨는데 for loop도 0번 index부터 시작하는건 중복 검사 같네요, 1번 index부터 검사하시는게 로직상 맞지 않을까 하는 생각이 듭니다.
````

### review_comment · alphaorderly · 2026-07-08T06:26:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3541685108
- ID: review_comment:3541685108
- 파일: combination-sum/yuseok89.py, 줄: 1, 원래 줄: 1

````text
다 좋으신데, 백트래킹 부분이 너무 복잡한거 같아요
별도의 함수로 제외하지 않고 구현하시면 훨씬 보기 좋게 될거 같아요
````

### review · alphaorderly · 2026-07-08T06:27:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#pullrequestreview-4651369185
- ID: review:4651369185
- 리뷰 상태: APPROVED

````text
깔끔하게 잘 해결하신것 같습니다!

````

### review_comment · yuseok89 · 2026-07-09T11:31:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3551243483
- ID: review_comment:3551243483
- 파일: combination-sum/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541685108

````text
백트래킹 코드를 좀 더 보기좋게 수정했습니다.
별도의 함수로 빼지 않고 구현은 어떤 방식을 말하시는걸까요?
````

### review_comment · yuseok89 · 2026-07-09T11:40:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3551294424
- ID: review_comment:3551294424
- 파일: maximum-subarray/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541645703

````text
1. 그렇네요. 의견 감사합니다
2. 이터레이터 방식이 아무래도 성능 면에서 나아서 그렇게 구현했네요. 처음 sum 값을 중복을 고려해 넣어두어서, 로직상 틀렸다고 하기에는 어려운 것 같아요. 그래도 덕분에 이터레이터 방식을 유지하면서도 1번 index 부터 확인하는 방법을 고민해 보았네요. 감사합니다.
````

### review_comment · yuseok89 · 2026-07-09T11:41:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3551298408
- ID: review_comment:3551298408
- 파일: valid-palindrome/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541609663

````text
네 맞네요. 일단 이 문제는 투포인터로 접근하는게 맞을 것 같습니다.
````

### review_comment · yuseok89 · 2026-07-11T12:52:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3564182612
- ID: review_comment:3564182612
- 파일: combination-sum/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541685108

````text
말씀하신 내용이 이해를 못했어서, 풀이하신 내용을 봤는데 DP 로 풀이된 것으로 보이는데요.
코드가 짧은 것은 맞는데, 시간복잡도나 공간복잡도에서 더 좋다고 보시는건가요?
````

### review_comment · alphaorderly · 2026-07-11T12:53:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3564184386
- ID: review_comment:3564184386
- 파일: maximum-subarray/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541645703

````text
맞습니다! 로직상 틀린건 절대절대 아니죠!
수정하신 코드 엄청 깔끔하시고 좋은거 같아요
````

### review_comment · alphaorderly · 2026-07-11T12:57:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3564188899
- ID: review_comment:3564188899
- 파일: combination-sum/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541685108

````text
제 코드 말씀하시는거라면 위에 주석으로 백트래킹 정답 있어요!

```
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []
        app = []

        def backtracking(last: int, left: int) -> None:
            if left == 0:
                ans.append(app[:])
                return

            for i in range(last, N):
                if candidates[i] > left:
                    continue

                app.append(candidates[i])
                backtracking(i, left - candidates[i])
                app.pop()

        backtracking(0, target)

        return ans
   ```

이건데 보시다시피 backtracking 함수를 class에 별도로 두지 않고 nested하게 뒀거든요

그래서 상대적으로 param 으로 전달되는 값이 적어지고 자연스럽게 가독성이 좋아지죠

아주 개인적으로 이걸 더 선호해서요, 사실 이게 맞다! 이건 아니죠
````

### review_comment · yuseok89 · 2026-07-11T14:14:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3564346441
- ID: review_comment:3564346441
- 파일: combination-sum/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541685108

````text
이렇게 쓸 수도 있네요.
함수 안에 함수를 선언하니, 내부 함수가 부모 함수의 `지역` 변수를 쓸 수 있네요.
문제 풀이에 이렇게 활용하는 것은 생각 못했는데, 다음 풀이에 활용해보겠습니다.
감사합니다.
````

### review_comment · alphaorderly · 2026-07-11T14:17:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2719#discussion_r3564351868
- ID: review_comment:3564351868
- 파일: combination-sum/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3541685108

````text
넵 맞습니다, 다만 immutable 한 변수를 내부 함수에서 쓰실때는 nonlocal등으로 미리 지정할 필요가 있습니다.
함수 내부에서 재선언이 되어버리거든요!
````

## [#2720 [Yiseull] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2720)

### review_comment · DaleSeo · 2026-07-09T00:09:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#discussion_r3548002585
- ID: review_comment:3548002585
- 파일: number-of-1-bits/Yiseull.java, 줄: None, 원래 줄: 3

````text
옷, 요런 풀이는 출제 의도와 맞지 않을지도? 면접관이 `Integer.bitCount`이 어떻게 동작하는 깊고 파고 들면 인터뷰가 말릴 수도 있고요. 코딩 테스트에서 표준 라이브러리를 사용하는 것은 양날의 검이 될 수 있으니 참고 바랍니다.
````

### review · DaleSeo · 2026-07-09T00:10:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#pullrequestreview-4658770325
- ID: review:4658770325
- 리뷰 상태: APPROVED

````text
수고하셨습니다! 아주 마이너한 피드백 드렸어용~
````

### review_comment · Yiseull · 2026-07-11T11:43:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#discussion_r3564066299
- ID: review_comment:3564066299
- 파일: number-of-1-bits/Yiseull.java, 줄: None, 원래 줄: 3
- 답글 대상: review_comment:3548002585

````text
말씀하신 대로 코딩테스트 준비 과정에서는 라이브러리 사용을 자제하고 직접 구현해서 푸는 게 맞는 것 같습니다. 
이 문제는 풀이를 알고 있어서 간단히 Integer.bitCount로 처리했는데, 앞으로는 내부 동작까지 설명할 수 있도록 직접 구현하는 방향으로 연습하겠습니다. 좋은 피드백 감사합니다! 🙏
````

### review_comment · parkhojeong · 2026-07-11T17:34:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#discussion_r3564707183
- ID: review_comment:3564707183
- 파일: maximum-subarray/Yiseull.java, 줄: 12, 원래 줄: 12

````text
tmp가 임시 변수로 의미 없는 값인 줄 알았는데 실제 로직에서는 의미가 있어서 적절한 네이밍 해주시면 더 좋을 거 같습니다!
````

### review · parkhojeong · 2026-07-11T17:38:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#pullrequestreview-4678448586
- ID: review:4678448586
- 리뷰 상태: APPROVED

````text
수고하셨습니다! 저도 마이너한 커멘트 하나 남겼습니다~
````

### review_comment · parkhojeong · 2026-07-11T17:52:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#discussion_r3564736022
- ID: review_comment:3564736022
- 파일: number-of-1-bits/Yiseull.java, 줄: None, 원래 줄: 3
- 답글 대상: review_comment:3548002585

````text
openjdk 구현체의 경우엔 2비트로 쪼개서 좌측 비트를 빼는 식으로 계산을 하네요. POPCNT 지원하는 cpu의 경우 JVM에서 체크해서 해당 명령어 사용하도록 최적화 하는 방식인 것 같습니다. 코드 링크도 첨부해드립니다~

https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/lang/Integer.java#L1594-L1614
```java
    public static int bitCount(int i) {
        // HD, Figure 5-2
        i = i - ((i >>> 1) & 0x55555555);
        i = (i & 0x33333333) + ((i >>> 2) & 0x33333333);
        i = (i + (i >>> 4)) & 0x0f0f0f0f;
        i = i + (i >>> 8);
        i = i + (i >>> 16);
        return i & 0x3f;
    }
```
````

### review_comment · Yiseull · 2026-07-12T03:14:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#discussion_r3565560692
- ID: review_comment:3565560692
- 파일: number-of-1-bits/Yiseull.java, 줄: None, 원래 줄: 3
- 답글 대상: review_comment:3548002585

````text
코드까지 찾아서 알려주셔서 내부 구현 코드까지 확인했네요 감사합니다!👍 한 번에 이해는 안돼서 클로드랑 같이 이해 해봐야겠네요 ㅎㅎ 
````

### review_comment · Yiseull · 2026-07-12T03:17:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2720#discussion_r3565563718
- ID: review_comment:3565563718
- 파일: maximum-subarray/Yiseull.java, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3564707183

````text
의미있는 네이밍 currentSum으로 변경했습니다! 피드백 감사합니다!
````

## [#2721 [DaleSeo] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2721)

### review_comment · parkhojeong · 2026-07-10T17:51:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2721#discussion_r3560943075
- ID: review_comment:3560943075
- 파일: number-of-1-bits/DaleSeo.rs, 줄: 12, 원래 줄: 12

````text
오 Brian Kernighan algorithm이라고도 불리는 방식이군요!

rust에선 count_ones()를 사용하면 cpu 의 popcount 가 지원되는 경우 명령어 사이클을 더 줄일 수도 있는 거 같네요 :)
````

### review · parkhojeong · 2026-07-10T17:51:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2721#pullrequestreview-4673777886
- ID: review:4673777886
- 리뷰 상태: APPROVED

````text
수고하셨습니다 :) 
````

## [#2722 [chapse57] Week 3](https://github.com/DaleStudy/leetcode-study/pull/2722)

### review · freemjstudio · 2026-07-11T09:40:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2722#pullrequestreview-4677405172
- ID: review:4677405172
- 리뷰 상태: COMMENTED

````text
엇 3주차 문제랑 예전 문제랑 섞인것 같습니다..! 
코드가 전반적으로 파이썬 함수들을 잘 활용하셔서 간결하네용! 

제가 지난 주차 문제도 merge해도 되는지 study 규칙을 몰라서 코멘트만 남기겠습니다,,, 고생하셨습니다 ! 
````

### review_comment · togo26 · 2026-07-11T16:19:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2722#discussion_r3564575417
- ID: review_comment:3564575417
- 파일: climbing-stairs/chapse57.py, 줄: 19, 원래 줄: 19

````text
공간복잡도 고려한 점은 좋습니다. 다만 변수명을 좀 더 구체적으로 작성해주시면 리뷰어 입장에서 검토하기 좋으니 고려해주시면 좋을 것 같습니다.

````

### review_comment · togo26 · 2026-07-11T16:26:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2722#discussion_r3564588251
- ID: review_comment:3564588251
- 파일: number-of-1-bits/chapse57.py, 줄: 7, 원래 줄: 7

````text
심플하게 풀어주셔서 좋네요. 내장 함수 기반으로 바이너리를 확인하는 방법 외에도 이진법 계산 방식이나 비트 연산 방식 등 다양한 방법으로 문제에 접근하시는 것도 추천합니다.
````

### review · togo26 · 2026-07-11T16:28:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2722#pullrequestreview-4678294089
- ID: review:4678294089
- 리뷰 상태: APPROVED

````text
PR에 언급하신 문제 위주로 검토하였습니다. 최적화 검토 관점에서 복잡도 계산도 추가해주시면 좋을 것 같습니다. 3주차 수고하셨습니다👍
````

## [#2723 [togo26] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2723)

### review_comment · dahyeong-yun · 2026-07-10T13:19:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3559207652
- ID: review_comment:3559207652
- 파일: maximum-subarray/togo26.js, 줄: 6, 원래 줄: 6

````text
시도한 코드까지 정리해 두는 꼼꼼함..! 저도 배워갑니다 👍🏼👍🏼 
````

### review_comment · dahyeong-yun · 2026-07-11T04:58:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3563238488
- ID: review_comment:3563238488
- 파일: combination-sum/togo26.js, 줄: 22, 원래 줄: 22

````text
정렬을 추가해서 연산 수를 줄이는 것도 좋은 아이디어네요 👍
````

### review_comment · dahyeong-yun · 2026-07-11T06:05:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3563381734
- ID: review_comment:3563381734
- 파일: combination-sum/togo26.js, 줄: 22, 원래 줄: 22

````text
애초에 정렬을 해서 불필요한 탐색을 줄이는 방법이 있네요 👍🏼
````

### review_comment · dahyeong-yun · 2026-07-11T06:08:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3563386248
- ID: review_comment:3563386248
- 파일: valid-palindrome/togo26.js, 줄: None, 원래 줄: 15

````text
풀이 자체랑은 연관이 적지만, `new`로 객체 생성을 하지 않아도 되는 것 같아요.
```suggestion
  const nonAlphanumeric = /[^a-zA-Z0-9]+/;
```
또 해당 정규식으로 한글자씩만 비교하기 때문에 끝의 `+`도 생략할 수 있네요.
```suggestion
  const nonAlphanumeric = /[^a-zA-Z0-9]/;
```
````

### review_comment · dahyeong-yun · 2026-07-11T06:22:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3563422587
- ID: review_comment:3563422587
- 파일: decode-ways/togo26.js, 줄: None, 원래 줄: 68

````text
아마 codeMap 은 숫자가 알파벳으로 치환되는 범위인지를 확인하는 것 같은데 이미 0으로 시작하지 않는지나, 26이하인지를 판별하고 있기 때문에 제거가 가능할 것 같아요.

```suggestion
    ways += go(start + 1);
    const twoDigits = firstDigit + secondDigit;
    if (Number(twoDigits) <= 26) {
      ways += go(start + 2);
    }
```
````

### review_comment · dahyeong-yun · 2026-07-11T06:27:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3563438672
- ID: review_comment:3563438672
- 파일: number-of-1-bits/togo26.js, 줄: 10, 원래 줄: 10

````text
덕분에 저도 자료형의 허용 범위 이상인 경우를 생각해봐야 한다는 걸 느꼈어요 👍🏼
````

### review · dahyeong-yun · 2026-07-11T06:36:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#pullrequestreview-4671799641
- ID: review:4671799641
- 리뷰 상태: APPROVED

````text
실패 케이스까지 꼼꼼하게 적어주셔서 저도 공부가 많이 되었습니다! 3주차도 고생하셨어요 :)
````

### review_comment · ICE0208 · 2026-07-11T11:57:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3564091451
- ID: review_comment:3564091451
- 파일: maximum-subarray/togo26.js, 줄: 1, 원래 줄: 1

````text
O(n³)부터 O(n²), O(n)까지 모든 풀이를 남겨주셔서 시간 복잡도가 개선되는 과정이 잘 보여 인상 깊었습니다!
````

### review_comment · togo26 · 2026-07-11T16:34:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3564602736
- ID: review_comment:3564602736
- 파일: valid-palindrome/togo26.js, 줄: None, 원래 줄: 15
- 답글 대상: review_comment:3563386248

````text
굳이 명시적으로 생성자를 쓸 필요가 없겠네요. 제안 반영하겠습니다 의견 감사합니다!
````

### review_comment · togo26 · 2026-07-11T16:37:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2723#discussion_r3564608168
- ID: review_comment:3564608168
- 파일: decode-ways/togo26.js, 줄: None, 원래 줄: 68
- 답글 대상: review_comment:3563422587

````text
확인 감사합니다 업데이트 반영하겠습니다!
````

## [#2724 [dahyeong-yun] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2724)

### review · seueooo · 2026-07-11T12:19:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2724#pullrequestreview-4677756585
- ID: review:4677756585
- 리뷰 상태: APPROVED

````text
설명이 자세히 적혀있어 이해하기 쉬웠습니다! 깔끔하고 최적화가 잘되어있는 것 같아요 잘보고갑니다👍
````

## [#2725 [seueooo] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2725)

### review_comment · parkhojeong · 2026-07-10T16:55:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560600472
- ID: review_comment:3560600472
- 파일: decode-ways/seueooo.js, 줄: 21, 원래 줄: 22

````text
dp로 풀어주셨군요! 주석이 코드랑 딱 맞아 떨어지는 느낌이 아니어서 읽으면서 조금 멈칫하게 되었던 거 같아요. 개인적으로는 지워도 괜찮을 거 같고, 적는다면 로직에 맞게 좀더 정리하면 좋을 거 같습니다~
````

### review_comment · parkhojeong · 2026-07-10T16:59:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560620847
- ID: review_comment:3560620847
- 파일: maximum-subarray/seueooo.js, 줄: None, 원래 줄: 16

````text
kadane 알고리즘이란걸 쓰신 거 같은데 혹시 어떤 방법인지 설명 부탁드려도 될까요?
````

### review_comment · parkhojeong · 2026-07-10T17:03:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560647366
- ID: review_comment:3560647366
- 파일: valid-palindrome/seueooo.js, 줄: None, 원래 줄: 17

````text
answer 변수는 없어도 될 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-10T17:10:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560690234
- ID: review_comment:3560690234
- 파일: validate-binary-search-tree/seueooo.js, 줄: 26, 원래 줄: 26

````text
inOrder 방식으로 풀어주셨군요! 전역변수 prev를 사용하고 있는데 순수 함수 형태로 풀어보셔도 좋을 거 같아요!
````

### review_comment · parkhojeong · 2026-07-10T17:16:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560722164
- ID: review_comment:3560722164
- 파일: combination-sum/seueooo.js, 줄: 9, 원래 줄: 9

````text
이 주석은 코드랑 안 맞는거 같아서 지워주셔도 좋을 거 같아요!
````

### review_comment · parkhojeong · 2026-07-10T17:18:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560732090
- ID: review_comment:3560732090
- 파일: 3sum/seueooo.js, 줄: 34, 원래 줄: 34

````text
꼼꼼하게 최적화 하셔서 풀어주셨네요 :)
````

### review_comment · parkhojeong · 2026-07-10T17:22:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3560758105
- ID: review_comment:3560758105
- 파일: number-of-1-bits/seueooo.js, 줄: 14, 원래 줄: 14

````text
사소한 부분이긴 한데 요런 스타일도 한 번 고려해보셔도 좋을 거 같습니다!
- python에는 `n // 2` 처럼 깔끔하게 표현이 되는데 js 는 비슷한 연산이 n >> 1 일 거 같네요. 한 번 고려해보셔도 좋을 거 같습니다 :)  
- count 부분은 n % 2 의 결과가 0, 1이어서 `count += n % 2`로 써볼 수도 있을 거 같습니다!

```suggestion
var hammingWeight = function (n) {
  let count = 0;
  while (n > 0) {
    count += n % 2;
    n >>=  1;
  }
  return count;
```
````

### review · parkhojeong · 2026-07-10T17:28:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#pullrequestreview-4673378732
- ID: review:4673378732
- 리뷰 상태: APPROVED

````text
수고하셨습니다~! 코드가 간결하고 풀이도 최적화가 많이 되어있어서 좋았습니다 :)
몇 가지 커멘트 남겨보았습니다.
````

### review_comment · JAEKWANG97 · 2026-07-10T22:36:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3562350601
- ID: review_comment:3562350601
- 파일: combination-sum/seueooo.js, 줄: 26, 원래 줄: 26

````text
`start`를 넘겨 중복 조합을 막고, 재귀 후 `pop()`으로 상태를 복구하는 흐름이 잘 읽혔습니다! 현재도 정답이지만 `candidates`를 먼저 정렬한 뒤 `sum + candidates[i] > target`일 때 `break`하면, 뒤의 더 큰 후보를 더 탐색하지 않아도 돼서 가지치기를 조금 더 일찍 할 수 있을 것 같아요.
````

### review_comment · JAEKWANG97 · 2026-07-10T22:36:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3562350638
- ID: review_comment:3562350638
- 파일: maximum-subarray/seueooo.js, 줄: None, 원래 줄: 16

````text
`dp[i]`가 현재 위치에서 끝나는 최대 연속합이라는 흐름이 명확해서 읽기 좋았습니다! 이 풀이에서는 직전 값과 전체 최댓값만 필요하므로, 배열 대신 두 변수만 사용하면 공간을 O(1)로 줄이고 마지막의 `Math.max(...dp)`도 피할 수 있을 것 같습니다.
````

### review · JAEKWANG97 · 2026-07-10T22:36:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#pullrequestreview-4675386300
- ID: review:4675386300
- 리뷰 상태: APPROVED

````text
전체적으로 잘 봤습니다! 각 풀이에서 사용한 패턴이 명확하고 코드도 간결했습니다. Combination Sum의 가지치기와 Maximum Subarray의 공간 사용 쪽에 개선 아이디어만 짧게 남겼습니다. 수고하셨습니다!
````

### review_comment · seueooo · 2026-07-11T11:22:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3564032181
- ID: review_comment:3564032181
- 파일: combination-sum/seueooo.js, 줄: 9, 원래 줄: 9
- 답글 대상: review_comment:3560722164

````text
요 부분은 코드랑은 관련 없고 시간복잡도 계산에서 T / M의 의미를 설명하려고 둔 주석이에요 !
````

### review_comment · seueooo · 2026-07-11T11:25:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3564038140
- ID: review_comment:3564038140
- 파일: decode-ways/seueooo.js, 줄: 21, 원래 줄: 22
- 답글 대상: review_comment:3560600472

````text
이부분 헷갈리게 적어놨네요 반영했습니다~!
````

### review_comment · seueooo · 2026-07-11T11:48:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3564074990
- ID: review_comment:3564074990
- 파일: maximum-subarray/seueooo.js, 줄: None, 원래 줄: 16
- 답글 대상: review_comment:3560620847

````text
오 처음 들어보는데 제가 구현한 방식이 kadane 알고리즘이군요..!
현재 값 nums[i]를 이전 연속합에 이어 붙일지, 아니면 nums[i]부터 새로 시작할지를 비교해서 최대 연속 부분합을 갱신하는 방식으로 구현했습니다 :)
````

### review_comment · seueooo · 2026-07-11T11:53:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3564083894
- ID: review_comment:3564083894
- 파일: number-of-1-bits/seueooo.js, 줄: 14, 원래 줄: 14
- 답글 대상: review_comment:3560758105

````text
시프트 연산자를 거의 사용해보지 않아서 잘 몰랐는데 좋은 정보 알아갑니다 :)
````

### review_comment · seueooo · 2026-07-11T12:03:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2725#discussion_r3564102461
- ID: review_comment:3564102461
- 파일: maximum-subarray/seueooo.js, 줄: None, 원래 줄: 16
- 답글 대상: review_comment:3562350638

````text
의견감사합니다:) 반영했습니다. 7b8764b4e32d631f8d610842006ef2a23d237a84
````

## [#2726 [jaekwang97] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2726)

### review_comment · parkhojeong · 2026-07-11T04:53:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#discussion_r3563232496
- ID: review_comment:3563232496
- 파일: valid-palindrome/jaekwang97.java, 줄: 26, 원래 줄: 26

````text
```suggestion
        int left = 0;
        int right = lower.length() - 1;

        while (left < right) {
            if (!Character.isLetterOrDigit(lower.charAt(left))) {
                left++;
                continue;
            }

            if (!Character.isLetterOrDigit(lower.charAt(right))) {
                right--;
                continue;
            }

            if (s.charAt(left).toLowerCase() != s.charAt(right).toLowerCase()) {
                return false;
            }

            left++;
            right--;
```

투 포인터로 풀어주셨네요 :) 

대소문자에 대한 판단 로직을 while 문 안으로 옮기면 s에 대한 수정 없이 주요 로직을 볼 수 있어 조금 더 명시적일 수도 있을 것 같습니다!
````

### review_comment · parkhojeong · 2026-07-11T05:05:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#discussion_r3563251890
- ID: review_comment:3563251890
- 파일: combination-sum/jaekwang97.java, 줄: 22, 원래 줄: 22

````text
사소하지만 요렇게 개선해보면 좋을 거 같습니다 :)
- 기능이 없어보이는 `answers.clear();` 제거
- `break -> return` 로 바꾸어 return 사용하는 일관성
- removeLast() 이용해서 append -> remove 흐름 쉽게 파악하도록 변경
```suggestion
    private final List<List<Integer>> answers = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        dfs(new ArrayList<>(), 0, 0, target, candidates);
        return answers;
    }
    private void dfs(List<Integer> list, int sum, int start, int target, int[] candidates) {
        if (sum == target) {
            answers.add(new ArrayList<>(list));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (sum + candidates[i] > target) return;
            list.add(candidates[i]);
            dfs(list, sum + candidates[i], i, target, candidates);
            list.removeLast();
        }
    }
}
```
````

### review_comment · parkhojeong · 2026-07-11T05:11:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#discussion_r3563261582
- ID: review_comment:3563261582
- 파일: decode-ways/jaekwang97.java, 줄: 14, 원래 줄: 14

````text
substring을 사용하면 가독성을 높일 수 있을 거 같습니다 :)
```suggestion
            int twoDigit = Integer.parseInt(s.substring(i - 2, i));
            if(twoDigit >= 10 && twoDigit <= 26){
                dp[i] += dp[i - 2];
            }
```
````

### review · parkhojeong · 2026-07-11T05:13:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#pullrequestreview-4676580489
- ID: review:4676580489
- 리뷰 상태: APPROVED

````text
수고하셨습니다 :) 전체적으로 간결한 풀이여서 좋았던 거 같습니다. 
몇 가지 커멘트 남겨보았습니다~
````

### review_comment · JAEKWANG97 · 2026-07-11T06:31:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#discussion_r3563448243
- ID: review_comment:3563448243
- 파일: valid-palindrome/jaekwang97.java, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:3563232496

````text
좋은 의견 감사합니다! 대소문자 변환을 비교하는 시점에 처리하면 별도의 문자열을 만들지 않고 로직을 볼 수 있다는 점 이해했습니다! Java에서는 Character toLowerCase 형태로 활용할 수 있을 것 같아요! 다음 풀이에서도 참고해보겠습니다!
````

### review_comment · JAEKWANG97 · 2026-07-11T06:31:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#discussion_r3563448282
- ID: review_comment:3563448282
- 파일: combination-sum/jaekwang97.java, 줄: 22, 원래 줄: 22
- 답글 대상: review_comment:3563251890

````text
좋은 의견 감사합니다! removeLast를 사용하면 값을 추가하고 다시 제거하는 백트래킹 흐름이 더 잘 보일 것 같아요! clear와 break 부분도 LeetCode의 호출 방식과 코드 흐름을 기준으로 다시 비교해보겠습니다! 꼼꼼하게 봐주셔서 감사합니다!
````

### review_comment · JAEKWANG97 · 2026-07-11T06:32:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2726#discussion_r3563448333
- ID: review_comment:3563448333
- 파일: decode-ways/jaekwang97.java, 줄: 14, 원래 줄: 14
- 답글 대상: review_comment:3563261582

````text
좋은 의견 감사합니다! substring을 사용하면 두 자리 숫자를 확인하는 의도가 코드에서 바로 드러나서 더 읽기 쉬울 것 같아요! 문자 연산 방식과 비교해보면서 가독성 측면에서도 참고하겠습니다!
````

## [#2727 [parkhojeong] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2727)

### review_comment · JAEKWANG97 · 2026-07-11T00:24:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2727#discussion_r3562665285
- ID: review_comment:3562665285
- 파일: decode-ways/parkhojeong.py, 줄: 24, 원래 줄: 24

````text
0이 들어가는 경우를 먼저 나누고 문자열을 구간별로 분리해서 경우의 수를 계산하신 흐름을 잘 봤습니다! 제가 생각한 DP 방식과 달라서 이런 식으로도 풀 수 있다는 걸 배웠어요!
````

### review_comment · JAEKWANG97 · 2026-07-11T00:24:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2727#discussion_r3562665318
- ID: review_comment:3562665318
- 파일: maximum-subarray/parkhojeong.py, 줄: 42, 원래 줄: 42

````text
연속된 양수와 음수를 먼저 묶은 다음 양쪽 구간을 합쳐가며 최댓값을 찾으셨네요! 제가 풀었던 점화식 방식과 달라서 코드를 따라가며 비교해볼 수 있었습니다!
````

### review · JAEKWANG97 · 2026-07-11T00:24:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2727#pullrequestreview-4675787959
- ID: review:4675787959
- 리뷰 상태: APPROVED

````text
전체적으로 잘 봤습니다! 문제마다 풀이 흐름이 잘 드러나서 코드를 따라가기 좋았습니다! 특히 Decode Ways와 Maximum Subarray는 제가 풀었던 방식과 달라서 다른 접근을 배울 수 있었습니다! 수고하셨습니다!
````

### review_comment · parkhojeong · 2026-07-11T05:25:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2727#discussion_r3563283958
- ID: review_comment:3563283958
- 파일: decode-ways/parkhojeong.py, 줄: 24, 원래 줄: 24
- 답글 대상: review_comment:3562665285

````text
조건 중에 0이 중요한 부분이더라구요. 0을 기준으로 입력 값을 쪼개준 뒤, 각 경우의 수를 구해 곱해주도록 해보았습니다 :)
dp 방식은 생각 못헀는데 풀어주신 거 보고 배울 수 있었습니다!
````

### review_comment · parkhojeong · 2026-07-11T10:10:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2727#discussion_r3563926614
- ID: review_comment:3563926614
- 파일: maximum-subarray/parkhojeong.py, 줄: 42, 원래 줄: 42
- 답글 대상: review_comment:3562665318

````text
연속된 합에 대한 문제라 + - + - + - ... 형태로 데이터를 정리를 먼저 해봤어요. 이후 최대값을 그리디 방식으로 구하는 걸로 해결해봤습니다 :)
````

## [#2728 [Chanz] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2728)

### issue_comment · Chanz82 · 2026-07-11T00:33:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#issuecomment-4940772544
- ID: issue_comment:4940772544

````text
easy 2, medium 1 개 문제의 벽을 계속 넘지 못하고 있네요..ㅠㅠ 다음주 분발해보겠습니다..흑.
````

### review_comment · xeulbn · 2026-07-11T02:49:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3562974440
- ID: review_comment:3562974440
- 파일: combination-sum/Chanz82.py, 줄: 3, 원래 줄: 3

````text
combination은 외부 함수의 지역 변수로 이미 선언되어 있어 내부 함수의 매개변수로 다시 전달하지 않아도 될 것 같습니다. 내부 함수가 클로저로 직접 참조하도록 변경하면 함수 인자를 줄이고 코드의 의도를 조금 더 명확하게 표현할 수 있습니다.

또한 target은 최초 목표값이 아니라 재귀 호출마다 남은 값을 의미하므로 remain과 같은 이름을 사용하면 가독성이 더 좋아질 것 같습니다.
````

### review_comment · xeulbn · 2026-07-11T02:51:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3562978720
- ID: review_comment:3562978720
- 파일: valid-palindrome/Chanz82.py, 줄: 9, 원래 줄: 9

````text
Python의 문자열은 불변 객체이기 때문에 반복문 안에서 alpha_num_str += ch.lower()를 수행하면 매번 새로운 문자열이 생성되는 것으로 알고있습니다. (제 주 언어가 자바라 정확하지 않습니다! ) 입력 크기가 커질 경우 불필요한 문자열 복사가 발생할 수 있으므로 리스트에 append()한 뒤 join()하거나, 투 포인터를 이용해 원본 문자열에서 바로 비교하는 방식이 더 적절할 수 있을 것 같습니다.
````

### review · xeulbn · 2026-07-11T02:52:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#pullrequestreview-4676267075
- ID: review:4676267075
- 리뷰 상태: APPROVED

````text
전체적으로 코드 잘 읽어보았습니다. 
제가 주 언어가 자바인지라 오랜만에 파이썬 코드를 읽어보니 즐거웠습니다.
이번 주도 고생하셨습니다!
````

### review_comment · parkhojeong · 2026-07-11T16:51:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3564634951
- ID: review_comment:3564634951
- 파일: valid-palindrome/Chanz82.py, 줄: 9, 원래 줄: 9
- 답글 대상: review_comment:3562978720

````text
3.13 기준으로 새로 생성하는 방식으로 동작하네요. 저도 몰랐던 내용인데 덕분에 알아갑니다!

구현체 코드는 이거 참고하시면 될 거 같습니다.
- str.lower() (https://github.com/python/cpython/blob/3.13/Objects/unicodeobject.c#L12129-L12142)
- ASCII 소문자 결과 할당 (https://github.com/python/cpython/blob/3.13/Objects/unicodeobject.c#L9572-L9589)
- PyUnicode_New (https://github.com/python/cpython/blob/3.13/Objects/unicodeobject.c#L1343-L1414)
````

### review_comment · parkhojeong · 2026-07-11T17:00:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3564652575
- ID: review_comment:3564652575
- 파일: valid-palindrome/Chanz82.py, 줄: 19, 원래 줄: 19

````text
포문 안에서 end_idx가 따로 관리되는 부분에서 코드 따라가기가 약간 어려웠던 거 같습니다.

루프 돌릴지는 while 조건문에서 처리해주고 주요 로직만 본문에서 처리하는 형태도 고려해보시면 좋을 거 같습니다!
```suggestion
        left_idx = 0
        right_idx = len(alpha_num_str) - 1
        while left_idx < right_idx:
            if alpha_num_str[left_idx] != alpha_num_str[right_idx]:
                return False
            
            left_idx += 1
            right_idx -= 1
        
        return True
```
````

### review_comment · parkhojeong · 2026-07-11T17:08:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3564665160
- ID: review_comment:3564665160
- 파일: combination-sum/Chanz82.py, 줄: 20, 원래 줄: 20

````text
요거 돌려보니까 성능이 좋지는 않아서 좀 더 최적화 해보셔도 좋을 것 같습니다!
다른 풀이 참고하셔도 될 거 같아요
https://github.com/DaleStudy/leetcode-study/tree/main/combination-sum
````

### review_comment · parkhojeong · 2026-07-11T17:11:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3564670979
- ID: review_comment:3564670979
- 파일: number-of-1-bits/Chanz82.py, 줄: 10, 원래 줄: 10

````text
깔끔하게 풀어주신 거 같습니다! `n % 2`를 바로 더하는 방식도 고려해보셔도 좋을 거 같습니다 :)

```suggestion
        bit_count = 0
        while n > 0:
            bit_count += n % 2
            n //= 2
```
````

### review · parkhojeong · 2026-07-11T17:12:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#pullrequestreview-4678392580
- ID: review:4678392580
- 리뷰 상태: APPROVED

````text
수고하셨습니다! 몇 가지 커멘트 남겨보았습니다~
````

### review_comment · Chanz82 · 2026-07-12T15:05:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3566543129
- ID: review_comment:3566543129
- 파일: combination-sum/Chanz82.py, 줄: 3, 원래 줄: 3
- 답글 대상: review_comment:3562974440

````text
candidates는 그렇게 처리했는데. combination은 그렇게 처리를 못했네요. 세심한 리뷰 감사합니다..! 
````

### review_comment · Chanz82 · 2026-07-12T15:06:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2728#discussion_r3566545738
- ID: review_comment:3566545738
- 파일: number-of-1-bits/Chanz82.py, 줄: 10, 원래 줄: 10
- 답글 대상: review_comment:3564670979

````text
아하 0이면 의미가 없으니 더해도 되네요..! 감사합니다!
````

## [#2729 [xeulbn] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2729)

### review_comment · sonshn · 2026-07-11T03:33:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#discussion_r3563052875
- ID: review_comment:3563052875
- 파일: number-of-1-bits/xeulbn.java, 줄: 17, 원래 줄: 17

````text
비트 연산을 활용해서 해결하셨군요! 찾아보니 이런 것을 Hamming이라고 하는 것 같네요
````

### review_comment · sonshn · 2026-07-11T03:34:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#discussion_r3563054501
- ID: review_comment:3563054501
- 파일: valid-palindrome/xeulbn.java, 줄: 32, 원래 줄: 32

````text
저도 정확히 똑같이 풀었습니다! 사실 배열을 활용할까 했었는데, 투 포인터를 사용하는 것이 문제 의도랑 맞는 것 같네요
````

### review_comment · sonshn · 2026-07-11T03:35:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#discussion_r3563055829
- ID: review_comment:3563055829
- 파일: combination-sum/xeulbn.java, 줄: 30, 원래 줄: 30

````text
백트래킹으로 해결하셨군요...! 많이 배워갑니다 😊
````

### review · sonshn · 2026-07-11T03:37:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#pullrequestreview-4676359730
- ID: review:4676359730
- 리뷰 상태: APPROVED

````text
시간 복잡도나 공간 복잡도도 고려하셔서 최적의 방법으로 풀이하셨네요! 저도 Java로 준비하고 있는데, 덕분에 많이 배워갑니다. 이번 주도 고생많으셨어요!
````

### review_comment · parkhojeong · 2026-07-11T16:29:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#discussion_r3564594042
- ID: review_comment:3564594042
- 파일: maximum-subarray/xeulbn.java, 줄: None, 원래 줄: 23

````text
currentStart, maxStart, maxEnd 는 사용 안되는 변수라 지워주시면 좋을 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-11T16:30:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#discussion_r3564595515
- ID: review_comment:3564595515
- 파일: combination-sum/xeulbn.java, 줄: 28, 원래 줄: 28

````text
removeLast를 사용하시면 add -> remove 흐름을 좀더 직관적으로 나타낼 수 있을 거 것 같네요!

```suggestion
        for (int i=start; i<candidates.length; i++) {
            int candidate = candidates[i];

            current.add(candidate);
            backtrack(candidates, remain - candidate, i, current, result);
            current.removeLast();
        }
```
````

### review_comment · parkhojeong · 2026-07-11T16:31:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#discussion_r3564597778
- ID: review_comment:3564597778
- 파일: decode-ways/xeulbn.java, 줄: 20, 원래 줄: 20

````text
substring 을 사용하면 좀 더 직관적일 수 있을 거 같아서 고려해보시면 좋을 거 같습니다 !
```suggestion
            int twoDigit = Integer.parseInt(s.substring(i - 2, i));
```
````

### review · parkhojeong · 2026-07-11T16:35:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2729#pullrequestreview-4678318494
- ID: review:4678318494
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다. 간결하게 잘 풀어주신 거 같습니다!

커멘트 남겨보았습니다. maximum-subarray에 안쓰는 변수가 있어서 지우고 머지하면 좋을 거 같아 request changed 남겨놓습니다~
````

## [#2730 [sonshn] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2730)

### review_comment · freemjstudio · 2026-07-11T09:46:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2730#discussion_r3563883516
- ID: review_comment:3563883516
- 파일: valid-palindrome/sonshn.java, 줄: 10, 원래 줄: 10

````text
저는 문자열을 파싱하고나서 유효성 검사하는 방법이었는데, 파싱과 유효성을 동시에 검사하면 공간복잡도를 좀 더 줄일 수 있는 것 같아 보여서 좋아보입니다 !! 
````

### review · freemjstudio · 2026-07-11T09:46:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2730#pullrequestreview-4677420371
- ID: review:4677420371
- 리뷰 상태: APPROVED

````text
고생하셨습니다~~
````

### review · JinuCheon · 2026-07-11T13:43:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2730#pullrequestreview-4677905083
- ID: review:4677905083
- 리뷰 상태: COMMENTED

````text
👍 수고하셨습니다
````

## [#2731 [JinuCheon] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2731)

### review · sangbeenmoon · 2026-07-11T05:24:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2731#pullrequestreview-4676643636
- ID: review:4676643636
- 리뷰 상태: APPROVED

````text
두가지 이상의 풀이 방법을 올려주신 점이 인상적이네요! 👍 
고생하셨습니다
````

## [#2732 [sangbeenmoon] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2732)

### review_comment · freemjstudio · 2026-07-11T09:38:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2732#discussion_r3563869535
- ID: review_comment:3563869535
- 파일: decode-ways/sangbeenmoon.py, 줄: 52, 원래 줄: 52

````text
s[i] 가 0 인 경우에는 두자리수 인 경우 s[i-1:i+1] 이 알파벳 범위안에 들어가는지 검사하는 것도 직관적이어서 좋지만 
s[i] != "0" 인 경우와 두자리수인 경우만 따지게 되면 더 코드가 간결해질 수 있을 것 같습니다 
````

### review · freemjstudio · 2026-07-11T09:38:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2732#pullrequestreview-4677399157
- ID: review:4677399157
- 리뷰 상태: APPROVED

````text
고생하셨습니다 🥇 
````

## [#2734 [freemjstudio] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2734)

### review_comment · jthw1005 · 2026-07-11T14:08:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2734#discussion_r3564335201
- ID: review_comment:3564335201
- 파일: combination-sum/freemjstudio.py, 줄: 1, 원래 줄: 1

````text
생각도 안 하고 바로 DP로 풀었는데, 백트래킹 방식이 정배인거 같네요! 👍
````

### review_comment · jthw1005 · 2026-07-11T14:12:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2734#discussion_r3564343213
- ID: review_comment:3564343213
- 파일: number-of-1-bits/freemjstudio.py, 줄: 4, 원래 줄: 4

````text
Hamming Weight이 뭘까하고 찾아봤는데, 상황에 딱 맞는 네이밍이네요.
하나 또 배워갑니다! 🙏
````

### review_comment · jthw1005 · 2026-07-11T14:21:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2734#discussion_r3564359109
- ID: review_comment:3564359109
- 파일: valid-palindrome/freemjstudio.py, 줄: 8, 원래 줄: 8

````text
문제 조건에서 s가 ascii로 제한되어 있으니 isalnum()을 쓰는 것도 괜찮을 것 같아 보이네요!
````

### review · jthw1005 · 2026-07-11T14:21:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2734#pullrequestreview-4677991243
- ID: review:4677991243
- 리뷰 상태: APPROVED

````text
이번주도 고생하셨습니다! 다음주도 화이팅입니다! 🔥
````

### review_comment · freemjstudio · 2026-07-11T14:43:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2734#discussion_r3564396038
- ID: review_comment:3564396038
- 파일: valid-palindrome/freemjstudio.py, 줄: 8, 원래 줄: 8
- 답글 대상: review_comment:3564359109

````text
오 그런 함수가 있군요 감사합니다!!
````

### review_comment · freemjstudio · 2026-07-11T14:43:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2734#discussion_r3564397184
- ID: review_comment:3564397184
- 파일: combination-sum/freemjstudio.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3564335201

````text
오 dp 로도 풀수있군용..
````

## [#2735 [jthw1005] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2735)

### review_comment · j2h30728 · 2026-07-11T15:01:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2735#discussion_r3564429864
- ID: review_comment:3564429864
- 파일: valid-palindrome/jthw1005.js, 줄: 2, 원래 줄: 2

````text
오 정규식 쓸 생각을 못했었는데 덕분에 깨닫고 갑니다!
````

## [#2736 [j2h30728] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2736)

### review · alphaorderly · 2026-07-11T15:15:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#pullrequestreview-4678139133
- ID: review:4678139133
- 리뷰 상태: APPROVED

````text
전반적으로 깔끔하게 잘 해결하신것 같습니다!
````

### review_comment · parkhojeong · 2026-07-11T16:12:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#discussion_r3564562636
- ID: review_comment:3564562636
- 파일: number-of-1-bits/j2h30728.ts, 줄: None, 원래 줄: 9

````text
abs 없이 `sum += n % 2;` 만 해줘도 될 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-11T16:22:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#discussion_r3564582045
- ID: review_comment:3564582045
- 파일: valid-palindrome/j2h30728.ts, 줄: 11, 원래 줄: 11

````text
조건이 alphanumeric 인데 알파벳만 처리해서 테스트 통과가 안되네요! 다시 풀어주셔야 할 거 같아요~
````

### review · parkhojeong · 2026-07-11T16:25:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#pullrequestreview-4678281251
- ID: review:4678281251
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다! 전체적으로 깔끔하게 잘 풀어주신 거 같네요.

valid-palindrome 은 통과가 안되는 상태라 request-changed 로 남겨두었습니다!
````

### issue_comment · DaleSeo · 2026-07-14T21:02:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#issuecomment-4973963128
- ID: issue_comment:4973963128

````text
@j2h30728 답안 PR이 병합될 수 있도록 피드백 반영 좀 부탁드리겠습니다.
````

### review_comment · j2h30728 · 2026-07-15T00:37:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#discussion_r3583629041
- ID: review_comment:3583629041
- 파일: valid-palindrome/j2h30728.ts, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3564582045

````text
헛! 잡아주셔서 정말 갑사합니다. @parkhojeong 
````

### review_comment · j2h30728 · 2026-07-15T00:38:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2736#discussion_r3583630210
- ID: review_comment:3583630210
- 파일: number-of-1-bits/j2h30728.ts, 줄: None, 원래 줄: 9
- 답글 대상: review_comment:3564562636

````text
감사합니다!
````

## [#2737 [alphaorderly] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2737)

### review_comment · SamTheKorean · 2026-07-17T00:25:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2737#discussion_r3599597158
- ID: review_comment:3599597158
- 파일: coin-change/alphaorderly.py, 줄: 5, 원래 줄: 5

````text
오 한문제를 이렇게 여러가지 방법으로 푸셨군요! 덕분에 배워갑니다 ㅎㅎ
````

### review · yuseok89 · 2026-07-17T00:36:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2737#pullrequestreview-4718526664
- ID: review:4718526664
- 리뷰 상태: APPROVED

````text
한문제에 대해서 다양하게 풀이하시고, 고민도 많이 하시는 것 같아 많이 배웁니다.
4주차 고생하셨습니다
````

### review_comment · parkhojeong · 2026-07-17T18:19:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2737#discussion_r3605274179
- ID: review_comment:3605274179
- 파일: word-search/alphaorderly.py, 줄: 99, 원래 줄: 99

````text
저도 여러 방식으로 풀어보고 최적화 해봤는데 최종적으로 이 로직을 추가하니 0ms에 근접한 결과가 나오네요.

풀어주신 것도 돌려보니 이 로직 여부에 따라 성능이 5ms / 500ms로 확연히 차이 나는데요. 
현재 리트코드 테스트 케이스에 보드 인풋이 "AAAAAAAAAAAAA...AAAB" 과 같은 테스트 케이스가 있어서 그런 거 같습니다. 
이 로직만으로 다양한 인풋 패턴을 커버는 어려울 거 같지만 이런 식으로 인풋 값의 패턴을 파악해서 최적화는게 중요한 포인트인 것 같네요. 좋은 아이디어인 것 같습니다!
````

### review_comment · okyungjin · 2026-07-19T03:24:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2737#discussion_r3609702340
- ID: review_comment:3609702340
- 파일: word-search/alphaorderly.py, 줄: 99, 원래 줄: 99
- 답글 대상: review_comment:3605274179

````text
@parkhojeong Submit 할 때 검증하는 테스트케이스도 볼 수 있나요?
````

### issue_comment · okyungjin · 2026-07-19T03:28:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2737#issuecomment-5013998372
- ID: issue_comment:5013998372

````text
풀이가 다양하고 최적화가 잘 되어 있어서 배울 점이 많네요🔥 감사합니다~!
````

## [#2738 [daehyun99] WEEK 03 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2738)

### review_comment · parkhojeong · 2026-07-12T12:32:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3566300851
- ID: review_comment:3566300851
- 파일: maximum-subarray/daehyun99.py, 줄: 20, 원래 줄: 20

````text
요거 실제로 돌려보니 성능이 좋지는 않아서 최적화 시도해보셔도 좋을 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-12T12:34:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3566304298
- ID: review_comment:3566304298
- 파일: decode-ways/daehyun99.py, 줄: 1, 원래 줄: 1

````text
코드가 상당히 직관적이어서 좋네요.
````

### review_comment · parkhojeong · 2026-07-12T12:42:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3566315725
- ID: review_comment:3566315725
- 파일: combination-sum/daehyun99.py, 줄: 19, 원래 줄: 19

````text
`values[:] + [candidate]` 사용하면 temp 없이 간단하게 표현이 가능할 거 같습니다.
```suggestion
                if sum_values + candidate <= target:
                    que.append(values[:] + [candidate])
```
````

### review_comment · parkhojeong · 2026-07-12T12:42:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3566316520
- ID: review_comment:3566316520
- 파일: combination-sum/daehyun99.py, 줄: 1, 원래 줄: 1

````text
ai 리뷰에서 처럼 큐에 조합들이 쌓이는 경우를 고려해서 최적화 해보셔도 좋을 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-12T12:45:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3566320886
- ID: review_comment:3566320886
- 파일: valid-palindrome/daehyun99.py, 줄: 10, 원래 줄: 10

````text
string은 예약어여서 다른 변수명을 사용하는게 좋을 거 같고 ord 보다는 isalnum이나 명시적으로 조건을 나타내는 방식으로 표현해주면 좋을 거 같습니다!
```suggestion
        for ch in s:
            if ch.isalnum():
                forward += string
        backward = forward[::-1]
```
````

### review · parkhojeong · 2026-07-12T12:45:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#pullrequestreview-4680042467
- ID: review:4680042467
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 몇 가지 커멘트 남겼습니다.
````

### issue_comment · DaleSeo · 2026-07-12T14:22:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#issuecomment-4951517349
- ID: issue_comment:4951517349

````text
@daehyun99 님, 다음 답안 제출부터 주차 설정이 누락되지 않도록 부탁드리겠습니다.

<img width="1780" height="856" alt="2026-07-12 at 10 22 42" src="https://github.com/user-attachments/assets/a644d49e-709e-4c5a-8130-83c293589858" />

````

### issue_comment · daehyun99 · 2026-07-13T02:48:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#issuecomment-4953977501
- ID: issue_comment:4953977501

````text
> @daehyun99 님, 다음 답안 제출부터 주차 설정이 누락되지 않도록 부탁드리겠습니다.

앗 넵 죄송합니다.. 헷갈렸었습니다.
````

### review_comment · daehyun99 · 2026-07-13T04:20:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3568022772
- ID: review_comment:3568022772
- 파일: maximum-subarray/daehyun99.py, 줄: 20, 원래 줄: 20
- 답글 대상: review_comment:3566300851

````text
루프를 1번으로 줄이고, `max(nums)`도 줄이니 성능이 꽤 많이 좋아지네요! 조언 감사합니다!!

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)
        if result <= 0:
            return result

        val = 0
        for i in range(len(nums)):
            val += nums[i]
            if val < 0:
                val = 0
            result = max(result, val)
        return result
```
````

### review_comment · daehyun99 · 2026-07-13T04:25:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3568035869
- ID: review_comment:3568035869
- 파일: decode-ways/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3566304298

````text
2주차에 #230 문제가 생각나서, 접근법을 적용해서 풀어보았습니다.
````

### review_comment · parkhojeong · 2026-07-14T17:13:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3581136065
- ID: review_comment:3581136065
- 파일: maximum-subarray/daehyun99.py, 줄: 20, 원래 줄: 20
- 답글 대상: review_comment:3566300851

````text
처음 `result <= 0` 처리 부분이 "제일 큰 값이 음수 또는 0인 경우는 더 할게 없다"로 이해됐는데 이게 어떻게 문제를 풀지 복선처럼 느껴지는 거 같아요. 이후 포문에선 음수가 나오면 리셋해주고, 더해질 수 있는 케이스는 계속 더해본다는게 쉽게 이해됐습니다. 
공유 감사합니다.
````

### review_comment · parkhojeong · 2026-07-14T17:25:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3581221473
- ID: review_comment:3581221473
- 파일: decode-ways/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3566304298

````text
저도 #230 생각은 이렇게 풀 생각은 못했네요. 대단하십니다!

저는 0을 먼저 전처리해서 0이 없는 여러 인풋으로 쪼개고 divide & conquer 접근으로 풀어봤는데 참고차 남겨드립니다.
https://github.com/DaleStudy/leetcode-study/blob/main/decode-ways/parkhojeong.py
````

### review_comment · daehyun99 · 2026-07-15T05:30:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2738#discussion_r3584694274
- ID: review_comment:3584694274
- 파일: decode-ways/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3566304298

````text
풀이 공유 감사드립니다!
파이썬에서 `if s[i - 1] + s[i] >= "27":`처럼 문자열 간의 비교가 되는 것을 처음 알았네요.
````

## [#2739 [yuseok89] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2739)

### review_comment · alphaorderly · 2026-07-12T21:35:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3567169496
- ID: review_comment:3567169496
- 파일: merge-two-sorted-lists/yuseok89.py, 줄: 1, 원래 줄: 1

````text
이거 2개 비교하는 부분 끝나고 리스트 두개중에 한개 순회 다 끝난 상태에서는 나머지 남은 리스트는 그냥 뒤에 통째로 붙혀주는게 더 좋더라구요!
그니까 while 말구 단일 if문으로 처리가 가능해서 이게 훨씬 깔끔하고 좋은것 같았어요
파이썬의 or가 어떻게 단축평가를 하는지 고려하면 더욱 줄일수도 있구요!
````

### review_comment · yuseok89 · 2026-07-15T13:29:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3587645658
- ID: review_comment:3587645658
- 파일: merge-two-sorted-lists/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3567169496

````text
의견 감사합니다.
굳이 더 순회 할 필요 없었네요.
파이썬 or 도 좀 더 살펴보겠습니다.
````

### review_comment · alphaorderly · 2026-07-15T13:56:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3587859023
- ID: review_comment:3587859023
- 파일: coin-change/yuseok89.py, 줄: 1, 원래 줄: 1

````text
저는 코인이 양수값만 있어서 DP만 했었는데 BFS로 해도 충분히 가능하겠네요!
````

### review_comment · alphaorderly · 2026-07-15T13:59:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3587882154
- ID: review_comment:3587882154
- 파일: find-minimum-in-rotated-sorted-array/yuseok89.py, 줄: 1, 원래 줄: 1

````text
저는 while loop 안에 복잡한 연산 들어가는거 별로라 최대한 간단하게 했는데, 이렇게 하시면 얼리 리턴이 가능해서 좋네요!
````

### review_comment · alphaorderly · 2026-07-15T14:02:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3587909120
- ID: review_comment:3587909120
- 파일: word-search/yuseok89.py, 줄: 1, 원래 줄: 1

````text
이거 회원님 답안은 3000ms 가량 걸리는데
백트래킹을 유지한 상태에서 

1. 어차피 답이 안되는것 미리 쳐내기
2. 좀 더 효율적으로 탐색하기

이 두가지만 추가해도 leetcode 실행속도상 0ms까지 도달할수 있어요!
꽤나 흥미롭더라구요, 저는 하나하나 직접 추가해가면서 성능 튜닝 했었네요
````

### review_comment · alphaorderly · 2026-07-15T14:03:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3587915326
- ID: review_comment:3587915326
- 파일: word-search/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3587909120

````text
<img width="591" height="359" alt="Image" src="https://github.com/user-attachments/assets/dc15c84f-0d7b-4fb7-aa92-379b5d0e02bf" />
````

### review_comment · alphaorderly · 2026-07-15T14:04:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3587923794
- ID: review_comment:3587923794
- 파일: maximum-depth-of-binary-tree/yuseok89.py, 줄: 1, 원래 줄: 1

````text
아주 개인적인 생각인데, rec을 쓰지 않고 maxDepth 자체를 재귀로 하면 좀 코드가 간단해지지 않을까요?

````

### review_comment · alphaorderly · 2026-07-16T10:02:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3594457283
- ID: review_comment:3594457283
- 파일: word-search/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3587909120

````text
백트래킹에서 탐색공간을 프루닝하는건 좋은 공부가 될것 같습니다!
````

### review_comment · yuseok89 · 2026-07-17T00:33:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3599626058
- ID: review_comment:3599626058
- 파일: word-search/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3587909120

````text
리뷰 감사합니다.
미리 쳐내기는 바로 반영되어도 좋을 것 같아요.
효율적으로 탐색하는 것은 작성하신 코드를 보니 뒤집어서 탐색하는 것을 말씀하시는 것 같은데,
뒤집는 쪽이 느려지는 경우도 만들어지긴 해서, 어느 경우에나 효율적이라고 보기는 어려운 것 같았어요.
이 문제 테스트셋에는 정말 잘 맞는 것 같습니다.
````

### review_comment · alphaorderly · 2026-07-17T00:46:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3599672560
- ID: review_comment:3599672560
- 파일: word-search/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3587909120

````text
맞습니다! 빈도 기반으로 뒤집었는데, 해당 문제를 어떻게 하면 조금이라도 빨리 풀수 있을까에만 초점을 맞춘 코드이긴 합니다!
````

### review_comment · yuseok89 · 2026-07-17T00:54:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3599698777
- ID: review_comment:3599698777
- 파일: maximum-depth-of-binary-tree/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3587923794

````text
그러네요. 문제 풀 당시에는 바로 생각을 못했었네요.
리뷰 감사합니다.
````

### review_comment · parkhojeong · 2026-07-17T14:36:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3603950970
- ID: review_comment:3603950970
- 파일: find-minimum-in-rotated-sorted-array/yuseok89.py, 줄: 18, 원래 줄: 18

````text
low는 mid + 1 부터 시작해도 될 거 같습니다
```suggestion
            else:
                low = mid + 1

```
````

### review_comment · parkhojeong · 2026-07-17T14:37:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3603960913
- ID: review_comment:3603960913
- 파일: merge-two-sorted-lists/yuseok89.py, 줄: 12, 원래 줄: 12

````text
ret은 무슨 약자일까요?
````

### review_comment · parkhojeong · 2026-07-17T14:45:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3604008895
- ID: review_comment:3604008895
- 파일: word-search/yuseok89.py, 줄: 14, 원래 줄: 14

````text
빈도 이용해서 최적화하신 거 좋은 거 같습니다. 이걸 rec 함수에서도 사용하면 좀 더 최적화가 가능할 거 같네요.
````

### review_comment · parkhojeong · 2026-07-17T14:46:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3604015250
- ID: review_comment:3604015250
- 파일: word-search/yuseok89.py, 줄: 27, 원래 줄: 27

````text
None으로 할당했다가 word[idx]로 복원하는거 좋은 거 같습니다!
````

### review_comment · parkhojeong · 2026-07-17T16:01:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3604503760
- ID: review_comment:3604503760
- 파일: coin-change/yuseok89.py, 줄: 1, 원래 줄: 1

````text
bfs 방식으로 풀어주셨네요. dict 이용해서 필요한 공간만 사용하는 것도 신경쓰셔서 푸신 거 같네요.
````

### review · parkhojeong · 2026-07-17T16:01:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#pullrequestreview-4723605430
- ID: review:4723605430
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

### review_comment · yuseok89 · 2026-07-18T01:39:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3607276912
- ID: review_comment:3607276912
- 파일: find-minimum-in-rotated-sorted-array/yuseok89.py, 줄: 18, 원래 줄: 18
- 답글 대상: review_comment:3603950970

````text
의견 감사합니다 !
````

### review_comment · yuseok89 · 2026-07-18T01:40:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3607277962
- ID: review_comment:3607277962
- 파일: merge-two-sorted-lists/yuseok89.py, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3603960913

````text
return value 약자로 썼는데,
다음엔 좀 더 가독성 있게 작성해보겠습니다.
````

### review_comment · yuseok89 · 2026-07-18T01:41:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3607278617
- ID: review_comment:3607278617
- 파일: word-search/yuseok89.py, 줄: 14, 원래 줄: 14
- 답글 대상: review_comment:3604008895

````text
rec 함수에서 어떻게 활용할 수 있을까요?
````

### review_comment · parkhojeong · 2026-07-18T12:38:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2739#discussion_r3608373418
- ID: review_comment:3608373418
- 파일: word-search/yuseok89.py, 줄: 14, 원래 줄: 14
- 답글 대상: review_comment:3604008895

````text
제가 잘못 생각헀네요. 초기에 한 번 사용하면 이후 과정에선 불필요하네요!
````

## [#2740 [dahyeong-yun] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2740)

### review_comment · dolphinflow86 · 2026-07-16T14:56:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3596539173
- ID: review_comment:3596539173
- 파일: merge-two-sorted-lists/dahyeong-yun.java, 줄: 16, 원래 줄: 16

````text
@dahyeong-yun 보통 dummy로 많이 쓰는데 merged도 실제로 머지된 노드를 나타내는거라 괜찮아 보이네요!
````

### review_comment · dolphinflow86 · 2026-07-16T14:57:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3596542839
- ID: review_comment:3596542839
- 파일: merge-two-sorted-lists/dahyeong-yun.java, 줄: 34, 원래 줄: 34

````text
@dahyeong-yun 3항 연산자로 쓰는것도 깔끔해 보입니다. (취향 차이이긴 하지만)
````

### review_comment · dolphinflow86 · 2026-07-16T14:59:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3596557870
- ID: review_comment:3596557870
- 파일: merge-two-sorted-lists/dahyeong-yun.java, 줄: 14, 원래 줄: 14

````text
@dahyeong-yun 깔끔하게 풀어주셔서 더 코멘트 달 부분이 없네요. 저도 거의 같은 방식으로 풀었는데 재귀를 활용한 방법도 있더라고요? 문제는 이게 공간복잡도가 더 높아져서 구현해보지는 않았습니다 ㅎㅎ 뭐라도 말씀드려야 할 것 같아서 주저리 써보았습니다.
````

### review_comment · dolphinflow86 · 2026-07-17T13:11:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603391335
- ID: review_comment:3603391335
- 파일: word-search/dahyeong-yun.java, 줄: 53, 원래 줄: 53

````text
@dahyeong-yun 저도 처음에 이렇게 visited 썼다가, 나중에 보니 해당 보드에 문자를 #와 같은걸로 마킹하고 다시 함수 끝에서 돌려놓으면 굳이 visited가 필요없더라고요! 요 방법도 적용해보셔도 좋을 것 같아요.
````

### review_comment · dolphinflow86 · 2026-07-17T13:13:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603399077
- ID: review_comment:3603399077
- 파일: word-search/dahyeong-yun.java, 줄: 3, 원래 줄: 3

````text
@dahyeong-yun 저는 이 문제 시간복잡도 분석에 시간이 좀 걸렸었는데, 혹시 어떻게 분석을 접근하셨는지 한번 풀어서 설명해주실 수 있나요?
````

### review_comment · alphaorderly · 2026-07-17T13:35:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603541128
- ID: review_comment:3603541128
- 파일: coin-change/dahyeong-yun.java, 줄: 27, 원래 줄: 27

````text
이 부분 j 시작점을 coin으로 바꾸시면 훨씬 보기 좋을것 같아요! 반복 횟수도 줄어들구요
```
for(int j=coin; j <= amount; j++) {
    methods[j] = Math.min(methods[j], methods[j - coin] + 1);
}
```
이렇게요!
작동 되는건 확인했어요
````

### review_comment · alphaorderly · 2026-07-17T13:37:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603557654
- ID: review_comment:3603557654
- 파일: word-search/dahyeong-yun.java, 줄: 53, 원래 줄: 53
- 답글 대상: review_comment:3603391335

````text
그거 엄청 좋은 방식이네요!
visited로 임의 공간 사용 안해도 되니까 좋네요
````

### review_comment · parkhojeong · 2026-07-17T14:07:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603757993
- ID: review_comment:3603757993
- 파일: coin-change/dahyeong-yun.java, 줄: 27, 원래 줄: 27

````text
i, j, coin, amount 등이 섞여 있어 이해하는데 약간 어려웠던 거 같습니다.

1부터 amount 까지 가는 루프만 인덱스를 필요로 하니 이 떄만 i를 사용해서 루프를 돌리고 코인은 변수 값을 바로 쓰는 형태로 써보셔도 좋을 거 같습니다. 포문 순서는 바꾸셔도 될 거 같은데 점화식 형태로 업데이트하니 바깥 포문은 1~amount까지 돌리는게 생각의 흐름과 맞을 거 같습니다.
```suggestion
        for(int i=1; i <= amount; i++){
            for(int coin: coins){
                if(i >= coin){
                    methods[i] = Math.min(methods[i], methods[i - coin] + 1);
                }
            }
        }
```
````

### review_comment · parkhojeong · 2026-07-17T14:08:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603763597
- ID: review_comment:3603763597
- 파일: coin-change/dahyeong-yun.java, 줄: 24, 원래 줄: 24

````text
coins을 미리 소트해두면 좀 더 최적화 해볼 수 있을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-17T14:09:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603769709
- ID: review_comment:3603769709
- 파일: find-minimum-in-rotated-sorted-array/dahyeong-yun.java, 줄: 26, 원래 줄: 26

````text
`nums[mid] > nums[right]` 조건은 주석으로 쓰기 보단 코드로 나타내는게 더 정확할 거 같습니다. 실제로는 else 문이라 `nums[mid] >= nums[right]` 에 대한 로직이라 정확히 매치는 안되는 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-17T14:10:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603773012
- ID: review_comment:3603773012
- 파일: find-minimum-in-rotated-sorted-array/dahyeong-yun.java, 줄: 19, 원래 줄: 19

````text
nit: len은 한번만 사용이 되서 인라인해도 될 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-17T14:13:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603791743
- ID: review_comment:3603791743
- 파일: find-minimum-in-rotated-sorted-array/dahyeong-yun.java, 줄: 23, 원래 줄: 23

````text
더 최적화 한다면 `if(nums[left] < nums[mid] && nums[mid] < nums[right])` 다음과 같은 로직을 넣어보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-17T14:13:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603793939
- ID: review_comment:3603793939
- 파일: maximum-depth-of-binary-tree/dahyeong-yun.java, 줄: 16, 원래 줄: 16

````text
깔끔하네요!
````

### review_comment · parkhojeong · 2026-07-17T14:26:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603883744
- ID: review_comment:3603883744
- 파일: word-search/dahyeong-yun.java, 줄: 46, 원래 줄: 46

````text
파라미터가 다소 많은 거 같아서 줄여보셔도 좋을 거 같아요. 첫번째 파라미터 cursor는 인덱스 값을 가져서 idx 와 같은 네이밍을 고려하셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-17T14:27:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3603891570
- ID: review_comment:3603891570
- 파일: word-search/dahyeong-yun.java, 줄: 20, 원래 줄: 20

````text
visited 없이 board 에 마킹했다 되돌리는 식으로 사용하시면 보다 간결하게 작성이 되실 거 같습니다.
````

### review · parkhojeong · 2026-07-17T14:28:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#pullrequestreview-4723392972
- ID: review:4723392972
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 몇 가지 커멘트 남겨보았습니다.
````

### review_comment · dahyeong-yun · 2026-07-18T08:41:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608010887
- ID: review_comment:3608010887
- 파일: coin-change/dahyeong-yun.java, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3603541128

````text
그렇네요. 어차피 그 부분을 체크를 안해도 되니까 분기를 만들 필요가 없네요 👍🏼 
````

### review_comment · dahyeong-yun · 2026-07-18T08:49:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608022129
- ID: review_comment:3608022129
- 파일: word-search/dahyeong-yun.java, 줄: 3, 원래 줄: 3
- 답글 대상: review_comment:3603399077

````text
저도 쉽지 않았던 것 같아요. 정리된 생각으로 말씀드리면, 

- find를 하기 전에 바깥 쪽에 이중 루프가 있으므로 일단 n * m(즉, 가로 길이 * 세로 길이) 만큼은 순회를 한다고 봤고요.
- find를 하면 각 글자에서 3방향으로 다시 뻗어 나가니까, 재귀가 호출 될 때마다 3씩 곱한만큼 콜스택이 쌓일거라 3^x 형태가 된다고 생각했어요. 이 때 x가 무엇일까 생각하면, 재귀는 단어의 길이까지 찾고 멈추니까 단어의 길이가 되겠네요.

(분석이 맞는지는 잘 모르겠네요)
````

### review_comment · dahyeong-yun · 2026-07-18T08:52:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608026879
- ID: review_comment:3608026879
- 파일: word-search/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603284136

````text
@DaleStudy 시간복잡도 분석이 정확히 어떻게 되었는지 풀어서 설명해주세요. 그리고 3방향씩만 재귀가 호출되는데 왜 4의 제곱 형태로 표현했는지도 부연해 주세요. 만약 기존에 틀린 답을 제공했다고 판단되면 설명을 하기보다 정정을 해주세요.
````

### review_comment · dahyeong-yun · 2026-07-18T08:55:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608036173
- ID: review_comment:3608036173
- 파일: word-search/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603284136

````text
@Dalestudy 그러니까 word-search 문제의 시간복잡도의 경우 NM3^L이 총 수행이 되는 것은 맞으나, 최악의 근사를 가정해서 4^L로 표기 했다는 건가요?
````

### review_comment · dahyeong-yun · 2026-07-18T08:56:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608042723
- ID: review_comment:3608042723
- 파일: word-search/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603284136

````text
@Dalestudy 그럼 word-search 문제의 최초 알고리즘 패턴 분석 코멘트에 작성한 부분이 잘못되었고, 유저 분석 결과가 맞다고 이해하면 될까요?
````

### review_comment · dahyeong-yun · 2026-07-18T08:58:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608048933
- ID: review_comment:3608048933
- 파일: word-search/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603284136

````text
@Dalestudy word-search 문제의 최초 알고리즘 패턴 분석 코멘트에 실제 분석을 4^L로 명시했는데, 지금까지 대화에서 설명하기로는 O(NM3^L)이 맞다 라고 이야기 하고 있는데요. 그렇다면 초기 유저 분석의 결과가 ✅ 가 되야할 것 같습니다.
````

### review_comment · dahyeong-yun · 2026-07-18T08:59:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2740#discussion_r3608050731
- ID: review_comment:3608050731
- 파일: word-search/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603284136

````text
@dolphinflow86 봇이 분석해주기로는 이렇네요.

> 3. word-search의 재귀 호출
> 
> * 문제 아이디어: 시작 위치에서 상하좌우로 문자 일치를 따라가며 탐색합니다. 백트래킹으로 방문 배열을 유지합니다.
> * 한 위치에서의 재귀 호출
>   
>   * 현재 위치에서 4방향으로 탐색합니다. 하지만 다음 위치로 이동하기 전에 경계 체크와 방문 여부, 다음 문자인지 검사를 합니다.
>   * 실제로는 한 단계의 재귀 호출은 4방향 중 하나를 선택해 그 방향으로 깊이를 증가시키는 형태이며, 최대 재귀 깊이는 단어 길이 L에 의해 결정됩니다. 따라서 시간은 대략 N_M_(3^L)으로 표현됩니다.
>   * 3^L 표현의 이유는 첫 칸에서 시작할 때 이미 한 방향으로 진입한 경우를 제외하고, 매 다음 단계에서 한 칸을 방문했을 때 남은 3방향(뒤로 돌아가기를 제외한 세 방향)으로 분기가 가능하다는 관점 때문입니다. 즉, 첫 글자 위치에서 시작해 각 단계마다 대략 3개의 선택지가 남아 재귀 깊이가 L에 도달할 때까지 분기합니다. 이론상 최악의 경우 3^L의 경로를 탐색하고, 격자 크기 N_M에 따라 총 수행은 N_M*3^L이 됩니다.
> * 공간복잡도: 방문 배열 O(N*M) + 재귀 깊이 O(L) 입니다.
> 
> 정정/정리 요청에 따른 요약
> 
> * 제시된 시간복잡도 표기는 각각:
>   
>   * word-search: 시간 약 O(N_M_3^L), 공간 O(N*M) (또는 재귀 스택 O(L) + 방문 배열)
> * 3방향 재귀 설명의 반영: 각 단계에서 사실상 세 방향으로 분기가 가능하되, 이미 방문한 칸이나 경계 등으로 인해 실제 분기가 줄어들 수 있습니다. 따라서 3^L 근사치이지만 최악의 경우를 가정한 표현입니다. 4방향으로의 이론적 최대 분기는 재귀 시작 직후의 첫 선택이 포함되면 4^L에 근접하나, 이미 방문 제약과 이전 칸으로의 역방향을 제외하기에 실질 분기는 약 3^L입니다. 코드에서 4의 제곱 형태로 표현된 부분은 없고, 주석의 의도는 3방향 확장을 가정한 근사입니다.
> 
> 필요하면 각 문제별 수식 및 예제도 더 자세히 붙여드리겠습니다.


````

## [#2741 [dolphinflow86] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2741)

### review_comment · alphaorderly · 2026-07-17T09:29:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3601997071
- ID: review_comment:3601997071
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
혹시 pivot을 (right + left) // 2 가 아닌 left + (right - left) // 2 로 하신 이유가 있으실까요?
````

### review_comment · alphaorderly · 2026-07-17T09:31:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3602010381
- ID: review_comment:3602010381
- 파일: maximum-depth-of-binary-tree/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
이거 depth 패러미터 주지 않고 maxDepth 만으로도 구현 가능하세요! 스스로 재귀해서 하면 코드도 엄청 줄일수 있어요, 성능도 같고요
````

### review_comment · JeonJe · 2026-07-17T09:50:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3602137099
- ID: review_comment:3602137099
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 14

````text
`pivot = left + (right - left) // 2`로 오버플로를 방어하신 부분이 인상깊었습니다!

풀이를 보고 문득 Python에서는 오버플로가 어떻게 되는지 궁금해져서 찾아보니, Python의 `int`는 임의정밀도(arbitrary precision)라 값이 아무리 커져도 오버플로우가 나지 않는다고 하더라고요. 그래서 이 경우엔 `(left + right) // 2`로 단순하게 써도 괜찮지 않을까 싶은데, 어떻게 생각하시나요?

반대로 저는 Java인데도 오버플로우 방어 없이 `(left + right) / 2`로 풀었더라고요 😅
````

### review_comment · alphaorderly · 2026-07-17T09:53:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3602156435
- ID: review_comment:3602156435
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 14
- 답글 대상: review_comment:3602137099

````text
이거 근데 
- $$n == nums.length$$
- $$1 \le n \le 5000$$

nums 배열 길이가 길어야 5,000이라서
left + right 의 최대 값이 10,000이라서요
오버플로우 애초에 신경 안써도 될거에요
````

### review_comment · dolphinflow86 · 2026-07-17T13:19:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603436400
- ID: review_comment:3603436400
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 14
- 답글 대상: review_comment:3602137099

````text
두 분 다 좋은 코멘트 감사합니다!

제가 예전에는 c++로 주로 풀었다보니 습관적으로 저렇게 썼던 것 같아요.
문제 조건 상 저렇게 안해도 되겠네요! 
그리고 파이썬은 int가 임의정밀도라는 사실 새로 알게 되었습니다. 감사합니다 :)
````

### review_comment · alphaorderly · 2026-07-17T13:29:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603501517
- ID: review_comment:3603501517
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 14
- 답글 대상: review_comment:3602137099

````text
생각나서 하나 덧붙히자면 보통 오버플로우 일어나서 관리해야 하는 문제들은 10^9 + 7 로 나머지연산 해서 리턴하라고 하더라고요!

````

### review_comment · dolphinflow86 · 2026-07-17T13:29:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603501685
- ID: review_comment:3603501685
- 파일: maximum-depth-of-binary-tree/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3602010381

````text
bottom up 방식으로 depth를 더하면서 올라오면 간단하게 끝나는군요
리뷰 감사합니다!
````

### review_comment · parkhojeong · 2026-07-17T13:37:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603554224
- ID: review_comment:3603554224
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 18

````text
좀더 최적화 한다면 이 로직을 추가해볼 수 있을 거 같습니다.
```
if nums[left] < nums[pivot] < nums[right]:
                return nums[left]
```
````

### review_comment · parkhojeong · 2026-07-17T13:38:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603558840
- ID: review_comment:3603558840
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: 20, 원래 줄: 20

````text
nit: right 보단 left가 약간 더 자연스러운(?) 개인적인 느낌이 있는 거 같습니다.
```suggestion
        return nums[left]
```
````

### review_comment · parkhojeong · 2026-07-17T13:41:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603580797
- ID: review_comment:3603580797
- 파일: word-search/dolphinflow86.py, 줄: None, 원래 줄: 33

````text
n, m, w 보단 의미 있는 네이밍 사용하는게 인지 부하를 줄여줄 수 있을 거 같습니다. 
````

### review_comment · parkhojeong · 2026-07-17T13:42:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603589541
- ID: review_comment:3603589541
- 파일: word-search/dolphinflow86.py, 줄: None, 원래 줄: 35

````text
꼼꼼하게 최적화 해주셨네요.
````

### review_comment · parkhojeong · 2026-07-17T13:44:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603602628
- ID: review_comment:3603602628
- 파일: merge-two-sorted-lists/dolphinflow86.py, 줄: 27, 원래 줄: 27

````text
dummy 도 괜찮은데 의미를 조금 더 담은 네이밍이면 어떨까 싶습니다.
````

### review_comment · parkhojeong · 2026-07-17T13:47:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603621896
- ID: review_comment:3603621896
- 파일: maximum-depth-of-binary-tree/dolphinflow86.py, 줄: None, 원래 줄: 17

````text
다른 풀이(`word-search/dolphinflow86.py`)에서 인라인하시던 패턴처럼 써도 가독성이 괜찮을 거 같습니다.
변수를 사용한다면 실제로 들어가는 값에 맞추어 left_max, right_max 처럼 max의 의미를 담는 것도 좋을 거 같습니다.
```suggestion
        return max(
            self.dfs(node.left, depth + 1),
            self.dfs(node.right, depth + 1)
        )
```
````

### review_comment · parkhojeong · 2026-07-17T13:50:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603638866
- ID: review_comment:3603638866
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 14

````text
실질적으로 left, right의 중간에 해당하는 mid 값이 들어가서 mid 같은 변수명을 쓰는게 어떨까 싶습니다. 이후 역할로서 pivot으로 사용하는 거라서요.
````

### review · parkhojeong · 2026-07-17T13:50:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#pullrequestreview-4723147554
- ID: review:4723147554
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 몇가지 커멘트 남겨보았습니다.
````

### review_comment · dolphinflow86 · 2026-07-17T14:29:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3603907742
- ID: review_comment:3603907742
- 파일: find-minimum-in-rotated-sorted-array/dolphinflow86.py, 줄: None, 원래 줄: 18
- 답글 대상: review_comment:3603554224

````text
@parkhojeong 오.. 생각하지 못했는데 좋은 최적화 포인트네요!
알려주셔서 감사합니다.
````

### review_comment · dahyeong-yun · 2026-07-18T01:59:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3607315608
- ID: review_comment:3607315608
- 파일: word-search/dolphinflow86.py, 줄: 16, 원래 줄: 16

````text
추가 공간 없이 임시문자로 대체 했다가 복구하는 것도 좋은 방법이네요 👍🏼 
````

### review · dahyeong-yun · 2026-07-18T02:13:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#pullrequestreview-4727357302
- ID: review:4727357302
- 리뷰 상태: APPROVED

````text
한 주간 고생하셨습니다! 다른 분들도 많이 리뷰를 해주셨네요. 코드도 간결하고, 저도 비슷한 방식으로 풀었어서 크게 코멘트 드릴 부분은 없는 것 같아요 :) 

저는 이번 주 word-search 과 같이 백트래킹 해야 하는 부분이 항상 좀 쉽게 안 떠오르고 안 풀리더라고요. dolphinflow86 님은 풀면서 다른 어려움은 없으셨는지 궁금하네요. 다음 주도 화이팅 해봐요~!
````

### review_comment · parkhojeong · 2026-07-18T06:52:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#discussion_r3607823302
- ID: review_comment:3607823302
- 파일: word-search/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
실제로 돌려보니 4000ms 정도 나오는데 조금 더 최적화 해보셔도 좋을 것 같습니다. 
````

### issue_comment · dolphinflow86 · 2026-07-18T08:14:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2741#issuecomment-5010546548
- ID: issue_comment:5010546548

````text
> 한 주간 고생하셨습니다! 다른 분들도 많이 리뷰를 해주셨네요. 코드도 간결하고, 저도 비슷한 방식으로 풀었어서 크게 코멘트 드릴 부분은 없는 것 같아요 :)
> 
> 저는 이번 주 word-search 과 같이 백트래킹 해야 하는 부분이 항상 좀 쉽게 안 떠오르고 안 풀리더라고요. dolphinflow86 님은 풀면서 다른 어려움은 없으셨는지 궁금하네요. 다음 주도 화이팅 해봐요~!

코멘트 감사합니다! 저도 백트래킹 하는거랑, top down DP랑 가끔식 혼동이 오더라고요, 비슷한 문제를 계속 풀어보면 어느순간 패턴이 좀 보이지 않을까 합니다. 한 주간 고생 많으셨고 같이 화이팅 하시죠!
````

## [#2742 [JeonJe] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2742)

### review_comment · okyungjin · 2026-07-18T11:42:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608277266
- ID: review_comment:3608277266
- 파일: coin-change/JeonJe.java, 줄: 1, 원래 줄: 1

````text
저는 바텀업 방식으로 작성했는데 탑다운으로 풀어주셨군요!
coins: [1], amout: 10000이 입력으로 주어졌을 때 재귀 스택이 10,000까지 깊어질 수 있을 것 같습니다~

````

### review_comment · okyungjin · 2026-07-18T11:43:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608278792
- ID: review_comment:3608278792
- 파일: find-minimum-in-rotated-sorted-array/JeonJe.java, 줄: 1, 원래 줄: 1

````text
저도 동일하게 이진 탐색하도록 풀었습니다. 잘 봤습니다!
````

### review_comment · okyungjin · 2026-07-18T11:45:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608281787
- ID: review_comment:3608281787
- 파일: maximum-depth-of-binary-tree/JeonJe.java, 줄: 1, 원래 줄: 1

````text
직관적이고 간결한 풀이 잘 봤습니다 👍 
````

### review_comment · okyungjin · 2026-07-18T11:47:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608284113
- ID: review_comment:3608284113
- 파일: merge-two-sorted-lists/JeonJe.java, 줄: 1, 원래 줄: 1

````text
ListNode 할당하는 로직을 조금 수정해서 공간 복잡도를 O(1)로 개선해보면 좋을 것 같습니다!
````

### review_comment · okyungjin · 2026-07-18T11:49:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608286894
- ID: review_comment:3608286894
- 파일: word-search/JeonJe.java, 줄: 1, 원래 줄: 1

````text
dx, dy로 포지션을 미리 할당해놓고 쓰니까 깔끔하네요. 잘 봤습니다!!

visited 배열을 선언하지 않도록해서 공간 복잡도를 O(L)로 최적화를 해보는 것도 좋을 것 같습니다 🔥
````

### review · okyungjin · 2026-07-18T11:49:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#pullrequestreview-4728423660
- ID: review:4728423660
- 리뷰 상태: APPROVED

````text
이번 주도 고생 많으셨습니다~ 다음 주도 파이팅입니다!
````

### review_comment · JeonJe · 2026-07-18T11:51:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608289461
- ID: review_comment:3608289461
- 파일: word-search/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608286894

````text
무의식적으로 visited 배열을 사용해서 dfs/bfs 를 풀고 있었는데 사용하지 않는 방식도 고민을 해봐야겠네요 
감사합니다!!
````

### review_comment · JeonJe · 2026-07-18T11:53:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608296786
- ID: review_comment:3608296786
- 파일: merge-two-sorted-lists/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608284113

````text
노드를 새로 만드는게 아니라, 이미 있는 list1, list2 노드를 이어 붙여주는 방식으로 최적화가 가능하겠네요!
생각 못했던 부분인데 좋은 리뷰 감사합니다!!
````

### review_comment · JeonJe · 2026-07-18T11:58:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2742#discussion_r3608308294
- ID: review_comment:3608308294
- 파일: coin-change/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608277266

````text
아하 조금만 제약 조건의 범위가 늘어나면 스택 오버플로우가 발생할 수 있겠네요.
반복문을 써서 가장 작은 금액 단위부터 채워나가는 식의 바텀업 풀이가 좋아보이긴하네요.

꼼꼼한 리뷰 감사합니다!
````

## [#2743 [okyungjin] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2743)

### review_comment · okyungjin · 2026-07-13T15:54:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3572103588
- ID: review_comment:3572103588
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 1, 원래 줄: 1

````text
@DaleStudy 개선 제안: 더 나은 변수 네이밍과 주석 정리로 가독성을 높일 수 있습니다. 는 어떤 방식을 말하는건지 제안해주라 
````

### review_comment · okyungjin · 2026-07-13T15:57:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3572125305
- ID: review_comment:3572125305
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 1, 원래 줄: 1

````text
@DaleStudy 풀이1 공간 복잡도 설명해주라. 풀이 1에서 새로운 노드를 생성하는 비용을 최적화하려고 풀이2로 변경한거거든. 둘다 O(1) 이라고 볼 수 있는거야?
````

### review_comment · okyungjin · 2026-07-13T15:58:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3572137672
- ID: review_comment:3572137672
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3572125305

````text
@DaleStudy 그러면 https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3572117569 풀이 1에서 내가 예측한 공간 복잡도가 맞는 거 아닌가?
````

### review_comment · okyungjin · 2026-07-13T15:59:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3572146230
- ID: review_comment:3572146230
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3572125305

````text
@DaleStudy 그러면  ❌ 표시 없어야 하는거 아닌가해서! 저 분석 표를 다시 그려주라 

````

### review_comment · okyungjin · 2026-07-13T16:00:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3572152725
- ID: review_comment:3572152725
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3572125305

````text
@DaleStudy 이 파일의 알고리즘 시간/공간 복잡도 분석 
````

### review_comment · chapse57 · 2026-07-16T14:35:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3596367055
- ID: review_comment:3596367055
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 52, 원래 줄: 52

````text
이 부분에서 ListNode(list1.val)로 매번 새 노드를 생성하시는데, 기존 노드를 그대로 연결(node.next = list1)하면 새 노드를 안 만들어도 돼서 공간 복잡도를 O(1)로 줄일 수 있을 것 같아요. 저는 그렇게 풀었는데 참고하시라고 남깁니다! 전체 로직은 깔끔하게 잘 읽혔어요 👍
````

### review_comment · okyungjin · 2026-07-18T07:41:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3607924780
- ID: review_comment:3607924780
- 파일: merge-two-sorted-lists/okyungjin.py, 줄: 52, 원래 줄: 52
- 답글 대상: review_comment:3596367055

````text
@chapse57 코멘트 감사합니다! 풀이를 2가지로 작성했는데 이 부분 언급해주신게 맞을까요?

https://github.com/okyungjin/leetcode-study/blob/f24511286b1f9519e87e5d64fdb19e3648658584/merge-two-sorted-lists/okyungjin.py#L72-L99

````

### review_comment · okyungjin · 2026-07-18T09:46:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608113579
- ID: review_comment:3608113579
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 1, 원래 줄: 1

````text
@dalestudy 내가 의도한 유형으로 안 풀었어?
````

### review_comment · okyungjin · 2026-07-18T09:47:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608115152
- ID: review_comment:3608115152
- 파일: word-search/okyungjin.py, 줄: 1, 원래 줄: 1

````text
@dalestudy 시간 복잡도랑 공간 복잡도 어떻게 계산했어? 과정 알려줘
````

### review_comment · okyungjin · 2026-07-18T09:50:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608120135
- ID: review_comment:3608120135
- 파일: word-search/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608115152

````text
@dalstudy word-search 프루닝 어떻게 하면 더 좋을지 제안해주라. 해시맵으로 문자열의 좌표를 미리 기록해두기?
````

### review_comment · okyungjin · 2026-07-18T11:04:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608225582
- ID: review_comment:3608225582
- 파일: coin-change/okyungjin.py, 줄: 1, 원래 줄: 1

````text
@dalstudy O(A * C)랑 O(C * A)랑 같은거 아닐까!
````

### review_comment · ICE0208 · 2026-07-18T11:12:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608235897
- ID: review_comment:3608235897
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 21, 원래 줄: 21

````text
현재 구현은 LIFO 방식으로 동작하므로, 변수 이름도 `queue`보다 `stack`이 자연스러울 것 같습니다!

반대로 FIFO 방식의 큐로 구현한다면 노드가 깊이 순서대로 처리되므로, `max()`를 사용하지 않고 `max_depth = cur_depth`로 갱신하는 것만으로도 충분할 것 같습니다.
````

### review_comment · ICE0208 · 2026-07-18T11:19:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608244277
- ID: review_comment:3608244277
- 파일: word-search/okyungjin.py, 줄: 1, 원래 줄: 1

````text
DFS를 시작하기 전에 단어의 길이가 보드 전체 칸 수보다 긴지 확인하면, 경로를 만들 수 없는 입력을 탐색 전에 바로 제외할 수 있을 것 같습니다!
````

### review · ICE0208 · 2026-07-18T11:23:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#pullrequestreview-4728377584
- ID: review:4728377584
- 리뷰 상태: APPROVED

````text
안녕하세요. 이번 주 리뷰를 담당한 ICE0208입니다.

각 풀이의 주석이 잘 정리되어 있었고, 구현 방식도 제가 푼 방식과 유사해 비교하며 이해하기 쉬웠습니다. 몇 가지 의견은 코멘트로 남겼습니다.

이번 주도 고생 많으셨습니다! 👍
````

### review_comment · okyungjin · 2026-07-18T11:27:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608254329
- ID: review_comment:3608254329
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 21, 원래 줄: 21
- 답글 대상: review_comment:3608235897

````text
@ICE0208 놓친 부분 짚어주셔서 감사합니다!
````

### review_comment · okyungjin · 2026-07-18T11:30:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608258204
- ID: review_comment:3608258204
- 파일: word-search/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608244277

````text
좋은 의견 감사합니다!
````

### review_comment · okyungjin · 2026-07-18T12:02:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2743#discussion_r3608314648
- ID: review_comment:3608314648
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 21, 원래 줄: 21
- 답글 대상: review_comment:3608235897

````text
stack으로 변수명 수정했습니다(6808c867c0614697cb554ba9fd5bd1f2e9b50231)

감사합니다!
````

## [#2744 [ICE0208] WEEK 04 Solutions ](https://github.com/DaleStudy/leetcode-study/pull/2744)

### review_comment · parkhojeong · 2026-07-18T12:50:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#discussion_r3608392637
- ID: review_comment:3608392637
- 파일: coin-change/ICE0208.java, 줄: 1, 원래 줄: 1

````text
변수명이나 로직이 깔끔한 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T12:52:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#discussion_r3608395499
- ID: review_comment:3608395499
- 파일: find-minimum-in-rotated-sorted-array/ICE0208.java, 줄: 1, 원래 줄: 1

````text
dfs 로 풀어주셨네요. while 문을 사용하시면 좀 더 간결하게 작성이 가능할 거 같아서 시도해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T12:55:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#discussion_r3608400108
- ID: review_comment:3608400108
- 파일: word-search/ICE0208.java, 줄: 1, 원래 줄: 1

````text
요거 돌려보니 runtime이 하위 20~30% 정도로 나와서 최적화 좀 더 시도해보셔도 좋을 거 같습니다. 불필요한 탐색 과정을 사전에 정리하는 방식으로 접근해보시면 될 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T12:55:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#discussion_r3608400595
- ID: review_comment:3608400595
- 파일: coin-change/ICE0208.java, 줄: 9, 원래 줄: 9

````text
이름이 강렬하네요
````

### review_comment · parkhojeong · 2026-07-18T12:56:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#discussion_r3608401948
- ID: review_comment:3608401948
- 파일: merge-two-sorted-lists/ICE0208.java, 줄: 1, 원래 줄: 1

````text
요거 재귀로도 풀어보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-18T12:56:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#pullrequestreview-4728532937
- ID: review:4728532937
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

### review_comment · ICE0208 · 2026-07-18T14:42:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2744#discussion_r3608554091
- ID: review_comment:3608554091
- 파일: word-search/ICE0208.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608400108

````text
직접 돌려주시기까지 하시다니 꼼꼼한 리뷰 감사합니다!
복습하면서 더 최적화해보도록 하겠습니다!
````

## [#2745 [chapse57] Week 4 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2745)

### issue_comment · DaleSeo · 2026-07-16T01:47:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2745#issuecomment-4987255653
- ID: issue_comment:4987255653

````text
@chapse57 님, 이번 주차 풀이 제출 감사합니다! Merge Two Sorted Lists 풀이 잘 봤어요.

> ※ 이전 주차 커밋이 본진 미머지 상태라 함께 딸려왔습니다

제가 PR 본문에 이 말의 뜻을 잘 이해하지 못했습니다. 혹시 어떤 상황인지 조금만 더 설명해주실 수 있을까요?
Commits 탭과 Files changed 탭을 열어보니 이번 주차 문제 외에도 이전 주차 파일들이 diff에 함께 잡혀 있던데 이 것 때문에 그런 건가요?
이렇게 관련 없는 변경까지 계속 누적해서 한꺼번에 올라오면 다른 리뷰어들도 혼란스러울 것 같아서 여쭙니다.
````

### issue_comment · chapse57 · 2026-07-16T05:50:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2745#issuecomment-4988642881
- ID: issue_comment:4988642881

````text
@DaleSeo 안녕하세요! 확인 감사합니다.

말씀하신 게 맞습니다. 제가 fork에서 계속 main 브랜치로 작업하다 보니,
이전 주차 커밋들이 본진에 squash 머지된 뒤에도 제 fork에는 원본이 남아
새 PR마다 이전 파일들이 diff에 함께 잡히고 있었습니다.

알고리즘 스터디가 처음이라 브랜치/fork 관리가 미숙했습니다.
이번 PR 머지 후에 fork를 sync하고, 다음 주차부터는 주차별로 브랜치를 나눠서
이번 주 변경만 깔끔하게 올라오도록 하겠습니다. 알려주셔서 감사합니다!

On Thu, Jul 16, 2026 at 10:48 AM Dale Seo ***@***.***> wrote:

> *DaleSeo* left a comment (DaleStudy/leetcode-study#2745)
> <https://github.com/DaleStudy/leetcode-study/pull/2745#issuecomment-4987255653>
>
> @chapse57 <https://github.com/chapse57> 님, 이번 주차 풀이 제출 감사합니다! Merge Two
> Sorted Lists 풀이 잘 봤어요.
>
> ※ 이전 주차 커밋이 본진 미머지 상태라 함께 딸려왔습니다
>
> 제가 PR 본문에 이 말의 뜻을 잘 이해하지 못했습니다. 혹시 어떤 상황인지 조금만 더 설명해주실 수 있을까요?
> Files changed 탭을 열어보니 이번 주차 문제 외에도 이전 주차 파일들이 diff에 함께 잡혀 있던데 이 것 때문에 그런
> 건가요?
> 이렇게 간련 없는 변경까지 계속 누적해서 한꺼번에 올라오면 다른 리뷰어들도 헷갈릴 것 같아서 여쭙니다.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/DaleStudy/leetcode-study/pull/2745?email_source=notifications&email_token=APBYVYKDP3XW4EQQDOPBE235FAX57A5CNFSNUABFM5UWIORPF5TWS5BNNB2WEL2JONZXKZKDN5WW2ZLOOQXTIOJYG4ZDKNJWGUZ2M4TFMFZW63VHNVSW45DJN5XKKZLWMVXHJLDGN5XXIZLSL5RWY2LDNM#issuecomment-4987255653>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/APBYVYM5W2PTKZE6GLXJLDL5FAX57AVCNFSNUABFKJSXA33TNF2G64TZHM3TQOBXGMZTGNBSHNEXG43VMU5TIOBZGAZDONJRHA22C5QC>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>

````

### issue_comment · DaleSeo · 2026-07-16T14:12:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2745#issuecomment-4992897186
- ID: issue_comment:4992897186

````text
@chapse57 님, 빠르고 솔직한 답변 감사합니다!

그런데 굳이 다음 주까지 기다리실 필요가 있을까요? 지금 이 PR에서 바로 정리하실 수 있는 문제라고 생각합니다. 머지 후에 sync가 아니라, 먼저 sync를 하고 나면 이 PR의 diff도 이번 주 파일 하나로 줄어들거든요.

fork의 main 브랜치에서 다음 명령어를 실행하시면 됩니다.

```bash
git fetch upstream           # upstream = DaleStudy/leetcode-study
git merge upstream/main      # GitHub 웹에서 "Sync fork" 버튼과 동일
git push origin main         # PR도 자동 갱신
```

그리고 하나 더 말씀드리고 싶은 게 있어요. 알고리즘 스터디가 처음이라 미숙했다고 하셨는데, 사실 이건 저희 스터디에만 해당하는 게 아니라 어떤 협업 저장소에서든 통하는 기본적인 협업 예절에 가깝다고 생각합니다. PR에 꼭 필요한 변경만 담고, main이 아니라 브랜치에서 작업하고, fork를 upstream과 맞춰두는 것, 전부 다른 저장소에 기여할 때도 그대로 쓰이는 습관들이죠. 그래서 지금 여기서 익혀두시면 나중에 회사나 오픈소스에서 크게 도움이 되실 거예요. 저희 스터디가 그런 협업 흐름을 편하게 연습할 수 있는 곳이기도 하고요.

솔직히 이런 피드백을 받는 게 조금 불편하게 느껴지실 수도 있다는 것, 잘 알고 있어요. 그럼에도 말씀드리는 이유는 제가 이 스터디 전체의 경험을 챙겨야 하는 입장이라서예요. 리뷰어분들은 각자 시간을 내어 자원해서 코드를 봐주시는데, 관련 없는 파일이 매주 쌓여서 올라오면 어떤 게 이번 주 변경인지 가려내는 데만 힘을 빼게 되고, 그게 반복되면 리뷰 문화 자체가 지치게 되거든요. 반대로 PR이 깔끔하면 리뷰어도 정말 봐야 할 코드에 집중할 수 있고, 그 혜택은 결국 모든 참가자에게 돌아갑니다.

제 피드백을 너무 불편하게 받아들이지 않으셨으면 하고, 혹시 위 과정에서 막히는 부분 있으면 편하게 물어봐 주세요.
````

### issue_comment · chapse57 · 2026-07-16T14:39:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2745#issuecomment-4993171142
- ID: issue_comment:4993171142

````text
@DaleSeo 알려주신 대로 upstream 등록하고 fetch → merge → push 했더니 이번 주 파일 하나만 남았습니다.
Files changed도 8개에서 1개로 줄었어요. 짚어주셔서 감사합니다. 다음 주차부터는 브랜치 나눠서 작업하겠습니다!

> Message ID: ***@***.***>
>

````

### review_comment · parkhojeong · 2026-07-17T13:16:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2745#discussion_r3603422770
- ID: review_comment:3603422770
- 파일: merge-two-sorted-lists/chapse57.py, 줄: 28, 원래 줄: 28

````text
깔끔한 풀이네요! 다른 부분은 쉽게 이해가 됐는데 dummy 가 무슨 값을 가지는지 생각을 해야했던 거 같습니다. dummy_head 같은 약간은 의미를 드러내는 것이면 어떨까 생각해봤습니다.
````

### review · parkhojeong · 2026-07-17T13:25:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2745#pullrequestreview-4722997934
- ID: review:4722997934
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다.

PR 제목 형식(`[discord-id] WEEK N solutions`)이 맞지 않아서 request-changes 남겨 놓습니다.  PR 내용의 문제도 #224 형태로 남겨주시면 이후에 다른 분들이 볼 떄도 편할 거 같아서 함께 수정해주시면 좋을 거 같습니다. 

[답안 제출 가이드](https://github.com/DaleStudy/leetcode-study/wiki/%EB%8B%B5%EC%95%88-%EC%A0%9C%EC%B6%9C-%EA%B0%80%EC%9D%B4%EB%93%9C) 에 있으니 전체적으로 살펴보시면 좋을 거 같습니다.


````

## [#2746 [DaleSeo] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2746)

### issue_comment · DaleSeo · 2026-07-17T12:53:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2746#issuecomment-5003484572
- ID: issue_comment:5003484572

````text
@seongmin36 님, 별다른 피드백 없으시면 승인 부탁드리겠습니다.
````

### review_comment · parkhojeong · 2026-07-17T13:04:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2746#discussion_r3603348639
- ID: review_comment:3603348639
- 파일: find-minimum-in-rotated-sorted-array/DaleSeo.rs, 줄: 16, 원래 줄: 13

````text
조금 더 최적화 한다면 lo, mid, hi 중 lo에 해당하는 값이 가장 작을 때에는 바로 리턴해도 될 거 같습니다.

case 1
```
1 2 3 4 5 --> 이 케이스 
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
```

case 2
```
1 2 3  --> 이 케이스
2 3 1
3 1 2
```

대략 이런 코드가 되겠네요.

```suggestion
        while lo < hi {
            let mid = (lo + hi) / 2;
            
            if nums[lo] < nums[mid] && nums[mid] < nums[hi]{
                return nums[lo]
            }
            
            if nums[mid] > nums[hi] {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
```
````

### review · parkhojeong · 2026-07-17T13:04:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2746#pullrequestreview-4722913404
- ID: review:4722913404
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 깔끔하게 풀어주신 거 같습니다.
````

### review_comment · seongmin36 · 2026-07-17T13:05:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2746#discussion_r3603356111
- ID: review_comment:3603356111
- 파일: find-minimum-in-rotated-sorted-array/DaleSeo.rs, 줄: 19, 원래 줄: 16

````text
이진탐색으로 해결해주셨군요, 코드 잘 봤습니다. 고생하셨습니다!
````

### review · seongmin36 · 2026-07-17T13:06:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2746#pullrequestreview-4722922127
- ID: review:4722922127
- 리뷰 상태: APPROVED

````text
rust는 처음 접해봐서 찾아보면서 봤습니다. 선언문이 정말 특이하네요! 직관적이면서 간단하고, 재미있는 것 같습니다.
4주차도 수고하셨습니다!
````

### review_comment · DaleSeo · 2026-07-17T23:41:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2746#discussion_r3606988688
- ID: review_comment:3606988688
- 파일: find-minimum-in-rotated-sorted-array/DaleSeo.rs, 줄: 16, 원래 줄: 13
- 답글 대상: review_comment:3603348639

````text
@parkhojeong 님, 좋은 제안 감사합니다! 🙏 
탐색 구간이 이미 정렬돼 있으면 맨 앞이 최소값이니 바로 반환할 수 있겠네요.
그런데 `mid`까지 볼 필요 없이 `nums[lo] < nums[hi]` 한 번의 비교만으로 동일한 조기 반환을 할 수 있더라고요.
그래서 아래처럼 좀 더 단순화하여 반영하겠습니다.

```suggestion
        while lo < hi {
            if nums[lo] < nums[hi] {
                return nums[lo];
            }
            let mid = (lo + hi) / 2;
            if nums[mid] > nums[hi] {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
```


````

## [#2747 [seongmin36] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2747)

### review_comment · alphaorderly · 2026-07-17T04:14:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2747#discussion_r3600322169
- ID: review_comment:3600322169
- 파일: merge-two-sorted-lists/seongmin36.js, 줄: 1, 원래 줄: 1

````text
O(1) 공간복잡도와 O(N) 시간복잡도로도 해결하실수 있으세요! 한번 시도해보시는것도 좋겠네요
````

### review_comment · parkhojeong · 2026-07-18T12:45:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2747#discussion_r3608386086
- ID: review_comment:3608386086
- 파일: find-minimum-in-rotated-sorted-array/seongmin36.js, 줄: 22, 원래 줄: 18

````text
탐색 과정에서 정답으로 판정할 수 있는 경우가 있어서 한 번 최적화 시도해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T12:47:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2747#discussion_r3608388893
- ID: review_comment:3608388893
- 파일: maximum-depth-of-binary-tree/seongmin36.js, 줄: None, 원래 줄: 26

````text
count 보단 maxDepth 와 같은 네이밍이 더 적절할 거 같은데 함수명이랑 겹쳐서 인라인해도 괜찮을 거 같습니다.
````

### review · parkhojeong · 2026-07-18T12:47:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2747#pullrequestreview-4728526419
- ID: review:4728526419
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 코드가 간결해서 좋네요!
````

### review_comment · seongmin36 · 2026-07-18T14:32:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2747#discussion_r3608539350
- ID: review_comment:3608539350
- 파일: find-minimum-in-rotated-sorted-array/seongmin36.js, 줄: 22, 원래 줄: 18
- 답글 대상: review_comment:3608386086

````text
그렇네요, 회전된 정렬 배열이라는 점에서 최솟값을 바로 찾을 수 있겠네요! 피드백 감사합니다 ☺️
````

## [#2748 [tigermint] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2748)

### review_comment · parkhojeong · 2026-07-18T11:20:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#discussion_r3608245235
- ID: review_comment:3608245235
- 파일: maximum-depth-of-binary-tree/tigermint.kt, 줄: 28, 원래 줄: 28

````text
!! 단언은 불필요한 것 같네요.
````

### review_comment · parkhojeong · 2026-07-18T11:22:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#discussion_r3608248041
- ID: review_comment:3608248041
- 파일: merge-two-sorted-lists/tigermint.kt, 줄: None, 원래 줄: 31

````text
여기 !! 도 불필요한 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T11:24:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#discussion_r3608251331
- ID: review_comment:3608251331
- 파일: word-search/tigermint.kt, 줄: 10, 원래 줄: 10

````text
board를 활용해 방문한 셀은 마킹해놓는 식으로 하면 visited 선언 없이도 가능하니 이렇게 풀어보시는 것도 추천드립니다.
````

### review_comment · parkhojeong · 2026-07-18T11:25:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#discussion_r3608252041
- ID: review_comment:3608252041
- 파일: word-search/tigermint.kt, 줄: 26, 원래 줄: 26

````text
전역변수 flag 대신 dfs 함수의 반환 값을 boolean으로 활용해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T11:26:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#discussion_r3608253377
- ID: review_comment:3608253377
- 파일: word-search/tigermint.kt, 줄: 19, 원래 줄: 19

````text
실제로 돌려보니 runtime 이 50% 정도 나오는데요. board, word 인풋을 가지고 미리 리턴할 수 있는 케이스도 고려해서 최적화 해보시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T11:28:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#discussion_r3608255275
- ID: review_comment:3608255275
- 파일: find-minimum-in-rotated-sorted-array/tigermint.kt, 줄: 9, 원래 줄: 9

````text
작성하신 로직의 아이디어에서 중간에 해답인 케이스를 알 수 있는데요. 이 떄는 더 이상 진행할 필요가 없어서 최적화 해보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-18T11:29:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2748#pullrequestreview-4728385249
- ID: review:4728385249
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

## [#2749 [parkhojeong] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2749)

### review_comment · alphaorderly · 2026-07-17T14:15:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3603811052
- ID: review_comment:3603811052
- 파일: find-minimum-in-rotated-sorted-array/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
혹시 슬라이싱을 쓰신 이유가 있으실까요?
슬라이싱은 그 크기만큼 O(N) 시간복잡도라 빠르진 않을것 같아서요, 
문자열은 immutable 한 객체라서 새로 복사해서 주는 방식으로 작동하잖아요
````

### review_comment · alphaorderly · 2026-07-17T14:19:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3603837858
- ID: review_comment:3603837858
- 파일: word-search/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
이거 풀이 1900ms 나오는데 0ms까지 줄일수 있는거 아시나요? 한번 시도해보시는것도 재밌으실거에요!
````

### review_comment · alphaorderly · 2026-07-17T14:22:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3603858791
- ID: review_comment:3603858791
- 파일: merge-two-sorted-lists/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
너무 잘 풀어 주셨는데, 다만 조금 아쉬운점은 로직이 너무 복잡해서 코드 가독성이 떨어지는게 아닐까 싶어요
차라리 더미 헤드를 하나 써서 푸시는게 더 나을듯 하다는 생각이 듭니다.
실제로 다른 링크드 리스트 문제들을 풀다 보시면 더미 헤드를 썼을때 코드가 간결해지는 경우가 꽤 많이 있어요
````

### review_comment · parkhojeong · 2026-07-17T14:32:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3603926944
- ID: review_comment:3603926944
- 파일: word-search/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603837858

````text
오 한 번 시도 해보곘습니다. 리뷰 감사합니다! 
````

### issue_comment · parkhojeong · 2026-07-17T18:50:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#issuecomment-5006506924
- ID: issue_comment:5006506924

````text
@alphaorderly 
알파님 리뷰 감사합니다. 아까 달아주신 리뷰에 댓글을 남겼는데 추가로 커밋을 하니 제가 남긴 커멘트가 삭제되었고 댓글 다는 인풋창도 없어지네요.

주로 커멘트를 봇 커멘트에 남겨주시는 거 같은데요. 별도 커멘트로 남겨주시면 좋을 거 같습니다. 달아주셨던 것들은 별도 커멘트로 답변드릴게요
<img width="921" height="300" alt="image" src="https://github.com/user-attachments/assets/9c62a0c2-82a5-4f99-a43a-bdad16bb567c" />

````

### issue_comment · parkhojeong · 2026-07-17T18:52:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#issuecomment-5006520457
- ID: issue_comment:5006520457

````text
@alphaorderly 

> 이거 풀이 1900ms 나오는데 0ms까지 줄일수 있는거 아시나요? 한번 시도해보시는것도 재밌으실거에요!

https://github.com/DaleStudy/leetcode-study/pull/2749/commits/c98db17ebcec64e0542534a12e02534b6aaa4398 로 최적화 시도해봤습니다. 인풋 패턴에 따른 최적화랑 카운터 기반으로 도중에 체크하는 방식이 이 문제에선 적합한 거 같네요! 

알파님 푸셨던 풀이에도 커멘트 하나 남겨놓았습니다 :) https://github.com/DaleStudy/leetcode-study/pull/2737#discussion_r3605274179

````

### issue_comment · DaleSeo · 2026-07-17T23:43:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#issuecomment-5008572845
- ID: issue_comment:5008572845

````text
@parkhojeong 님, 주차 설정 좀 부탁드리겠습니다. 안 그럼 통계에서 누락이 되서요.

<img width="1054" height="606" alt="2026-07-17 at 19 42 45" src="https://github.com/user-attachments/assets/ca41fd5b-a7e3-4b6d-a1e8-d9133cecdaa3" />

````

### issue_comment · parkhojeong · 2026-07-18T02:01:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#issuecomment-5009338516
- ID: issue_comment:5009338516

````text
> @parkhojeong 님, 주차 설정 좀 부탁드리겠습니다. 안 그럼 통계에서 누락이 되서요.
> 

@DaleSeo 설정했습니다. 확인 감사합니다. 
````

### review_comment · daehyun99 · 2026-07-18T06:56:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3607828981
- ID: review_comment:3607828981
- 파일: word-search/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
`backtrack`과 `DIRECTIONS`, `MARKER`를 사용한 풀이가 직관적으로 이해가 잘 되서 좋네요!
````

### review_comment · daehyun99 · 2026-07-18T07:08:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3607851196
- ID: review_comment:3607851196
- 파일: find-minimum-in-rotated-sorted-array/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
이건 사담인데

`[3, 1]` 테스트 케이스에 대하여, `mid_idx=1`이 되고, 아래의 코드에서 `nums[mid_idx + 1:]`가 `nums[2:]`로 되어서 인덱스 에러가 날 줄 알았는데, 안나는군요!
리뷰할 때마다 새로운 사실을 알아가게 되네요.

```py
            else:
                nums = nums[mid_idx + 1:]
```
````

### review_comment · daehyun99 · 2026-07-18T07:09:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3607852875
- ID: review_comment:3607852875
- 파일: coin-change/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
`sys.maxsize`로 최대값을 설정할 수 있군요!
많이 배워갑니다.
````

### review · daehyun99 · 2026-07-18T07:10:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#pullrequestreview-4727940362
- ID: review:4727940362
- 리뷰 상태: APPROVED

````text
안녕하세요.
4주차 리뷰를 맡은 김대현입니다!

전체적으로 잘 풀어주신 것 같네요. 고생하셨습니다!
````

### issue_comment · parkhojeong · 2026-07-18T11:57:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#issuecomment-5011161082
- ID: issue_comment:5011161082

````text
@alphaorderly 
슬라이싱을 미처 생각 못했었는데 CPython3.14 기준으로는 O(k) (k=길이) 에 해당하는 시간,공간 복잡도를 가지네요.  최적화 진행해봤습니다! [optimize find-minimum-in-rotated-sorted-array](https://github.com/DaleStudy/leetcode-study/pull/2749/commits/31ba2f45a4fa6c127855125ade6b059efe94710e)

슬라이싱 구현체 진입점: _BINARY_SLICE (https://github.com/python/cpython/blob/3.14/Python/bytecodes.c#L847-L863)
````

### review_comment · parkhojeong · 2026-07-18T12:14:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3608338551
- ID: review_comment:3608338551
- 파일: find-minimum-in-rotated-sorted-array/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3607851196

````text
파이썬이 range 넘어가는 경우엔 빈 배열로 되는 것을 사용해보았습니다. 근데 이 풀이는 슬라이싱이 O(n)의 복잡도라 최적화 진행해봤습니다. https://github.com/DaleStudy/leetcode-study/pull/2749/commits/31ba2f45a4fa6c127855125ade6b059efe94710e
````

### review_comment · parkhojeong · 2026-07-18T12:43:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3608382234
- ID: review_comment:3608382234
- 파일: word-search/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3607828981

````text
대문자 케이싱을 사용하면 가독성이 괜찮더라구요. 빈도 기반으로 체크하는 로직은 초기 한 번만 하면 되서 정리해보았습니다. https://github.com/DaleStudy/leetcode-study/pull/2749/commits/994aca2bb42177137cb0c275a875c1e14b4bdffd
````

### issue_comment · parkhojeong · 2026-07-18T12:43:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#issuecomment-5011296275
- ID: issue_comment:5011296275

````text
> 안녕하세요. 4주차 리뷰를 맡은 김대현입니다!
> 
> 전체적으로 잘 풀어주신 것 같네요. 고생하셨습니다!

리뷰 감사합니다. 대현님 리뷰 남겨주신 이후에 몇가지 최적화하여서 커멘트 남겨두었습니다 
````

### review_comment · okyungjin · 2026-07-19T03:13:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3609689750
- ID: review_comment:3609689750
- 파일: find-minimum-in-rotated-sorted-array/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3607851196

````text
> 이건 사담인데
> 
> `[3, 1]` 테스트 케이스에 대하여, `mid_idx=1`이 되고, 아래의 코드에서 `nums[mid_idx + 1:]`가 `nums[2:]`로 되어서 인덱스 에러가 날 줄 알았는데, 안나는군요! 리뷰할 때마다 새로운 사실을 알아가게 되네요.
> 
>             else:
>                 nums = nums[mid_idx + 1:]

오호 재밌는 언어네요
````

### review_comment · okyungjin · 2026-07-19T03:15:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2749#discussion_r3609693109
- ID: review_comment:3609693109
- 파일: find-minimum-in-rotated-sorted-array/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603811052

````text
> 혹시 슬라이싱을 쓰신 이유가 있으실까요? 슬라이싱은 그 크기만큼 O(N) 시간복잡도라 빠르진 않을것 같아서요, 문자열은 immutable 한 객체라서 새로 복사해서 주는 방식으로 작동하잖아요

@alphaorderly 이미 머지된 PR이지만 공부하려고 구경 중에 질문드립니다.
문자열 슬라이스에 대한 로직이 어떤 라인에 있는지 알 수 있을까요? 파일 히스토리를 찾아보았는데 문자열을 슬라이싱하는 로직을 못 찾아서 질문드립니다.

감사합니다😆
````

## [#2750 [daehyun99] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2750)

### review_comment · alphaorderly · 2026-07-17T15:48:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3604423716
- ID: review_comment:3604423716
- 파일: find-minimum-in-rotated-sorted-array/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603963626

````text
`You must write an algorithm that runs in O(log n) time.`
이 문제는 Log N 시간복잡도로 답을 제한하고 있기 때문에 꼭 이진탐색으로 한번 시도해 보시길 바래요
````

### review_comment · alphaorderly · 2026-07-17T15:51:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3604440186
- ID: review_comment:3604440186
- 파일: maximum-depth-of-binary-tree/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603963886

````text
1번 답안 level order search 방식으로 하신거 같은데 deque 쓰시면 하나만 쓰셔도 구현 가능하세요!
````

### review_comment · alphaorderly · 2026-07-17T15:52:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3604445984
- ID: review_comment:3604445984
- 파일: merge-two-sorted-lists/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603964088

````text
이 문제는 노드를 다시 만들 필요 없이 재활용이 가능한 문제라 꼭 해보시면 좋을것 같네요
````

### review_comment · daehyun99 · 2026-07-18T07:29:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3607904392
- ID: review_comment:3607904392
- 파일: find-minimum-in-rotated-sorted-array/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603963626

````text
> `You must write an algorithm that runs in O(log n) time.` 이 문제는 Log N 시간복잡도로 답을 제한하고 있기 때문에 꼭 이진탐색으로 한번 시도해 보시길 바래요

헉 그렇군요. `O(N)`으로 풀어서 나름 뿌듯했는데 더 개선할 수 있었군요!
개선해봤습니다!

```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_idx = 0
        mid_idx = len(nums)//2
        right_idx = len(nums)-1

        while True:
            if right_idx - left_idx <= 1:
                if nums[left_idx] <= nums[right_idx]:
                    return nums[left_idx]
                else:
                    return nums[right_idx]
            elif nums[mid_idx] > nums[right_idx]:
                left_idx = mid_idx
                mid_idx = (left_idx + right_idx) // 2
                right_idx = right_idx
            else:
                left_idx = left_idx
                right_idx = mid_idx
                mid_idx = (left_idx + right_idx) // 2

```
````

### review_comment · daehyun99 · 2026-07-18T07:36:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3607918418
- ID: review_comment:3607918418
- 파일: maximum-depth-of-binary-tree/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603963886

````text
코멘트보고 다시 풀어봤는데, 하나만 있어도 되네요
리뷰 감사합니다!

```py
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        que = deque()

        if root is None:
            return 0
        que.append([root, 1])

        while len(que) > 0 :
            node, count = que.popleft()
            if node.left is not None:
                que.append([node.left, count+1])
            if node.right is not None:
                que.append([node.right, count+1])
        return count
```
````

### review_comment · daehyun99 · 2026-07-18T08:17:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3607979000
- ID: review_comment:3607979000
- 파일: merge-two-sorted-lists/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3603964088

````text
단순히 `ListNode(list2.val)` 처럼 넣던 값을 `list2`로 바꾸면 해결이 되네요.
리뷰 감사합니다!
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Space: O(N)
        # Time: O(N)
        dummy = ListNode(val=0, next=None)
        pointer = dummy
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        if list1 is not None:
            pointer.next = list1
        elif list2 is not None:
            pointer.next = list2

        return dummy.next
```
````

### issue_comment · JAEKWANG97 · 2026-07-18T09:08:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#issuecomment-5010698225
- ID: issue_comment:5010698225

````text
이번 주는 현재 제출하신 네 문제로 마무리하시는 걸까요!
````

### issue_comment · daehyun99 · 2026-07-18T10:23:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#issuecomment-5010905951
- ID: issue_comment:5010905951

````text
> 이번 주는 현재 제출하신 네 문제로 마무리하시는 걸까요!

@JAEKWANG97 
앗 넵! 마지막 문제는 2시간 정도 끙끙대며 풀다가 결국 못 풀어서 나중에 다시 풀어보려고 합니다!
리뷰 부탁드려요!
````

### review_comment · JAEKWANG97 · 2026-07-18T11:25:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3608251749
- ID: review_comment:3608251749
- 파일: word-search/daehyun99.py, 줄: 13, 원래 줄: 13

````text
  문자별 좌표를 미리 모아두는 흐름이 이해하기 좋았습니다! 저도 나중에 이렇게 접근해야겠어요 ㅎㅎ

```
pos = defaultdict(set)
pos[board[i][j]].add((i, j))
```

이렇게 바꾸면 조회 성능이 더 좋아질 것 같아요!
````

### review · JAEKWANG97 · 2026-07-18T11:26:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#pullrequestreview-4728390915
- ID: review:4728390915
- 리뷰 상태: APPROVED

````text
전체적으로 잘 봤습니다! 특히 Word Search를 문자별 좌표와 가능한 경로를 확장하는 방식으로 푼 점이 제가 사용한 DFS 방식과 달라서 흥미로웠습니다. 좌표 조회에 set을 활용할 수 있는 부분만 가볍게 코멘트 남겼습니다.

문제 풀이하시느라 수고하셨습니다!
````

### review_comment · daehyun99 · 2026-07-18T12:29:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2750#discussion_r3608359045
- ID: review_comment:3608359045
- 파일: word-search/daehyun99.py, 줄: 13, 원래 줄: 13
- 답글 대상: review_comment:3608251749

````text
오오.. dict() 내부에 `set`을 쓸 생각은 못 했었는데 감사합니다.
풀어보니 확실히 성능이 좋아지긴 하네요!
리뷰 감사합니다!

Runtime: 9700 ms -> 5667 ms
Memory: 405 MB -> 371 MB

```py
from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pos = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in word:
                    tmp = pos.get(board[i][j], set())
                    tmp.add((i, j))
                    pos[board[i][j]] = tmp

        paths = pos.get(word[0], [])
        paths = [[path] for path in paths]

        for w in word[1:]:
            temp = []

            while len(paths) > 0:
                path = paths.pop()
                i , j = path[-1]
                if ((i, j+1) in pos[w]) and ((i, j+1) not in path):
                    temp.append(path[:] + [(i, j+1)])
                if ((i, j-1) in pos[w]) and ((i, j-1) not in path):
                    temp.append(path[:] + [(i, j-1)])
                if ((i+1, j) in pos[w]) and ((i+1, j) not in path):
                    temp.append(path[:] + [(i+1, j)])
                if ((i-1, j) in pos[w]) and ((i-1, j) not in path):
                    temp.append(path[:] + [(i-1, j)])
            paths.extend(temp)
        for path in paths:
            if len(path) == len(word):
                print(path)
                return True
        return False 
```
````

## [#2751 [jaekwang97] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2751)

### review_comment · parkhojeong · 2026-07-18T13:34:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3608454616
- ID: review_comment:3608454616
- 파일: coin-change/jaekwang97.java, 줄: 18, 원래 줄: 18

````text
amount + 1 이  매직넘버라 선언해서 사용하시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:34:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3608455055
- ID: review_comment:3608455055
- 파일: find-minimum-in-rotated-sorted-array/jaekwang97.java, 줄: 9, 원래 줄: 9

````text
탐색 중간에 답인 경우 리턴이 가능해서 최적화 해보시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:35:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3608456041
- ID: review_comment:3608456041
- 파일: maximum-depth-of-binary-tree/jaekwang97.java, 줄: 23, 원래 줄: 23

````text
전역변수 없이 dfs 리턴 값을 사용해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:36:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3608457853
- ID: review_comment:3608457853
- 파일: merge-two-sorted-lists/jaekwang97.java, 줄: 27, 원래 줄: 27

````text
ListNode 를 새로 만들지 않고 기존 노드만을 이용해서 풀어보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:38:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3608459439
- ID: review_comment:3608459439
- 파일: word-search/jaekwang97.java, 줄: 1, 원래 줄: 1

````text
요거 돌려보니 runtime 50% 정도 나와서 최적화 좀 더 해보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-18T13:38:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#pullrequestreview-4728591916
- ID: review:4728591916
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

### review_comment · okyungjin · 2026-07-19T03:01:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3609676709
- ID: review_comment:3609676709
- 파일: word-search/jaekwang97.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608459439

````text
앞으로 풀이할 때 Beats도 같이 봐아겠네요. 백분위였군요👍
````

### review_comment · JAEKWANG97 · 2026-07-19T03:40:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2751#discussion_r3609731880
- ID: review_comment:3609731880
- 파일: coin-change/jaekwang97.java, 줄: 18, 원래 줄: 18
- 답글 대상: review_comment:3608454616

````text
감사합니다. 상수 처리하면 가독성이 더 좋아질 것 같네요!
````

## [#2752 [freemjstudio] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2752)

### review_comment · Chanz82 · 2026-07-18T09:59:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608135802
- ID: review_comment:3608135802
- 파일: merge-two-sorted-lists/freemjstudio.py, 줄: 22, 원래 줄: 22

````text
Dummy 노드를 통해서 풀 수 있군요, 깔끔한 풀이 인 것 같습니다. 저도 이렇게 풀어봐야겠네요!
list1 if list1 is not None else list2 는 list1 or list2로 변경 할 수 있을 것 같습니다.
````

### review_comment · Chanz82 · 2026-07-18T10:02:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608138993
- ID: review_comment:3608138993
- 파일: maximum-depth-of-binary-tree/freemjstudio.py, 줄: 1, 원래 줄: 1

````text
별도 함수를 구현하지 않고 maxDepth를 직접 활용하신게 인상적이네요! 풀이가 매우 직관적이고 깔끔합니다!
````

### review · Chanz82 · 2026-07-18T10:02:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#pullrequestreview-4728283512
- ID: review:4728283512
- 리뷰 상태: APPROVED

````text
4주차 고생 하셨습니다!!
````

### review_comment · freemjstudio · 2026-07-18T12:06:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608323597
- ID: review_comment:3608323597
- 파일: merge-two-sorted-lists/freemjstudio.py, 줄: 22, 원래 줄: 22
- 답글 대상: review_comment:3608135802

````text

list1 or list2 이렇게도 쓸 수 있군요! 감사합니다
````

### review_comment · freemjstudio · 2026-07-18T12:07:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608326771
- ID: review_comment:3608326771
- 파일: maximum-depth-of-binary-tree/freemjstudio.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3608138993

````text
넵넵 예전에 리트코드 풀이나 외국 유튜브 풀이들 보면 직접 사용하는 것도 많더라구요..! 
````

### review_comment · parkhojeong · 2026-07-18T12:24:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608353144
- ID: review_comment:3608353144
- 파일: coin-change/freemjstudio.py, 줄: 1, 원래 줄: 1

````text
가독성 좋게 잘 풀어주신 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T12:25:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608353946
- ID: review_comment:3608353946
- 파일: find-minimum-in-rotated-sorted-array/freemjstudio.py, 줄: 13, 원래 줄: 13

````text
탐색 도중 정답 케이스가 나오는 경우를 고려해서 최적화 해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T12:26:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3608355500
- ID: review_comment:3608355500
- 파일: merge-two-sorted-lists/freemjstudio.py, 줄: 9, 원래 줄: 9

````text
변수명으로 merged_list 사용하신 이유가 있을까요?
````

### review · parkhojeong · 2026-07-18T12:27:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#pullrequestreview-4728492353
- ID: review:4728492353
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 깔끔하게 풀어주셔서 읽기 좋았던 거 같습니다!
````

### review_comment · freemjstudio · 2026-07-19T03:31:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2752#discussion_r3609712212
- ID: review_comment:3609712212
- 파일: merge-two-sorted-lists/freemjstudio.py, 줄: 9, 원래 줄: 9
- 답글 대상: review_comment:3608355500

````text
두개의 리스트를 합친 리스트라는 의미에서 사용했습니당
````

## [#2753 [Chanz] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2753)

### review_comment · sonshn · 2026-07-18T10:22:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608167104
- ID: review_comment:3608167104
- 파일: maximum-depth-of-binary-tree/Chanz82.py, 줄: 25, 원래 줄: 25

````text
확실히 이 문제에서는 BFS보다는 DFS가 더 좋은 풀이 같네요!
````

### review_comment · sonshn · 2026-07-18T10:23:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608167793
- ID: review_comment:3608167793
- 파일: merge-two-sorted-lists/Chanz82.py, 줄: 33, 원래 줄: 33

````text
저는 재귀로 풀었는데, 이렇게도 풀 수 있겠네요!
````

### review_comment · sonshn · 2026-07-18T10:24:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608168529
- ID: review_comment:3608168529
- 파일: word-search/Chanz82.py, 줄: 32, 원래 줄: 32

````text
이 문제를 DFS로 풀 수 있다는 것은 전혀 생각하지 못했네요...! 감사합니다!
````

### review · sonshn · 2026-07-18T10:24:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#pullrequestreview-4728314380
- ID: review:4728314380
- 리뷰 상태: APPROVED

````text
이번 주도 고생 많으셨습니다!
````

### review_comment · parkhojeong · 2026-07-18T12:57:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608403600
- ID: review_comment:3608403600
- 파일: find-minimum-in-rotated-sorted-array/Chanz82.py, 줄: 10, 원래 줄: 10

````text
탐색 중간에 정답으로 판별이 가능한 경우가 있는데 최적화 시도해보셔도 좋을 거 같습니다
````

### review_comment · parkhojeong · 2026-07-18T13:03:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608410895
- ID: review_comment:3608410895
- 파일: maximum-depth-of-binary-tree/Chanz82.py, 줄: 24, 원래 줄: 24

````text
개인적으로 외부 변수 max_depth, nonlocal 때문에 그런지 코드 따라가기가 약간 어려웠던거 같습니다. dfs 함수의 리턴 값을 활용하시면 가독성을 많이 올리실 수 있을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:07:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608417660
- ID: review_comment:3608417660
- 파일: merge-two-sorted-lists/Chanz82.py, 줄: 30, 원래 줄: 30

````text
cursor에 어떤 값이 담기고 list2와 어떻게 비교되어서 동작하는건지 따라가기가 조금 어려운 거 같습니다. 스왑 로직도 있고 해서 그런 거 같은데 조금 더 단순하게 풀어보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:09:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3608420103
- ID: review_comment:3608420103
- 파일: word-search/Chanz82.py, 줄: 26, 원래 줄: 26

````text
요거 돌려보면 runtime이 50% 정도 나오는데 최적화 시도해보셔도 좋을 거 같습니다. 불필요한 탐색을 안하도록 해보시면 될 거 같아요.
````

### review · parkhojeong · 2026-07-18T13:11:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#pullrequestreview-4728542936
- ID: review:4728542936
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

### review_comment · Chanz82 · 2026-07-20T18:51:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3616763950
- ID: review_comment:3616763950
- 파일: merge-two-sorted-lists/Chanz82.py, 줄: 30, 원래 줄: 30
- 답글 대상: review_comment:3608417660

````text
맞습니다. 저도 구현하면서 스왑하고 이런게 헷갈리더라고요.
다른 분들 풀이를 보니, 제가 다음 문장을 오해 한 것 같습니다. Dummy 노드도 만들면 안되는 것으로요.
The list should be made by splicing together the nodes of the first two lists.
````

### review_comment · Chanz82 · 2026-07-20T20:16:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2753#discussion_r3617273099
- ID: review_comment:3617273099
- 파일: find-minimum-in-rotated-sorted-array/Chanz82.py, 줄: 10, 원래 줄: 10
- 답글 대상: review_comment:3608403600

````text
정렬 된 경우인 경우 바로 반환하도록 했습니다. Leetcode에서는 기존 코드도 0ms라서.. 직접 성능 비교는 어렵군요..! 의도하신 바가 이게 맞을지 궁금하긴 합니다..ㅎㅎ

```
if nums[left] < nums[right]:
    return nums[left]
```
````

## [#2754 [sonshn] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2754)

### review_comment · parkhojeong · 2026-07-18T12:20:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2754#discussion_r3608346597
- ID: review_comment:3608346597
- 파일: merge-two-sorted-lists/sonshn.java, 줄: 1, 원래 줄: 1

````text
재귀로 푸셨군요. 엄청 간결하고 직관적이어서 좋은 거 같습니다.
````

### review · parkhojeong · 2026-07-18T12:21:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2754#pullrequestreview-4728486733
- ID: review:4728486733
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다. 

PR 설명에 언급하신 4주차 문제 외에 다른 풀이도 file changed에 포함되어 있는 것 같습니다. 정리 부탁드리곘습니다.
````

### issue_comment · sonshn · 2026-07-18T13:09:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2754#issuecomment-5011375333
- ID: issue_comment:5011375333

````text
> 수고하셨습니다.
> 
> PR 설명에 언급하신 4주차 문제 외에 다른 풀이도 file changed에 포함되어 있는 것 같습니다. 정리 부탁드리곘습니다.

@parkhojeong fork한 저장소에서 fork 동기화 작업 진행해서 이번 주차에 해당하는 file 들만 이력에 반영되도록 했습니다.
````

## [#2755 [Yiseull] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2755)

### review_comment · parkhojeong · 2026-07-18T13:25:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#discussion_r3608442608
- ID: review_comment:3608442608
- 파일: find-minimum-in-rotated-sorted-array/Yiseull.java, 줄: None, 원래 줄: 22

````text
탐색 중간에 답을 판별할 수 있어서 최적화 시도해보셔도 좋을 거 같습니다.

추가로 `if (nums[right] <= nums[left] && nums[left] <= nums[mid]) {` 는 조금 더 간소화 가능하니 생각해보셔도 좋을 듯 합니다.
````

### review · sangbeenmoon · 2026-07-18T13:27:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#pullrequestreview-4728583401
- ID: review:4728583401
- 리뷰 상태: APPROVED

````text
깔끔하게 잘 풀어주셨네요! 이번 한주도 고생 많으셨습니다 👍 
````

### review · parkhojeong · 2026-07-18T13:28:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#pullrequestreview-4728580570
- ID: review:4728580570
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 깔끔하게 풀어주신 거 같네요.
````

### review_comment · parkhojeong · 2026-07-18T13:50:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#discussion_r3608478405
- ID: review_comment:3608478405
- 파일: coin-change/Yiseull.java, 줄: 21, 원래 줄: 19

````text
`dp[amount] > amount`가 실제로 amount + 1 인지를 비교하는 거고 amount + 1 이 매직넘버로 쓰이고 있어서 변수로 선언해서 쓰시면 더 좋을 거 같습니다
````

### review_comment · parkhojeong · 2026-07-18T13:51:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#discussion_r3608479451
- ID: review_comment:3608479451
- 파일: coin-change/Yiseull.java, 줄: None, 원래 줄: 12

````text
amount 보다 큰 coin 처리은 안쓰도록 해주면 최적화 가능할 거 같습니다
````

### review_comment · Yiseull · 2026-07-18T14:42:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#discussion_r3608553933
- ID: review_comment:3608553933
- 파일: find-minimum-in-rotated-sorted-array/Yiseull.java, 줄: None, 원래 줄: 22
- 답글 대상: review_comment:3608442608

````text
left, right를 비교해서 답을 바로 판별할 수 있네요! 말씀해주신 방향으로 최적화했습니다. 더 좋은 방향 제안해주셔서 감사합니다!👍
````

### review_comment · Yiseull · 2026-07-18T14:58:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2755#discussion_r3608577868
- ID: review_comment:3608577868
- 파일: coin-change/Yiseull.java, 줄: 21, 원래 줄: 19
- 답글 대상: review_comment:3608478405

````text
매직넘버로 인해 풀이 가독성이 더 올라갔네요 감사합니다~!
````

## [#2756 [sangbeenmoon] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2756)

### review_comment · parkhojeong · 2026-07-18T13:31:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2756#discussion_r3608450381
- ID: review_comment:3608450381
- 파일: find-minimum-in-rotated-sorted-array/sangbeenmoon.py, 줄: 34, 원래 줄: 34

````text
이 부분 mid 할당은 중복으로 보여서 지워도 될 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:40:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2756#discussion_r3608462802
- ID: review_comment:3608462802
- 파일: word-search/sangbeenmoon.py, 줄: 1, 원래 줄: 1

````text
요거 돌려보니 3000ms 정도 나오는데 최적화 좀더 해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-18T13:42:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2756#discussion_r3608465512
- ID: review_comment:3608465512
- 파일: find-minimum-in-rotated-sorted-array/sangbeenmoon.py, 줄: 39, 원래 줄: 39

````text
탐색 중간에 정답인 경우 미리 리턴해보도록 해보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-18T13:42:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2756#pullrequestreview-4728588254
- ID: review:4728588254
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2757 [togo26] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2757)

### review_comment · parkhojeong · 2026-07-18T16:33:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2757#discussion_r3608746593
- ID: review_comment:3608746593
- 파일: merge-two-sorted-lists/togo26.js, 줄: 45, 원래 줄: 45

````text
dummy 류의 노드를 두면 훨씬 간결하게 풀 수 있어서 이렇게도 풀어보시는걸 추천드립니다.
다른 방법으로는 재귀로 풀면 아주 직관적으로도 풀 수 있어서 이 방법도 풀어보시면 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-18T16:35:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2757#pullrequestreview-4728873655
- ID: review:4728873655
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 한 문제라 아쉽지만 다음 주 토고님의 풀이 기다리겠습니다!
````

### review · parkhojeong · 2026-07-18T16:37:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2757#pullrequestreview-4728879824
- ID: review:4728879824
- 리뷰 상태: CHANGES_REQUESTED

````text
커밋 로그에 관계 없는 풀이들이 있어서 정리 한 번 부탁드립니다. 
````

### review · alphaorderly · 2026-07-19T03:01:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2757#pullrequestreview-4729752647
- ID: review:4729752647
- 리뷰 상태: APPROVED

````text
깔끔하게 잘 해결하신거 같아요!
````

### issue_comment · togo26 · 2026-07-20T11:34:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2757#issuecomment-5021774881
- ID: issue_comment:5021774881

````text
@parkhojeong 커밋 정리하였습니다. 감사합니다.
````

### review · okyungjin · 2026-07-20T13:44:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2757#pullrequestreview-4735478503
- ID: review:4735478503
- 리뷰 상태: APPROVED

````text
lgtm! 

(승인을 추가로 해도 merge block 상태군요)
````

## [#2758 [alphaorderly] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2758)

### review_comment · alphaorderly · 2026-07-19T03:05:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3609680958
- ID: review_comment:3609680958
- 파일: implement-trie-prefix-tree/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
Trie를 압축을 할수 있을거 같은데 좀 연구해볼 필요가 있겠네요
````

### issue_comment · alphaorderly · 2026-07-19T14:11:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#issuecomment-5016034189
- ID: issue_comment:5016034189

````text
코드 내용에 대한 적절한 평가 혹은 질문 혹은 보완점 리뷰 부탁드리겠습니다.
````

### issue_comment · DaleSeo · 2026-07-19T23:54:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#issuecomment-5017845656
- ID: issue_comment:5017845656

````text
병합을 위해 승인 처리합니다.

@DaleStudy 승인
````

### review · DaleSeo · 2026-07-20T00:00:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#pullrequestreview-4731713009
- ID: review:4731713009
- 리뷰 상태: APPROVED

````text
병합을 위해 승인합니다. 수고하셨습니다!
````

### issue_comment · DaleSeo · 2026-07-20T00:05:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#issuecomment-5017866759
- ID: issue_comment:5017866759

````text
@alphaorderly 앗, 죄송합니다. 답안 제출을 4주차 PR을 병합하다가 함께 일괄 병합이 되어버렸네요 😅 앞으로 이런 문제가 없도록 자동화 도구를 개선하겠습니다.
````

### issue_comment · alphaorderly · 2026-07-20T00:15:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#issuecomment-5017889901
- ID: issue_comment:5017889901

````text
네~!
````

### review_comment · parkhojeong · 2026-07-22T17:30:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3632383013
- ID: review_comment:3632383013
- 파일: encode-and-decode-strings/alphaorderly.py, 줄: 32, 원래 줄: 32

````text
각 문자열 길이가 0~200 이라 고정 길이 방식도 고려해볼 수 있을 것 같습니다. 데이터 패턴에 따라 1글자가 많으면 작성해주신 방식이 유리할 거 같고 3글자가 많으면 고정길이가 유리해서 trade-off는 있을 거 같아요. 
파싱하는 로직에서는 고정 자리수를 쓰는게 더 간단해서 좀 더 유리할 것 같네요.
````

### review_comment · parkhojeong · 2026-07-24T05:54:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643219287
- ID: review_comment:3643219287
- 파일: word-break/alphaorderly.py, 줄: 102, 원래 줄: 102

````text
target의 타입이 잘못된 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-24T06:01:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643255521
- ID: review_comment:3643255521
- 파일: word-break/alphaorderly.py, 줄: 125, 원래 줄: 125

````text
ans에는 무슨 값이 담기는 걸까요?
````

### review_comment · parkhojeong · 2026-07-24T06:11:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643298147
- ID: review_comment:3643298147
- 파일: word-break/alphaorderly.py, 줄: 68, 원래 줄: 68

````text
S, W 변수는 의미가 잘 안 드러나고 PEP 8 컨벤션이랑 달라서 가독성을 약간 떨어지게 하는 거 같습니다.

PEP 8 컨벤션에 맞추어 lowercase 를 사용하시는건 어떨까요? https://peps.python.org/pep-0008/#function-and-variable-names
````

### review_comment · parkhojeong · 2026-07-24T06:21:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643339626
- ID: review_comment:3643339626
- 파일: word-break/alphaorderly.py, 줄: 23, 원래 줄: 23

````text
@lru_cache의 maxSize 기본값이 128인데 이것도 고려하셨을까요?
````

### review · parkhojeong · 2026-07-24T06:34:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#pullrequestreview-4757000453
- ID: review:4757000453
- 리뷰 상태: COMMENTED

````text
수고하셨습니다.
````

### review_comment · alphaorderly · 2026-07-24T06:35:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643398838
- ID: review_comment:3643398838
- 파일: encode-and-decode-strings/alphaorderly.py, 줄: 32, 원래 줄: 32
- 답글 대상: review_comment:3632383013

````text
맞아요, 고정길이 코드 하신거 보니까 훨씬 깔끔하긴 하더라구요!!
````

### review_comment · alphaorderly · 2026-07-24T06:36:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643404538
- ID: review_comment:3643404538
- 파일: word-break/alphaorderly.py, 줄: 68, 원래 줄: 68
- 답글 대상: review_comment:3643298147

````text
아하! 저는 neetcodeIO 를 예전에 엄청 오래 보면서 공부를 했었어서 배열의 길이를 상수 취급해서 대문자로 적는거에 너무 익숙해져서 그렇긴 하네요
한번 고려해보겠습니다!
````

### review_comment · alphaorderly · 2026-07-24T06:41:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643425043
- ID: review_comment:3643425043
- 파일: word-break/alphaorderly.py, 줄: 125, 원래 줄: 125
- 답글 대상: review_comment:3643255521

````text
검색 대상인 target 문자열에서 start부터 보면서 trie에 들어간 문자열중에
start에서 시작하는 문자열중 prefix가 정확하게 일치하는 문자열에 한해
채웠다고 가정하고 다 채운 이후의 인덱스가 어디인지를 저장해요!

예를 들어 wordDict에 abc, teg가 있고
target이 strategy 이며 start가 4인 경우

teg가 4번 인덱스부터 시작할때 일치하기 때문에
4(t) 5(e) 6(g) 를 넘기고 그 다음 인덱스인 7이 들어갑니다.
````

### review_comment · alphaorderly · 2026-07-24T06:43:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643431768
- ID: review_comment:3643431768
- 파일: word-break/alphaorderly.py, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3643339626

````text
넹 맞아요, 문자열의 길이상 괜찮을것 같다는 판단이였어요
````

### review_comment · alphaorderly · 2026-07-24T06:48:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3643461219
- ID: review_comment:3643461219
- 파일: word-break/alphaorderly.py, 줄: 102, 원래 줄: 102
- 답글 대상: review_comment:3643219287

````text
그렇네요, 파이썬 타입 힌트는 강하게 묶여있지 않아서 실수를 자주 하게 되네요
````

### review_comment · okyungjin · 2026-07-25T12:15:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3650148244
- ID: review_comment:3650148244
- 파일: word-break/alphaorderly.py, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3643339626

````text
> 넹 맞아요, 문자열의 길이상 괜찮을것 같다는 판단이였어요

@alphaorderly 128개 외에 밀려나는 캐시는 재계산하면 된다로 해석하면 될까요?
저는 cache 데코레이터 사용했는데 성능 차이가 어느정도일까요

많이 배워갑니다👍
````

### review_comment · okyungjin · 2026-07-25T12:17:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2758#discussion_r3650150082
- ID: review_comment:3650150082
- 파일: implement-trie-prefix-tree/alphaorderly.py, 줄: 38, 원래 줄: 38

````text
이런 방법이...!
````

## [#2759 [okyungjin] WEEK 04 Solutions (최적화)](https://github.com/DaleStudy/leetcode-study/pull/2759)

### issue_comment · okyungjin · 2026-07-19T09:18:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#issuecomment-5015175550
- ID: issue_comment:5015175550

````text
@parkhojeong @alphaorderly 코치님들 안녕하세요. 다른 분들 PR 내용 참고해서 최적화 로직을 적용했는데 리뷰 부탁드려도 될까요? 
````

### issue_comment · alphaorderly · 2026-07-19T09:45:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#issuecomment-5015252628
- ID: issue_comment:5015252628

````text
사실 너무 꽤나 깔끔하게 잘 하셔서 더이상 말이 필요 없을 정도네요
잘해주셨습니다!
````

### review_comment · parkhojeong · 2026-07-19T10:18:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610359133
- ID: review_comment:3610359133
- 파일: coin-change/okyungjin.py, 줄: 27, 원래 줄: 27

````text
`if coin <= cur_amount` 로직을 포문 안에서 계속 돌게 해주신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-07-19T10:20:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610362958
- ID: review_comment:3610362958
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 30, 원래 줄: 30

````text
다른 파일들 포함해서 주석을 많이 달아주셨는데 코드만으로 충분한 것들이 많은 것 같아요! 

코드를 통해서 최대한 의도를 드러내고 꼭 필요한 상황에만 적어주시는 편이 좋을 거 같아요. 주석도 같이 읽어야 해서 인지적 부하도 올라가고 가독성이 떨어지는 부분도 생기기도 해서요. 특히 코드와 주석이 정확히 일치하지 않는 경우가 생기지 않도록 조심해야 하는 거 같아요.


````

### review_comment · parkhojeong · 2026-07-19T10:23:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610366859
- ID: review_comment:3610366859
- 파일: word-search/okyungjin.py, 줄: 32, 원래 줄: 32

````text
인풋의 패턴을 파악해서 최적화 한다는 점에선 좋은 접근인 거 같습니다. 다만 첫글자와 마지막 글자의 빈도만 비교해서 최적화하는건 특수한 케이스만 커버가 될 거 같아요. 리트코드 채점 데이터셋엔 이 경우가 들어간 거 같더라구요.
````

### review_comment · parkhojeong · 2026-07-19T10:35:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610381515
- ID: review_comment:3610381515
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 64, 원래 줄: 64

````text
가독성면에선 재귀가 가장 괜찮아서 재귀로도 풀어보시면 좋을 거 같아요. 
````

### review · parkhojeong · 2026-07-19T10:40:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#pullrequestreview-4730573684
- ID: review:4730573684
- 리뷰 상태: COMMENTED

````text
최적화 시도 해보신거 멋지네요! 몇 가지 커멘트 남겼습니다.
````

### review_comment · okyungjin · 2026-07-19T12:11:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610520675
- ID: review_comment:3610520675
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 30, 원래 줄: 30
- 답글 대상: review_comment:3610362958

````text
의견 감사합니다!
````

### review_comment · okyungjin · 2026-07-19T12:12:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610522747
- ID: review_comment:3610522747
- 파일: word-search/okyungjin.py, 줄: 32, 원래 줄: 32
- 답글 대상: review_comment:3610366859

````text
오 넵넵 감사합니다 : ) 
````

### review_comment · okyungjin · 2026-07-19T12:20:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610535353
- ID: review_comment:3610535353
- 파일: coin-change/okyungjin.py, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3610359133

````text
원래는 coins를 정렬한 뒤 if coin > cur_amount: break 조기 종료 조건을 사용했었는데요. 코드를 더 간결하게 다듬기 위해 정렬을 없애고 부등호를 뒤집는 방향으로 수정했습니다.

coins 배열 길이가 최대 12라 break 유무에 따른 성능 차이가 크지 않을 것 같아 로직을 간소화해 보았습니다!
````

### review_comment · okyungjin · 2026-07-19T12:22:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610537116
- ID: review_comment:3610537116
- 파일: coin-change/okyungjin.py, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3610359133

````text
사담이지만 그 아래 라인에 있는 min 함수를 제거하니 성능이 훨씬 좋아지더라구요
```py
min_coins[cur_amount] = min(min_coins[cur_amount], min_coins[cur_amount - coin] + 1)
```

if문 형태로 필요할 때만 할당하도록 하니 런타임 백분위가 30% 올라갔던 것 같습니다.
````

### review_comment · alphaorderly · 2026-07-19T12:23:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610539402
- ID: review_comment:3610539402
- 파일: coin-change/okyungjin.py, 줄: 27, 원래 줄: 27
- 답글 대상: review_comment:3610359133

````text
맞아요, max나 min으로 하는게 코드상 보기 좋고 쓰기도 편한게 맞는데
성능은 은근히 차이가 나더라구요
몇몇 문제는 100~200ms 가량 차이나는것도 본적 있어요
````

### review_comment · okyungjin · 2026-07-19T12:28:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#discussion_r3610546577
- ID: review_comment:3610546577
- 파일: maximum-depth-of-binary-tree/okyungjin.py, 줄: 64, 원래 줄: 64
- 답글 대상: review_comment:3610381515

````text
f0245ab0f70ef6dbffc6a07a5264a50343784b85 추가했습니다~ 깔끔하네요.
````

### issue_comment · okyungjin · 2026-07-19T13:35:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2759#issuecomment-5015921163
- ID: issue_comment:5015921163

````text
리뷰 정성스럽게 남겨주셔서 정말 감사드립니다 : ) 시간이 다 되어서 PR은 머지해두도록 하겠습니다!
````

## [#2760 [j2h30728] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2760)

### review_comment · parkhojeong · 2026-07-19T14:55:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2760#discussion_r3610780276
- ID: review_comment:3610780276
- 파일: find-minimum-in-rotated-sorted-array/j2h30728.ts, 줄: 2, 원래 줄: 2

````text
변수 명으로 n을 사용하신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-07-19T14:57:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2760#discussion_r3610782892
- ID: review_comment:3610782892
- 파일: coin-change/j2h30728.ts, 줄: 13, 원래 줄: 13

````text
`amount + 1`, `> amount ` 이 연관된 로직인데 드러나지 않아서 amount + 1 을 변수로 선언해서 사용하시면 좋을 거 같아요.
````

### review_comment · parkhojeong · 2026-07-19T15:00:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2760#discussion_r3610787855
- ID: review_comment:3610787855
- 파일: find-minimum-in-rotated-sorted-array/j2h30728.ts, 줄: 9, 원래 줄: 9

````text
이진탐색인데 last가 고정되어 있네요. 잘 이해가 안되서 그런데 이 부분 설명해주실 수 있을까요?
````

### review · parkhojeong · 2026-07-19T15:02:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2760#pullrequestreview-4730953911
- ID: review:4730953911
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 남은 문제인 word search도 풀어보시면 좋을 거 같아요.
````

## [#2762 [dolphinflow86] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2762)

### issue_comment · okyungjin · 2026-07-20T13:43:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#issuecomment-5022925549
- ID: issue_comment:5022925549

````text
@dolphinflow86 안녕하세요~ 상태 In Review로 설정되어 있는데 의도하신게 맞는지 확인 부탁드립니다!
````

### issue_comment · dolphinflow86 · 2026-07-20T14:16:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#issuecomment-5023257384
- ID: issue_comment:5023257384

````text
> @dolphinflow86 안녕하세요~ 상태 In Review로 설정되어 있는데 의도하신게 맞는지 확인 부탁드립니다!

안녕하세요! In Review로 된 것은 의도가 맞습니다. 예전에 스터디 가이드쪽에서 미리 PR을 올리고 리뷰를 길게 받으면서 가는게 좋다고 하신걸 본적이 있어서요. In Review로 바꾸는 것은 제가 잘못 봤을수도 있습니다 -> Solving으로 바꿔놓았습니다~
````

### review_comment · alphaorderly · 2026-07-20T14:20:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3614979909
- ID: review_comment:3614979909
- 파일: best-time-to-buy-and-sell-stock/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
깔끔하게 잘 해결해 주셨네요!
best time to buy and sell stock, 즉 해당 문제는
뒤에 로마 숫자를 붙혀서 1, 2, 3, 4, 5 총 다섯종류가 있는데요
dp 연습하기에 정말 괜찮은 문제라고 생각해서 
[2번문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
II는 한번 풀어보시길 추천드려요!
````

### review_comment · dolphinflow86 · 2026-07-20T14:25:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3615017082
- ID: review_comment:3615017082
- 파일: best-time-to-buy-and-sell-stock/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614979909

````text
오! 네 문제 추천 감사합니다! 한번 풀어볼게요 👍 
````

### review_comment · parkhojeong · 2026-07-24T10:43:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3644772289
- ID: review_comment:3644772289
- 파일: best-time-to-buy-and-sell-stock/dolphinflow86.py, 줄: 11, 원래 줄: 11

````text
사소하지만 더 최적화 할 수 있는 부분은  min, max 일 거 같아요. 고민해보셔도 좋을 거 같습니다! 
````

### review_comment · okyungjin · 2026-07-25T10:29:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650030332
- ID: review_comment:3650030332
- 파일: best-time-to-buy-and-sell-stock/dolphinflow86.py, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3644772289

````text
같은 의견입니다! min, max가 생각보다 비용이 크더라구요 
````

### review_comment · okyungjin · 2026-07-25T10:38:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650039604
- ID: review_comment:3650039604
- 파일: encode-and-decode-strings/dolphinflow86.py, 줄: 9, 원래 줄: 9

````text
저도 이번에 공부하면서 배운 내용인데, 아래와 같이 작성하면 최적화가 가능한 것 같습니다.

1. 리스트 대신 제너레이터 표현식 사용해서 메모리 최적화
2. 문자열 `+=` 연산으로 매번 새로운 문자열 생성하는대신, join으로 문자열 한번에 합치기


```py
def encode(self, strs: list[str]) -> str:
    return "".join(f"{len(s)}%{s}" for s in strs)
```

혹은 

```py
def encode(self, strs: list[str]) -> str:
    parts = (f"{len(s)}%{s}" for s in strs)
    return "".join(parts)
```
````

### review_comment · okyungjin · 2026-07-25T10:38:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650040284
- ID: review_comment:3650040284
- 파일: encode-and-decode-strings/dolphinflow86.py, 줄: 19, 원래 줄: 19

````text
개인적인 의견이지만 `%` 같은 구분자는 상수처리하면 가독성이 좋을 것 같습니다!
````

### review_comment · okyungjin · 2026-07-25T10:41:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650043136
- ID: review_comment:3650043136
- 파일: word-break/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
BFS나 Trie 자료구조 사용한 풀이법도 적용해보면 좋을 것 같습니다!
````

### review · okyungjin · 2026-07-25T10:44:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#pullrequestreview-4779110296
- ID: review:4779110296
- 리뷰 상태: APPROVED

````text
이번 주도 고생하셨습니다! 다음 주도 파이팅하세요 🔥
````

### review_comment · dolphinflow86 · 2026-07-25T11:04:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650069822
- ID: review_comment:3650069822
- 파일: best-time-to-buy-and-sell-stock/dolphinflow86.py, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3644772289

````text
두분 의견 감사합니다! if문으로 인라인 처리하면 함수 호출 오버헤드 등을 줄일 수 있겠네요. 
````

### review_comment · okyungjin · 2026-07-25T11:21:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650095682
- ID: review_comment:3650095682
- 파일: group-anagrams/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
리뷰 누락이 있어서 추가로 남깁니다.

1. `str`은 파이썬 클래스와 혼동이 있을 수 있어서 가급적이면 변수명으로 쓰지 않는 것이 좋을 것 같습니다.
2. 저도 리뷰 받았던 내용인데, sorted의 정렬 대신 다르게 구현하여 시간 복잡도를 개선해보면 좋을 것 같습니다.

````

### review_comment · dolphinflow86 · 2026-07-25T11:28:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650102124
- ID: review_comment:3650102124
- 파일: encode-and-decode-strings/dolphinflow86.py, 줄: 9, 원래 줄: 9
- 답글 대상: review_comment:3650039604

````text
저도 블로그로 정리하다 join으로 개선하는 부분 발견했는데, 짚어주셔서 감사합니다. 파이썬은 문자열이 immutable이라 조심해야겠더라고요. join이 재너레이터 표현식 방식으로 동작하는것도 잘 알아갑니다! 감사합니다.
````

### review_comment · dolphinflow86 · 2026-07-25T11:31:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650104195
- ID: review_comment:3650104195
- 파일: word-break/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3650043136

````text
찾아보니 작년에 BFS로 풀었더라고요? 이번에는 그 방법이 안떠올라서 조금 난감했네요 ㅎㅎ  BFS나 Trie 방법도 고려해보겠습니다!
````

### review_comment · dolphinflow86 · 2026-07-25T11:33:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2762#discussion_r3650106496
- ID: review_comment:3650106496
- 파일: group-anagrams/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3650095682

````text
c++ 습관이 자꾸 나오네요 ㅎㅎ str은 사용하지 않아야겠습니다. 두번째 방법도 한번 생각해볼게요! 꼼꼼하게 리뷰해주셔서 감사합니다 🙏
````

## [#2763 [okyungjin] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2763)

### review_comment · alphaorderly · 2026-07-20T14:02:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3614854775
- ID: review_comment:3614854775
- 파일: group-anagrams/okyungjin.py, 줄: 1, 원래 줄: 1

````text
sorted를 쓰는것도 좋지만, 정렬 자체가 N Log N 시간복잡도를 가져서
해시 함수를 구현해서 O(N) 시간복잡도로 구현하는것도 좋은것 같더라구요!

- 지금 봇에 댓글 달면 사라지는 버그 있어서 혹시 몰라 새로 답니다!

````

### review_comment · alphaorderly · 2026-07-20T14:03:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3614857676
- ID: review_comment:3614857676
- 파일: implement-trie-prefix-tree/okyungjin.py, 줄: 1, 원래 줄: 1

````text
문제의 목표에는 꽤나 잘 맞도록 잘 구현해 주셨는데요!
Trie 자료구조가 추구하는 방향과는 전혀 맞지 않는것이 너무 아쉽네요 ㅠㅠ
[링크](https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie)

해당 자료구조는 tree의 형태에 좀 더 가까운 자료구조고, 지금처럼 모든 prefix의 경우를 저장하시지 않으시더라도 최적의 시간으로 구할수 있게 해줘서 좋아요!
꼭!! 구현 해보시길 바랍니다!
````

### review_comment · okyungjin · 2026-07-20T14:04:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3614866581
- ID: review_comment:3614866581
- 파일: group-anagrams/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614854775

````text
> sorted를 쓰는것도 좋지만, 정렬 자체가 N Log N 시간복잡도를 가져서 해시 함수를 구현해서 O(N) 시간복잡도로 구현하는것도 좋은것 같더라구요!
> 
> * 지금 봇에 댓글 달면 사라지는 버그 있어서 혹시 몰라 새로 답니다!

@alphaorderly 감사합니다 ㅎㅎ 문제 쫙 풀고 최적화 해보도록 하겠습니다 👍👍👍

````

### review_comment · okyungjin · 2026-07-20T14:04:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3614868590
- ID: review_comment:3614868590
- 파일: implement-trie-prefix-tree/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614857676

````text
> 문제의 목표에는 꽤나 잘 맞도록 잘 구현해 주셨는데요! Trie 자료구조가 추구하는 방향과는 전혀 맞지 않는것이 너무 아쉽네요 ㅠㅠ [링크](https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%9D%BC%EC%9D%B4-Trie)
> 
> 해당 자료구조는 tree의 형태에 좀 더 가까운 자료구조고, 지금처럼 모든 prefix의 경우를 저장하시지 않으시더라도 최적의 시간으로 구할수 있게 해줘서 좋아요! 꼭!! 구현 해보시길 바랍니다!

@alphaorderly 오 맞아요... 사실 문제를 풀고나서 위키 문서를 보게 되었는데 최초에 생각한 구현이랑 방향성이 많이 다르더라구요. 내일 저녁 먹고 이어서 풀어보겠습니다 감사합니다 🔥


````

### review_comment · alphaorderly · 2026-07-20T14:19:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3614968469
- ID: review_comment:3614968469
- 파일: best-time-to-buy-and-sell-stock/okyungjin.py, 줄: 1, 원래 줄: 1

````text
엄청 깔끔하게 잘 해결하셨네요!
best time to buy and sell stock, 즉 해당 문제는
뒤에 로마 숫자를 붙혀서 1, 2, 3, 4, 5 총 다섯종류가 있는데요
dp 연습하기에 정말 괜찮은 문제라고 생각해서 
[2번문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
II는 한번 풀어보시길 추천드려요!

````

### review_comment · daehyun99 · 2026-07-25T07:30:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3649798630
- ID: review_comment:3649798630
- 파일: encode-and-decode-strings/okyungjin.py, 줄: 1, 원래 줄: 1

````text
덕분에 `find(찾을 문자열, 시작 인덱스)`과 `typing.Final`을 알아가네요!
````

### review_comment · daehyun99 · 2026-07-25T07:43:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3649815869
- ID: review_comment:3649815869
- 파일: implement-trie-prefix-tree/okyungjin.py, 줄: 1, 원래 줄: 1

````text
두 개의 `set()`에다가 트리의 구조 정보를 저장하는 방식도 있군요!

구현하신 클래스가 공간 복잡도는 높게 나오지만, 조회 성능이 중요한 문제에서는 좋을 것 같네요!
````

### review_comment · okyungjin · 2026-07-25T10:54:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3650058784
- ID: review_comment:3650058784
- 파일: implement-trie-prefix-tree/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614857676

````text
52ec55332b7d69c7c8d02a091f728faf3e30eaaf 커밋에서 적용했습니다.
wordBreak에서 이 자료구조를 활용할 수 있더라구요. 피드백 감사합니다!
````

### review_comment · okyungjin · 2026-07-25T11:58:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3650129876
- ID: review_comment:3650129876
- 파일: group-anagrams/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614854775

````text
84fbf28b29551187db6d7cc4890d7e02fe1db5ec

카운터 리스트를 튜플로 변환한 다음에 키로 사용하도록 최적화했습니다.
알고달레 찾아보니 Counter + fronzenset 방식도 사용이 가능하네요. 피드백 감사합니다!
````

### review_comment · daehyun99 · 2026-07-25T12:04:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3650136480
- ID: review_comment:3650136480
- 파일: word-break/okyungjin.py, 줄: 1, 원래 줄: 1

````text
와우 다양한 방법으로 풀이를 해주셨네요.

`trie` 자료구조를 사용하는 방법은 저도 문제를 풀면서 잠깐 생각했다가, 안될 것 같아서 다른 방법을 생각했었는데 dp와 함께 풀 수 있었군요! 많이 배워갑니다!

`cache` 또는 `failed`, `visited`, `dp`로 이미 수행한 결과를 기록하여, 중복 계산을 없애는 방법도 엄청 좋은 것 같네요!
````

### review · daehyun99 · 2026-07-25T12:12:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#pullrequestreview-4778836113
- ID: review:4778836113
- 리뷰 상태: APPROVED

````text
안녕하세요! 이번 주 리뷰어 김대현입니다.

한 주 동안 고생하셨습니다!! 많이 배워갑니다!
````

### review_comment · okyungjin · 2026-07-25T12:50:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2763#discussion_r3650188834
- ID: review_comment:3650188834
- 파일: implement-trie-prefix-tree/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3649815869

````text
직관적으로 떠오른 풀이인데 문제의 요구사항이랑은 멀더라구요. 
이전 풀이에는 복잡도를 안 적었는데 조회가 더 빠르네요! 리뷰 감사합니다~!
````

## [#2764 [daehyun99] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2764)

### review_comment · alphaorderly · 2026-07-20T14:04:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#discussion_r3614864149
- ID: review_comment:3614864149
- 파일: best-time-to-buy-and-sell-stock/daehyun99.py, 줄: 1, 원래 줄: 1

````text
꽤 깔끔하게 잘 해결하셨네요!
````

### review_comment · alphaorderly · 2026-07-20T14:20:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#discussion_r3614977230
- ID: review_comment:3614977230
- 파일: best-time-to-buy-and-sell-stock/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614864149

````text
그리고
best time to buy and sell stock, 즉 해당 문제는
뒤에 로마 숫자를 붙혀서 1, 2, 3, 4, 5 총 다섯종류가 있는데요
dp 연습하기에 정말 괜찮은 문제라고 생각해서 
[2번문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
II는 한번 풀어보시길 추천드려요!
````

### review_comment · yuseok89 · 2026-07-25T13:50:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#discussion_r3650270093
- ID: review_comment:3650270093
- 파일: group-anagrams/daehyun99.py, 줄: 1, 원래 줄: 1

````text
개수를 다 세지 않고도 푸는 방법이 있습니다.
개수를 세는 방법에서는 Counter + hash 를 활용하면 코드가 좀 더 간결하게 하실 수 있을 것 같으니 참고하세요 ~
````

### review_comment · yuseok89 · 2026-07-25T13:53:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#discussion_r3650274209
- ID: review_comment:3650274209
- 파일: implement-trie-prefix-tree/daehyun99.py, 줄: 1, 원래 줄: 1

````text
저는 별도의 TrieNode 라는 별도 클래스를 생성해서 풀었는데, 이렇게도 풀리네요 !
````

### review_comment · yuseok89 · 2026-07-25T14:02:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#discussion_r3650288580
- ID: review_comment:3650288580
- 파일: word-break/daehyun99.py, 줄: 1, 원래 줄: 1

````text
BFS 로도 접근 가능하네요 !
다만, wordDict 의 전처리를 통해서, 매번 wordDict 전체를 순회하지 않도록 하면 좀 더 효율화 할 수 있을 것도 같습니다.
````

### review · yuseok89 · 2026-07-25T14:03:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#pullrequestreview-4779353771
- ID: review:4779353771
- 리뷰 상태: APPROVED

````text
5주차 고생많으셨습니다 !
몇 가지 코멘트를 달아놓긴 했는데, 참고만 해주시면 되겠습니다 !
````

### review_comment · daehyun99 · 2026-07-25T17:57:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2764#discussion_r3650697668
- ID: review_comment:3650697668
- 파일: implement-trie-prefix-tree/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3650274209

````text
저도 풀고 다른 분들 풀이 보니깐 별도의 클래스를 많이 만들더라고요. 클래스를 만드는 게 더 깔끔해서 좋은 것 같아요!
````

## [#2765 [yuseok89] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2765)

### review_comment · alphaorderly · 2026-07-20T14:14:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3614938443
- ID: review_comment:3614938443
- 파일: best-time-to-buy-and-sell-stock/yuseok89.py, 줄: 1, 원래 줄: 1

````text
prices[1:]
와 같이 하시면 보기엔 정말 좋은데 말이죠
파이썬 슬라이싱은 말 그대로 배열을 하나 더 만들어서 사용하는거라 이 간단한 과정에만 O(N)의 시간이 소요되어요!

[파이썬 시간복잡도](https://wiki.python.org/moin/TimeComplexity)

Get slice 부분을 보시면 O(k) 라는것을 알수 있죠

그래서 좀 귀찮으시더라도

`range(1, len(prices))`

를 쓰시는게 나으실거에요!

물론 지금같은 경우는 전체 시간복잡도가 O(N)이고 저 연산은 단 한번 실행되니 시간복잡도 자체에는 큰 영향을 주진 않겠지만

for loop 안에서 써야하는 일이 생긴다면 좀 다르겠죠

word-break 문제에서 이부분을 잘 생각해 다른방식으로 최적화 할수 있는 부분이 있으니 한번 생각하면서 해보시면 좋을것 같네요!
````

### review_comment · alphaorderly · 2026-07-20T14:20:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3614974977
- ID: review_comment:3614974977
- 파일: best-time-to-buy-and-sell-stock/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614938443

````text
그리고
best time to buy and sell stock, 즉 해당 문제는
뒤에 로마 숫자를 붙혀서 1, 2, 3, 4, 5 총 다섯종류가 있는데요
dp 연습하기에 정말 괜찮은 문제라고 생각해서 
[2번문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
II는 한번 풀어보시길 추천드려요!
````

### review_comment · yuseok89 · 2026-07-21T14:38:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3623072076
- ID: review_comment:3623072076
- 파일: best-time-to-buy-and-sell-stock/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3614938443

````text
감사합니다. 많이 배웁니다.
로직상 제거해도 괜찮고, range 보다 미묘하게 슬라이스 제거한 것이 빨라, 슬라이스 제거 버전으로 수정했습니다.
````

### review_comment · parkhojeong · 2026-07-22T16:39:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3632048048
- ID: review_comment:3632048048
- 파일: best-time-to-buy-and-sell-stock/yuseok89.py, 줄: None, 원래 줄: 10

````text
max, min를 사용하면 오버헤드가 있어서 더 최적화 한다면 직접 비교해서 업데이트 하는 식으로 해볼 수 있을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-22T17:02:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3632208008
- ID: review_comment:3632208008
- 파일: word-break/yuseok89.py, 줄: None, 원래 줄: 22

````text
v는 무슨 약어일까요?
````

### review_comment · parkhojeong · 2026-07-22T17:08:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3632246479
- ID: review_comment:3632246479
- 파일: word-break/yuseok89.py, 줄: 1, 원래 줄: 1

````text
문제의 핵심적인 부분만 딱 캐치해서 푸신 거 같습니다. 아이디어는 어떻게 얻으셨는지 궁금하네요. 비슷하게 접근해서 푸셨던 문제나 경험이 있으실까요?
````

### review · parkhojeong · 2026-07-22T17:15:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#pullrequestreview-4756602397
- ID: review:4756602397
- 리뷰 상태: COMMENTED

````text
수고하셨습니다. 
````

### review_comment · parkhojeong · 2026-07-22T17:15:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3632288632
- ID: review_comment:3632288632
- 파일: word-break/yuseok89.py, 줄: None, 원래 줄: 2

````text
공란이라 요건 지우거나 표기 부탁드립니다.
````

### review · parkhojeong · 2026-07-22T17:16:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#pullrequestreview-4756890945
- ID: review:4756890945
- 리뷰 상태: CHANGES_REQUESTED

````text
복잡도 표기 공란과 이번 주와 관계없는 커밋 로그들은 정리 부탁드립니다.
````

### review_comment · parkhojeong · 2026-07-24T05:17:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3643074239
- ID: review_comment:3643074239
- 파일: word-break/yuseok89.py, 줄: None, 원래 줄: 29

````text
`min_len~max_len` 범위라 존재하지 않는 len도 탐색하네요.
````

### review_comment · yuseok89 · 2026-07-24T14:44:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3646142621
- ID: review_comment:3646142621
- 파일: best-time-to-buy-and-sell-stock/yuseok89.py, 줄: None, 원래 줄: 10
- 답글 대상: review_comment:3632048048

````text
그렇네요.
그렇게 더 최적화 해 볼 수 있네요.
감사합니다. 반영했습니다.
````

### review_comment · yuseok89 · 2026-07-24T14:45:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3646146002
- ID: review_comment:3646146002
- 파일: word-break/yuseok89.py, 줄: None, 원래 줄: 22
- 답글 대상: review_comment:3632208008

````text
visited 입니다.. ㅎ 너무 줄였네요..
````

### review_comment · yuseok89 · 2026-07-24T14:46:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3646154279
- ID: review_comment:3646154279
- 파일: word-break/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3632246479

````text
글세요.. 굳이 따지자면 제가 있는 회사에 내부 테스트가 있는데 스타일이 비슷한 문제인 것 같긴 합니다..
````

### review_comment · yuseok89 · 2026-07-24T14:47:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3646166904
- ID: review_comment:3646166904
- 파일: word-break/yuseok89.py, 줄: None, 원래 줄: 2
- 답글 대상: review_comment:3632288632

````text
복잡도 계산이 어려워 비워놨는데, 지우는 것이 좋겠네요.
커밋 로그도 정리했습니다.
감사합니다.
````

### review_comment · yuseok89 · 2026-07-24T14:56:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3646237812
- ID: review_comment:3646237812
- 파일: word-break/yuseok89.py, 줄: None, 원래 줄: 29
- 답글 대상: review_comment:3643074239

````text
여기서 min, max 가 별로네요. 저격되는 테스트 케이스가 만들어질 수도 있을 로직이네요.
수정했습니다.
감사합니다.
````

### review_comment · parkhojeong · 2026-07-25T04:12:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2765#discussion_r3649386876
- ID: review_comment:3649386876
- 파일: implement-trie-prefix-tree/yuseok89.py, 줄: 5, 원래 줄: 5

````text
요건 타입 힌트를 명확하게 지정해주면 더 좋을 거 같습니다. 
````

## [#2766 [essaysir] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2766)

### review_comment · JeonJe · 2026-07-25T02:39:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3649171666
- ID: review_comment:3649171666
- 파일: group-anagrams/essaysir.java, 줄: 9, 원래 줄: 9

````text
루프 안에서 i 자체를 쓰지 않고 strs[i]로 값만 참조할 때 가독성을 향상시키기 위해서 enhanced for-loop을 써보는 것도 좋을 것 같습니다!


````

### review_comment · JeonJe · 2026-07-25T02:43:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3649180527
- ID: review_comment:3649180527
- 파일: encode-and-decode-strings/essaysir.java, 줄: 6, 원래 줄: 6

````text
'#'이 encode/decode 양쪽에 매직 리터럴로 중복되기 때문에, private static final char DELIMITER = '#';로 추출해서 두 메서드의 인코딩 계약이 한 곳에서 관리되면 나중에 구분자 바꿀 때 한쪽만 수정하는 실수를 예방할 수 있을 것 같아요!
````

### review_comment · JeonJe · 2026-07-25T02:49:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3649198612
- ID: review_comment:3649198612
- 파일: best-time-to-buy-and-sell-stock/essaysir.java, 줄: 4, 원래 줄: 4

````text
최소값 대신 최소 인덱스를 들고 가는 접근도 깔끔하네요. 
인덱스로 잡으면 나중에 '며칠에 샀는지'까지 확장할 때 바로 쓸 수 있는 여지가 있어 좋네요!
````

### review_comment · parkhojeong · 2026-07-25T04:13:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3649387877
- ID: review_comment:3649387877
- 파일: best-time-to-buy-and-sell-stock/essaysir.java, 줄: 5, 원래 줄: 5

````text
lt는 무슨 약어일까요? 추측하기 어려운 약어로 보여서 의미를 담는 변수명을 사용하시면 좋을 거 같아요.
````

### review_comment · essaysir · 2026-07-25T05:30:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3649550337
- ID: review_comment:3649550337
- 파일: best-time-to-buy-and-sell-stock/essaysir.java, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3649198612

````text
좋은 의견들 너무 감사합니다! 앞으로, 코딩 테스트 하면서 적용해볼 수 있도록 노력하도록 하겠습니다.
````

### review_comment · parkhojeong · 2026-07-25T16:24:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3650522496
- ID: review_comment:3650522496
- 파일: best-time-to-buy-and-sell-stock/essaysir.java, 줄: 15, 원래 줄: 15

````text
최대 이익을 나타내는 값이어서 그 의미를 나타내는 변수명을 쓰는건 어떨까요?
````

### review_comment · parkhojeong · 2026-07-25T16:27:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#discussion_r3650527714
- ID: review_comment:3650527714
- 파일: encode-and-decode-strings/essaysir.java, 줄: 14, 원래 줄: 14

````text
구분자 없이도 가능한데 풀어보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-25T16:29:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#pullrequestreview-4778375180
- ID: review:4778375180
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 몇가지 커멘트 남겼습니다.
````

### issue_comment · DaleSeo · 2026-07-27T02:37:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#issuecomment-5086731253
- ID: issue_comment:5086731253

````text
@essaysir 님, Week 설정 누락되지 않도록 주의 부탁드리겠습니다. 이번 PR은 제가 대신 해드리도록 할께요.

<img width="1794" height="862" alt="2026-07-26 at 22 37 15" src="https://github.com/user-attachments/assets/8353e6b8-1e8e-48fc-ba4f-33eadcc94a87" />

````

### issue_comment · essaysir · 2026-07-27T02:47:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2766#issuecomment-5086774179
- ID: issue_comment:5086774179

````text
넵! 죄송합니다! 다음에는 누락하지 않도록 하겠습니다.
````

## [#2767 [JeonJe] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2767)

### review_comment · parkhojeong · 2026-07-25T15:55:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2767#discussion_r3650463902
- ID: review_comment:3650463902
- 파일: best-time-to-buy-and-sell-stock/JeonJe.java, 줄: 14, 원래 줄: 14

````text
sellDay 변수명 직관적이어서 좋은 거 같네요
````

### review_comment · parkhojeong · 2026-07-25T16:07:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2767#discussion_r3650486209
- ID: review_comment:3650486209
- 파일: word-break/JeonJe.java, 줄: 26, 원래 줄: 26

````text
앞에서부터 누적해서 푸는 분들이 많았는데 반대로 푸셔서 흥미로웠습니다. 앞에서부터 푸는 것도 고려하셨을 거 같은데 뒤에서부터 푸신 이유가 있으실까요?
````

### review_comment · parkhojeong · 2026-07-25T16:14:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2767#discussion_r3650507682
- ID: review_comment:3650507682
- 파일: implement-trie-prefix-tree/JeonJe.java, 줄: 23, 원래 줄: 23

````text
children[c - 'a'] 는 TrieNode의 세부 구현에 가까운데 Trie에  c - 'a'가 여러 코드에 걸쳐 나타나고 있는 것 같습니다. TrieNode에서 node.getChildren(c) 와 같은 방식으로 제공하는 건 어떨까요?
````

### review · parkhojeong · 2026-07-25T16:20:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2767#pullrequestreview-4779518310
- ID: review:4779518310
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 몇가지 커멘트 남겨보았습니다.
````

### review_comment · JeonJe · 2026-07-25T23:16:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2767#discussion_r3651255138
- ID: review_comment:3651255138
- 파일: implement-trie-prefix-tree/JeonJe.java, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3650507682

````text
미처 생각 못했던 부분인데, 함수로 감싸면 가독성도 높히고 실수도 줄일 수 있을 것 같네요.
감사합니다!
````

### review_comment · JeonJe · 2026-07-25T23:27:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2767#discussion_r3651270872
- ID: review_comment:3651270872
- 파일: word-break/JeonJe.java, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:3650486209

````text
재귀 형식의 탑다운 방식으로 먼저 풀다보니, 바텀업 방식도 자연스럽게 뒤에서 앞 방향으로 생각하게 되었습니다.
다른 분들께서는 어떻게 풀이하셨는지 한 번 살펴봐야겠네요. 
리뷰 감사합니다!!
````

## [#2768 [parkhojeong] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2768)

### review_comment · alphaorderly · 2026-07-23T01:07:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3634926835
- ID: review_comment:3634926835
- 파일: encode-and-decode-strings/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
숫자길이를 고정값으로 하니까 파싱이 확실히 간단하고 쉬워지네요!
배워갑니다.
````

### review_comment · alphaorderly · 2026-07-23T01:08:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3634930239
- ID: review_comment:3634930239
- 파일: implement-trie-prefix-tree/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
추가 Node없이 할수 있다면 그렇게 하는게 더 좋지 않을까 싶어요!
````

### review_comment · alphaorderly · 2026-07-23T01:19:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3634962444
- ID: review_comment:3634962444
- 파일: word-break/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
이 풀이 n이랑 m이 뭔지는 몰라도 
1. dfs에 cache 안되어 있음
2. dfs 내부에 슬라이싱 사용
때문에라도 O(m*n) 은 진짜 아닐거에요

다만 이거 trie 이용해서 비슷한 수준까지 최적화는 가능하세요!
````

### review_comment · alphaorderly · 2026-07-23T01:29:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3634993005
- ID: review_comment:3634993005
- 파일: word-break/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3634962444

````text
<img width="885" height="456" alt="Image" src="https://github.com/user-attachments/assets/ed92d8ac-f8c6-4b03-a250-fc413b3d96b4" />

그리고 중간에 split을 하신것 때문에 이런 반례에 대해서는 해결 불가능하실거에요
````

### review_comment · DaleSeo · 2026-07-23T01:45:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635037214
- ID: review_comment:3635037214
- 파일: word-break/parkhojeong.py, 줄: None, 원래 줄: 20

````text
`str.split()`은 왼쪽부터 겹치지 않게 등장 위치를 제거하는데, 이 동작이 실제 유효한 분할 경계와 항상 일치할까요? 외부 루프 없이 `dfs`만으로 전체 문자열을 검사하면 어떤 차이가 생기는지도 함께 고민해보시면 좋을 것 같습니다.
````

### review_comment · DaleSeo · 2026-07-23T01:46:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635039778
- ID: review_comment:3635039778
- 파일: word-break/parkhojeong.py, 줄: None, 원래 줄: 38

````text
같은 `i`에 대한 결과를 재활용할 방법이 있을지 생각해보시면 좋겠습니다.
````

### review_comment · DaleSeo · 2026-07-23T01:48:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635051513
- ID: review_comment:3635051513
- 파일: best-time-to-buy-and-sell-stock/parkhojeong.py, 줄: None, 원래 줄: 4

````text
여기에 저장되는 값은 가격이 아니라 이익이 아닌가요?
````

### review_comment · DaleSeo · 2026-07-23T01:50:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635056140
- ID: review_comment:3635056140
- 파일: implement-trie-prefix-tree/parkhojeong.py, 줄: None, 원래 줄: 3

````text
얘는 저장만 되고 쓰지는 않는 것 같네요?
````

### review · DaleSeo · 2026-07-23T01:51:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#pullrequestreview-4760134772
- ID: review:4760134772
- 리뷰 상태: APPROVED

````text
5문제 모두 푸시느라 고생 많으셨습니다! 생각해보실 만한 질문을 남겼습니다.
````

### review_comment · parkhojeong · 2026-07-23T03:08:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635297927
- ID: review_comment:3635297927
- 파일: word-break/parkhojeong.py, 줄: None, 원래 줄: 20
- 답글 대상: review_comment:3635037214

````text
리뷰 감사합니다. 테스트 케이스에는 없지만 split을 사용하면 놓치는 케이스들이 생기겠네요. 루프 없이 dfs만으로 처리하도록 처리해보았습니다! https://github.com/DaleStudy/leetcode-study/pull/2768/commits/8facb2ecafa6f7580e260f37308a2e5c95d4b332
````

### review_comment · parkhojeong · 2026-07-23T03:15:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635321367
- ID: review_comment:3635321367
- 파일: implement-trie-prefix-tree/parkhojeong.py, 줄: None, 원래 줄: 3
- 답글 대상: review_comment:3635056140

````text
지워주었습니다. https://github.com/DaleStudy/leetcode-study/pull/2768/commits/50caae08077b5cb2ab8206d18beeb89e533017dc
````

### review_comment · parkhojeong · 2026-07-23T03:17:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635330627
- ID: review_comment:3635330627
- 파일: best-time-to-buy-and-sell-stock/parkhojeong.py, 줄: None, 원래 줄: 4
- 답글 대상: review_comment:3635051513

````text
맞습니다. max_profit으로 변경해주었습니다. https://github.com/DaleStudy/leetcode-study/pull/2768/commits/78d8ad559ad1f3f8c616ed8feaf88737f854ba3b
````

### review_comment · parkhojeong · 2026-07-23T03:17:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3635333978
- ID: review_comment:3635333978
- 파일: word-break/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3634962444

````text
리뷰 감사합니다. 그러네요. 말씀하신 것처럼 놓치는 케이스가 있어서 split 사용하지 않고 다른 방식으로 풀어보았습니다. https://github.com/DaleStudy/leetcode-study/pull/2768/commits/8facb2ecafa6f7580e260f37308a2e5c95d4b332
````

### review_comment · parkhojeong · 2026-07-24T02:17:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2768#discussion_r3642537513
- ID: review_comment:3642537513
- 파일: implement-trie-prefix-tree/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3634930239

````text
추가 Node 없이 한다는게 무슨 말씀일까요?
````

## [#2769 [DaleSeo] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2769)

### review_comment · parkhojeong · 2026-07-24T04:41:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2769#discussion_r3642946260
- ID: review_comment:3642946260
- 파일: encode-and-decode-strings/DaleSeo.rs, 줄: 8, 원래 줄: 8

````text
`Follow-up question`까지 풀어보시면 좋을 거 같습니다!

`Follow up: Could you write a generalized algorithm to work on any possible set of characters?`
````

### review · parkhojeong · 2026-07-24T04:42:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2769#pullrequestreview-4770152526
- ID: review:4770152526
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

### review_comment · dahyeong-yun · 2026-07-25T09:46:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2769#discussion_r3649984812
- ID: review_comment:3649984812
- 파일: encode-and-decode-strings/DaleSeo.rs, 줄: 3, 원래 줄: 3

````text
- 이미 merge 되었군요. rust 코드를 처음 봐서 생소하긴 했는데, 이해하면 굉장히 직관적인 코드네요 👍🏼 
- 나중에 러스트 코드 리뷰 할 저를 위해 남겨 둡니다.
  - `return` 키워드를 명시하지 않아도 마지막 줄이 return 됨. (세미콜론이 있으면 void 라 함)
  - 타입 추론이 가능한 경우, 생략 가능
  - `mut` 는 변경 가능을 의미.
````

## [#2770 [dahyeong-yun] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2770)

### review_comment · parkhojeong · 2026-07-25T17:43:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2770#discussion_r3650666810
- ID: review_comment:3650666810
- 파일: word-break/dahyeong-yun.java, 줄: 33, 원래 줄: 33

````text
삼중 if 라서  살짝 리팩토링하면 가독성 챙겨볼 수 있을 거 같습니다.
```suggestion
            if(!s.startsWith(word, index) || len < index + wordLength) continue;
         
            if(dfs(index + wordLength)) return true; 
```
````

### review_comment · parkhojeong · 2026-07-25T17:48:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2770#discussion_r3650680435
- ID: review_comment:3650680435
- 파일: best-time-to-buy-and-sell-stock/dahyeong-yun.java, 줄: 14, 원래 줄: 14

````text
python의 경우엔 min, max가 오버헤드가 있어서 성능상 최적화 여지가 있는데 java는 min, max가 단순 삼항 연산자로 구현되어 있어서 큰 차이는 없는 거 같네요. 

java max 구현체 링크입니다.
https://github.com/openjdk/jdk/blob/3412d4c0dd5250f14cc6fe594355bdf2ff976417/src/java.base/share/classes/java/lang/Math.java#L2023
````

### review · parkhojeong · 2026-07-25T17:49:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2770#pullrequestreview-4779783860
- ID: review:4779783860
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

## [#2771 [seueooo] WEEK 04 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2771)

### review_comment · parkhojeong · 2026-07-24T03:09:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2771#discussion_r3642689153
- ID: review_comment:3642689153
- 파일: coin-change/seueooo.js, 줄: 1, 원래 줄: 1

````text
요건 돌려보면 runtime이 5% 정도 나오는데 최적화 시도해보시면 좋을 거 같습니다. 
````

### review_comment · parkhojeong · 2026-07-24T03:13:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2771#discussion_r3642700368
- ID: review_comment:3642700368
- 파일: merge-two-sorted-lists/seueooo.js, 줄: 1, 원래 줄: 1

````text
재귀로 풀어주셨네요. 재귀 아닌 방식으로 풀어보셔도 재밌으실 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-24T03:14:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2771#discussion_r3642704901
- ID: review_comment:3642704901
- 파일: word-search/seueooo.js, 줄: 1, 원래 줄: 1

````text
더 최적화 한다면 어떤 부분이 있을지 한 번 고민해보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-24T03:16:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2771#pullrequestreview-4769837484
- ID: review:4769837484
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

### review · parkhojeong · 2026-07-24T03:19:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2771#pullrequestreview-4769872358
- ID: review:4769872358
- 리뷰 상태: CHANGES_REQUESTED

````text
풀이와 관계없는 커밋 로그 정리 부탁드립니다.
````

## [#2772 [Chanz] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2772)

### review_comment · ICE0208 · 2026-07-25T11:15:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#discussion_r3650089075
- ID: review_comment:3650089075
- 파일: group-anagrams/Chanz82.py, 줄: 9, 원래 줄: 9

````text
문자열이 `lowercase English letters`로 제한되어 있으므로, 정렬 방식 대신 알파벳 빈도 배열을 키로 사용하면 시간 복잡도를 더 줄일 수 있을 것 같습니다!
````

### review_comment · ICE0208 · 2026-07-25T11:16:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#discussion_r3650089760
- ID: review_comment:3650089760
- 파일: implement-trie-prefix-tree/Chanz82.py, 줄: 16, 원래 줄: 16

````text
별도의 `Node` 클래스를 만들지 않고, 중첩된 `dict` 구조와 `'#'` 키를 활용해 단어의 끝을 판별한 점이 인상적이었습니다!
````

### review · ICE0208 · 2026-07-25T11:20:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#pullrequestreview-4779174242
- ID: review:4779174242
- 리뷰 상태: APPROVED

````text
전체적으로 코드가 깔끔하게 작성되어 있어 흐름을 빠르게 이해할 수 있었습니다. 몇 가지 코멘트 남겨두었습니다. 이번 주도 고생 많으셨습니다! 🙌
````

### review_comment · parkhojeong · 2026-07-25T17:12:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#discussion_r3650613235
- ID: review_comment:3650613235
- 파일: best-time-to-buy-and-sell-stock/Chanz82.py, 줄: 17, 원래 줄: 17

````text
단순히 price를 순회하는 인덱스에 sell이라는 변수를 붙이는게 어색한 거 같아요. 특히 첫번째 if 문에서 buy = sell이 잘 이해가 잘 되지는 않네요. 
````

### review_comment · parkhojeong · 2026-07-25T17:14:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#discussion_r3650615940
- ID: review_comment:3650615940
- 파일: implement-trie-prefix-tree/Chanz82.py, 줄: 26, 원래 줄: 26

````text
단어의 끝을 나타내는데 변수명으로 #을 쓰신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-07-25T17:19:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#discussion_r3650624209
- ID: review_comment:3650624209
- 파일: implement-trie-prefix-tree/Chanz82.py, 줄: 12, 원래 줄: 12

````text
Trie에 모든 구현을 하셨는데 주요 로직은 작은 헬퍼 함수들을 사용해보시면 코드의 의도를 더 드러내실 수 있을 거 같습니다. key를 구하는 getKey 같은게 있을 거 같아요.

별도로 노드에 대한 클래스를 만들어서 역할을 나누는 형태로도 구현해보시면 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-25T17:30:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#pullrequestreview-4778405708
- ID: review:4778405708
- 리뷰 상태: COMMENTED

````text
수고하셨습니다. 고민해보실만한 커멘트 몇 개 남겼습니다.
````

### review_comment · parkhojeong · 2026-07-25T17:35:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#discussion_r3650649715
- ID: review_comment:3650649715
- 파일: word-break/Chanz82.py, 줄: 18, 원래 줄: 18

````text
visited는 실패한 start 값들이 담기는 변수로 보이는데 이렇게 네이밍 하신 이유가 있을까요? 변수명만 봐선 방문했던 노드들이 담긴다는 의미로 읽히는데 add의 위치가 왜 리턴쪽에 있는지 생각이 들었네요.
````

### review · parkhojeong · 2026-07-25T17:38:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#pullrequestreview-4779762273
- ID: review:4779762273
- 리뷰 상태: CHANGES_REQUESTED

````text
머지되기 전에 체크하면 좋을 거 같아 request-changed로 남겨놓습니다.
````

### review · alphaorderly · 2026-07-27T04:55:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2772#pullrequestreview-4783714639
- ID: review:4783714639
- 리뷰 상태: APPROVED

````text
고생하셨습니다!
````

## [#2773 [freemjstudio] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2773)

### review_comment · dolphinflow86 · 2026-07-25T03:14:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2773#discussion_r3649252930
- ID: review_comment:3649252930
- 파일: best-time-to-buy-and-sell-stock/freemjstudio.py, 줄: 21, 원래 줄: 21

````text
타임아웃 과정부터 성공한 솔루션까지 같이 보여주셔서 비교하기 좋았습니다. 
시간/공간 복잡도 분석도 주석으로 같이 해주시면 더 좋을 것 같아요!
수고하셨습니다.
````

### review_comment · parkhojeong · 2026-07-25T16:53:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2773#discussion_r3650580232
- ID: review_comment:3650580232
- 파일: best-time-to-buy-and-sell-stock/freemjstudio.py, 줄: 18, 원래 줄: 18

````text
i가 0인 경우 불필요한 재계산이 되서 1부터 시작하면 명확할 거 같습니다.
````

### review · parkhojeong · 2026-07-25T16:56:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2773#pullrequestreview-4779687360
- ID: review:4779687360
- 리뷰 상태: CHANGES_REQUESTED

````text
프로젝트 주차 설정과 pr 체크리스트도 확인 부탁드립니다.
````

### review_comment · freemjstudio · 2026-07-26T05:10:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2773#discussion_r3651822500
- ID: review_comment:3651822500
- 파일: best-time-to-buy-and-sell-stock/freemjstudio.py, 줄: 21, 원래 줄: 21
- 답글 대상: review_comment:3649252930

````text
앞으로는 시간/공간복잡도 분석도 추가해보겠습니다
감사합니다 !! 
````

## [#2774 [ICE0208] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2774)

### review_comment · dahyeong-yun · 2026-07-25T09:16:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3649961105
- ID: review_comment:3649961105
- 파일: group-anagrams/ICE0208.java, 줄: 19, 원래 줄: 19

````text
저는 문자열 정렬로 해결 했는데, 빈도 배열이면 시간복잡도 상 더 유리하겠네요!
````

### review_comment · njngwn · 2026-07-25T09:33:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3649973894
- ID: review_comment:3649973894
- 파일: encode-and-decode-strings/ICE0208.py, 줄: 4, 원래 줄: 4

````text
어떤 문제는 자바로 푸시고, 어떤 문제는 파이썬으로 푸셨네요. 같이 연습을 하시는 이유가 따로 있나요?? 
````

### review_comment · njngwn · 2026-07-25T09:37:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3649976912
- ID: review_comment:3649976912
- 파일: encode-and-decode-strings/ICE0208.py, 줄: 1, 원래 줄: 1

````text
파이썬 3.9+ 부터는 선언을 안해도 list[str]을 쓸 수 있다고 합니다!
````

### review_comment · njngwn · 2026-07-25T09:38:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3649977576
- ID: review_comment:3649977576
- 파일: best-time-to-buy-and-sell-stock/ICE0208.java, 줄: 8, 원래 줄: 8

````text
주석도 설명이 아주 잘되어있고, 코드도 정말 깔끔하네요. 수고하셨습니다!!
````

### review_comment · njngwn · 2026-07-25T09:40:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3649979361
- ID: review_comment:3649979361
- 파일: group-anagrams/ICE0208.java, 줄: 27, 원래 줄: 27

````text
코드 수를 줄일 수 있어서 좋네요. 배워갑니다!
````

### issue_comment · njngwn · 2026-07-25T09:47:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#issuecomment-5078033521
- ID: issue_comment:5078033521

````text
전체적으로 따로 코멘트를 달 게 없다고 느낄 정도로 잘 쓰여진 코드네요. 깔끔하고 주석도 설명이 잘 되어있어서 이해하기 좋았습니다. 수고 많으셨습니다!!
````

### review_comment · dahyeong-yun · 2026-07-25T09:48:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3649987051
- ID: review_comment:3649987051
- 파일: word-break/ICE0208.py, 줄: 8, 원래 줄: 8

````text
굉장히 편리한 기능이네요. 중복이 바로 처리 되네요 👍🏼 
````

### review_comment · ICE0208 · 2026-07-25T10:48:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3650051462
- ID: review_comment:3650051462
- 파일: encode-and-decode-strings/ICE0208.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3649976912

````text
앗 그렇군요
알려주셔서 감사합니다!
````

### review_comment · ICE0208 · 2026-07-25T10:51:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3650055865
- ID: review_comment:3650055865
- 파일: encode-and-decode-strings/ICE0208.py, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3649973894

````text
원래 알고리즘 문제 풀이는 파이썬으로만 했는데, 최근 스프링 백엔드 쪽을 공부하고 있어서 자바와 좀 더 친해지고자 이번 알고리즘 문제는 자바로 풀고 있습니다...만! 이번 주는 시간이 없어 벼락치기로 문제를 풀다 보니 어쩔 수 없이 파이썬으로 빠르게 풀고 제출했습니다. ㅎㅎ
````

### issue_comment · ICE0208 · 2026-07-25T10:54:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#issuecomment-5078223117
- ID: issue_comment:5078223117

````text
@njngwn 꼼꼼한 코드리뷰 감사합니다☺️
````

### review · dahyeong-yun · 2026-07-25T14:53:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#pullrequestreview-4779038348
- ID: review:4779038348
- 리뷰 상태: COMMENTED

````text
자바 코드, 파이썬 코드가 같이 있어서 비교해서 보기 좋았습니다. 주석도 적절히 있고 코드 개행도 신경써서 나눠주셔서 보기 편했네요. 잘 보고 갑니다 👍🏼 
````

### review_comment · ICE0208 · 2026-07-25T15:01:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2774#discussion_r3650377782
- ID: review_comment:3650377782
- 파일: word-break/ICE0208.py, 줄: 8, 원래 줄: 8
- 답글 대상: review_comment:3649987051

````text
맞아요! 메모이제이션을 자동으로 처리해줘서 알고리즘 문제 풀이할 때 유용하더라고요 ☺️
````

## [#2775 [njngwn] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2775)

### review · sangbeenmoon · 2026-07-25T12:58:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2775#pullrequestreview-4779290507
- ID: review:4779290507
- 리뷰 상태: APPROVED

````text
고생하셨습니다!

`cache` , `extend()` 등의 라이브러리를 활용해서 간결하게 풀어내신 점이 인상적이네요! 👍 
````

## [#2776 [sangbeenmoon] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2776)

### review_comment · alphaorderly · 2026-07-25T14:21:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650314923
- ID: review_comment:3650314923
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 51

````text
            if sorted_target in d:
                d[sorted_target].append(target)
            else:
                d[sorted_target] = [target]
````

### review_comment · alphaorderly · 2026-07-25T14:22:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650315408
- ID: review_comment:3650315408
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 51
- 답글 대상: review_comment:3650314923

````text
이렇게 하시는게 훨씬 나을거에요, 지금 코드에서 copy는 의미를 모르겠어요
````

### review_comment · alphaorderly · 2026-07-25T14:23:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650316673
- ID: review_comment:3650316673
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 57

````text
list(d.values())

이렇게 리스트로 형변환 하시면 answer 없이 바로 가능하세요
````

### review_comment · parkhojeong · 2026-07-25T16:31:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650533420
- ID: review_comment:3650533420
- 파일: implement-trie-prefix-tree/sangbeenmoon.py, 줄: None, 원래 줄: 4

````text
d가 무슨 약어일까요?
````

### review_comment · parkhojeong · 2026-07-25T16:32:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650534785
- ID: review_comment:3650534785
- 파일: word-break/sangbeenmoon.py, 줄: None, 원래 줄: 41

````text
의미에 맞는 네이밍을 해주시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-25T16:33:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650537708
- ID: review_comment:3650537708
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 51

````text
copy 쓰신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-07-25T16:44:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650561317
- ID: review_comment:3650561317
- 파일: implement-trie-prefix-tree/sangbeenmoon.py, 줄: None, 원래 줄: 29

````text
[1:]이 O(n)이라 현재 insert, search에서 탐색 성능이 좋지 않은 거 같습니다. [1:]을 사용하지 않고 구현해보시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-25T16:45:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3650563286
- ID: review_comment:3650563286
- 파일: implement-trie-prefix-tree/sangbeenmoon.py, 줄: None, 원래 줄: 57

````text
Trie에는 구현이 없고 TrieNode에 모든 구현을 하신 이유가 있을까요?
````

### review · parkhojeong · 2026-07-25T16:48:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#pullrequestreview-4779622489
- ID: review:4779622489
- 리뷰 상태: COMMENTED

````text
수고하셨습니다. 
````

### review · parkhojeong · 2026-07-26T05:25:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#pullrequestreview-4781050967
- ID: review:4781050967
- 리뷰 상태: CHANGES_REQUESTED

````text
이번 주차 풀이와 관계 없는 커밋 로그는 정리 부탁드리고 리뷰 커멘트도 확인 부탁드립니다.
````

### review_comment · sangbeenmoon · 2026-07-26T07:25:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652002473
- ID: review_comment:3652002473
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 51
- 답글 대상: review_comment:3650314923

````text
네 깔끔하네요 ㅎㅎ 수정했습니다.
````

### review_comment · sangbeenmoon · 2026-07-26T07:25:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652002711
- ID: review_comment:3652002711
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 57
- 답글 대상: review_comment:3650316673

````text
네 수정했습니다! 👍 
````

### review_comment · sangbeenmoon · 2026-07-26T07:26:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652003523
- ID: review_comment:3652003523
- 파일: implement-trie-prefix-tree/sangbeenmoon.py, 줄: None, 원래 줄: 4
- 답글 대상: review_comment:3650533420

````text
dictionary 의 약어로 사용했는데요, 좀 더 가독성 있게 네이밍 수정했습니다!
````

### review_comment · sangbeenmoon · 2026-07-26T07:26:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652003689
- ID: review_comment:3652003689
- 파일: word-break/sangbeenmoon.py, 줄: None, 원래 줄: 41
- 답글 대상: review_comment:3650534785

````text
네 수정했습니다!
````

### review_comment · sangbeenmoon · 2026-07-26T07:27:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652005179
- ID: review_comment:3652005179
- 파일: group-anagrams/sangbeenmoon.py, 줄: None, 원래 줄: 51
- 답글 대상: review_comment:3650537708

````text
불필요한 부분이라 제거했습니다!
````

### review_comment · sangbeenmoon · 2026-07-26T07:27:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652005485
- ID: review_comment:3652005485
- 파일: implement-trie-prefix-tree/sangbeenmoon.py, 줄: None, 원래 줄: 29
- 답글 대상: review_comment:3650561317

````text
네 index 를 넘기도록 수정했습니다.
````

### review_comment · sangbeenmoon · 2026-07-26T07:28:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2776#discussion_r3652007309
- ID: review_comment:3652007309
- 파일: implement-trie-prefix-tree/sangbeenmoon.py, 줄: None, 원래 줄: 57
- 답글 대상: review_comment:3650563286

````text
root 처리가 깔끔할까 싶어서 TrieNode 에 구현했던 것인데요, Trie 에 직접 구현하는 것도 방법이었네요 ㅎㅎ 수정했습니다!
````

## [#2777 [alphaorderly] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2777)

### review_comment · JeonJe · 2026-07-30T00:10:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3678910446
- ID: review_comment:3678910446
- 파일: valid-parentheses/alphaorderly.py, 줄: None, 원래 줄: 30

````text
  `return len(stack) == 0` 은 `return not stack` 으로 더 간단하게 써볼 수 있을 것
  같습니다!

  PEP 8 Programming Recommendations에서는 빈 컨테이너의 falsy를 그대로 쓰는 쪽이 권장
  형태인 듯합니다. 저도 이번에 찾아보며 알게 된 거라 공유드립니다 🙂

  > For sequences, (strings, lists, tuples), use the fact that empty sequences are false:
  > ```python
  > # Correct:
  > if not seq:
  > if seq:
  >
  > # Wrong:
  > if len(seq):
  > if not len(seq):
  > ```
````

### review_comment · JeonJe · 2026-07-30T00:19:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3678943704
- ID: review_comment:3678943704
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: None, 원래 줄: 38

````text
  
```python 
elif ch not in node.children:
    continue
else:
    search.append(node.children[ch])
```

케이스마다 동작을 명시하는 것도 좋고, continue가 아무런 동작을 하지 않으니 아래 처럼 줄여볼 수도 있을 것 같습니다!
  
```python 
elif ch in node.children:
    search.append(node.children[ch])
```
````

### review_comment · JeonJe · 2026-07-30T00:20:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3678949915
- ID: review_comment:3678949915
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: 29, 원래 줄: 29

````text
BFS 순회는 생각 하지 못했는데 새롭게 배웠습니다!! 👍 👍 👍 


````

### review_comment · alphaorderly · 2026-07-30T02:09:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3679408726
- ID: review_comment:3679408726
- 파일: valid-parentheses/alphaorderly.py, 줄: None, 원래 줄: 30
- 답글 대상: review_comment:3678910446

````text
맞아요! 배열, 셋 같은데 비어있는지 체크하는데 좋은 연산이죠.
해당 부분 수정했습니다!
````

### review_comment · alphaorderly · 2026-07-30T02:09:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3679409635
- ID: review_comment:3679409635
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: None, 원래 줄: 38
- 답글 대상: review_comment:3678943704

````text
맞네요, continue를 괜히 넣었군요
수정 했습니다!
````

### review_comment · alphaorderly · 2026-07-30T02:10:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3679411493
- ID: review_comment:3679411493
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: 29, 원래 줄: 29
- 답글 대상: review_comment:3678949915

````text
세상에 존재하는 거의 모든 DFS는 BFS로 접근할수 있는거 같더라고요, 물론 재귀 제외하면 DFS가 더 나은것같다는 직감이 들기는 합니다 ㅎㅎ
````

### review_comment · JeonJe · 2026-08-01T03:05:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3694455369
- ID: review_comment:3694455369
- 파일: longest-increasing-subsequence/alphaorderly.py, 줄: 23, 원래 줄: 23

````text
굉장히 깔끔하게 푸셨네요!!
````

### review_comment · okyungjin · 2026-08-01T09:37:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3695348407
- ID: review_comment:3695348407
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: 29, 원래 줄: 29
- 답글 대상: review_comment:3678949915

````text
> 세상에 존재하는 거의 모든 DFS는 BFS로 접근할수 있는거 같더라고요, 물론 재귀 제외하면 DFS가 더 나은것같다는 직감이 들기는 합니다 ㅎㅎ

@alphaorderly “이 문제에서는 단어가 존재하는지 여부만 판단해서 DFS보다 BFS가 더 효율적이다”라고 해석하면 될까요?

정답 제출하실 때 DFS BFS 선택하는 기준이 있으신지 궁금합니다!
````

### review_comment · okyungjin · 2026-08-01T09:39:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3695350616
- ID: review_comment:3695350616
- 파일: valid-parentheses/alphaorderly.py, 줄: None, 원래 줄: 30
- 답글 대상: review_comment:3678910446

````text
이런 문서도 있군요! 공유 감사합니다
````

### review_comment · alphaorderly · 2026-08-01T10:23:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3695413758
- ID: review_comment:3695413758
- 파일: longest-increasing-subsequence/alphaorderly.py, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3694455369

````text
다시 풀때 공을 좀 들였습니다!
````

### review_comment · alphaorderly · 2026-08-01T10:24:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3695415312
- ID: review_comment:3695415312
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: 29, 원래 줄: 29
- 답글 대상: review_comment:3678949915

````text
@okyungjin 
문제가 봤을때 어떤 문제는 특정 경우를 충족하는 경우하 하나라도 있으면 결과가 결정되는 문제가 있는데, 이건 DFS를 선호하고요
특정 경우를 충족하는 모든 경우의 수를 세어야 하는 경우는 BFS를 더 선호하게 되는것 같네요!
````

### review_comment · alphaorderly · 2026-08-01T10:25:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3695416369
- ID: review_comment:3695416369
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: 29, 원래 줄: 29
- 답글 대상: review_comment:3678949915

````text
@okyungjin
혹은 다익스트라와 같이 무조건 BFS로 구현해야 하는 경우도 있습니다!
````

### review_comment · okyungjin · 2026-08-01T16:40:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2777#discussion_r3696078295
- ID: review_comment:3696078295
- 파일: design-add-and-search-words-data-structure/alphaorderly.py, 줄: 29, 원래 줄: 29
- 답글 대상: review_comment:3678949915

````text
> [@okyungjin](https://github.com/okyungjin) 문제가 봤을때 어떤 문제는 특정 경우를 충족하는 경우하 하나라도 있으면 결과가 결정되는 문제가 있는데, 이건 DFS를 선호하고요 특정 경우를 충족하는 모든 경우의 수를 세어야 하는 경우는 BFS를 더 선호하게 되는것 같네요!

@alphaorderly 이번 문제는 충족하는 경우가 있는지 여부만 보면 되니까 DFS에 적합한거군요. 설명 감사합니다☺️ 다음에 문제 풀면서 떠올려보겠습니다!
````

## [#2778 [freemjstudio] WEEK 05 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2778)

### issue_comment · freemjstudio · 2026-07-26T08:34:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2778#issuecomment-5082737624
- ID: issue_comment:5082737624

````text
문제를 추가로 하나 더 풀어서 다시 PR 올립니다. 확인 부탁드립니다!
````

### review_comment · parkhojeong · 2026-07-26T09:25:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2778#discussion_r3652180896
- ID: review_comment:3652180896
- 파일: group-anagrams/freemjstudio.py, 줄: 13, 원래 줄: 13

````text
defaultdict 을 쓰거나 setdefault 같은 방식을 쓰면 if, else를 안쓰고도 가능할 거 같습니다.
````

### review_comment · parkhojeong · 2026-07-26T16:42:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2778#discussion_r3652948533
- ID: review_comment:3652948533
- 파일: implement-trie-prefix-tree/freemjstudio.py, 줄: 7, 원래 줄: 7

````text
Trie가 마지막 여부를 가진다는게 어색하게 느껴지네요. 실제 의미는 루트 노드가 마지막인지를 담는 값인데 Trie 전체가 마지막인지(?)를 알려주는 값처럼 읽히네요. Node의 역할을 Trie에서도 해서 생기는 부분인데 Node 클래스를 이용해서 구현해보시면 좋을 거 같습니다.
````

### review · parkhojeong · 2026-07-26T16:50:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2778#pullrequestreview-4781366685
- ID: review:4781366685
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2780 [JeonJe] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2780)

### review_comment · alphaorderly · 2026-07-28T12:37:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3665532351
- ID: review_comment:3665532351
- 파일: container-with-most-water/JeonJe.java, 줄: 1, 원래 줄: 1

````text
제 생각에 while 안에 area 계산을 맨 윗쪽으로 끌어 올리면 while문밖에 연산을 하지 않아도 될것 같아요! 
그대신 0으로 초기화 하는거죠.
한번 고려해보시는것도 좋을 것 같습니다!
지금은 left와 right가 같은, 즉 하단부가 길이가 0인 너비까지 계산하게 되는것도 있구요
````

### review_comment · alphaorderly · 2026-07-29T00:10:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3670048226
- ID: review_comment:3670048226
- 파일: valid-parentheses/JeonJe.java, 줄: 1, 원래 줄: 1

````text
꽤나 깔끔하게 잘 해결하셨네요!!
````

### review_comment · JeonJe · 2026-07-29T13:03:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3674482115
- ID: review_comment:3674482115
- 파일: container-with-most-water/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3665532351

````text
리뷰 해주신 부분 적용하니 계산 횟수도 1번 줄어들고 코드도 훨씬 깔끔해지네요.

```java  
int answer = 0;
  while (left < right) {
      answer = Math.max(answer, calWaterArea(height, left, right));  // 계산 먼저
      if (height[left] <= height[right]) left++; else right--;       // 그 다음 이동
  }
```

리뷰 감사합니다!!


````

### review_comment · alphaorderly · 2026-07-29T13:31:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3674719817
- ID: review_comment:3674719817
- 파일: design-add-and-search-words-data-structure/JeonJe.java, 줄: 1, 원래 줄: 1

````text
깔끔한 DFS 풀이시네요!
````

### review_comment · alphaorderly · 2026-07-31T01:09:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3687344362
- ID: review_comment:3687344362
- 파일: longest-increasing-subsequence/JeonJe.java, 줄: 10, 원래 줄: 10

````text
아 미리 nums.length 로 배열을 초기화해놔도 괜찮겠네요! 사이즈는 별도로 관리하고요
````

### review_comment · okyungjin · 2026-08-01T06:21:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3694795506
- ID: review_comment:3694795506
- 파일: container-with-most-water/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3686711530

````text
풀이 잘 봤습니다! 

https://github.com/okyungjin/leetcode-study/blob/e764d8be80234ad2765821898a3e5ee02bcc7236/container-with-most-water/okyungjin.py#L29-L35

저도 처음에는 면적 계산 함수와 낮은 높이 구하는 함수를 따로 작성했었는데요,
풀어서 작성하니 높이에 따라 코드가 더 간결해지는 것 같아서 위와 같이 작성했습니다. 참고 부탁드립니다!
````

### review_comment · okyungjin · 2026-08-01T07:37:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695045156
- ID: review_comment:3695045156
- 파일: design-add-and-search-words-data-structure/JeonJe.java, 줄: 23, 원래 줄: 23

````text
@JeonJe 자바에서 26개 정도의 고정 배열이면 HashMap보다 배열이 훨씬 효율적인가요?
````

### review_comment · okyungjin · 2026-08-01T07:41:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695066640
- ID: review_comment:3695066640
- 파일: valid-parentheses/JeonJe.java, 줄: 1, 원래 줄: 1

````text
깔끔한 풀이 잘 봤습니다.
홀수일 때 조기종료하는 로직을 넣으면 최적화 가능할 것 같습니다!
````

### review_comment · okyungjin · 2026-08-01T08:09:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695165217
- ID: review_comment:3695165217
- 파일: longest-increasing-subsequence/JeonJe.java, 줄: 1, 원래 줄: 1

````text
깔끔한 풀이 잘 봤습니다. 저도 n logn 으로 최적화 해보겠습니다! 👍
````

### review · okyungjin · 2026-08-01T08:09:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#pullrequestreview-4833853549
- ID: review:4833853549
- 리뷰 상태: APPROVED

````text
이번 주도 고생하셨습니다 🔥🔥🔥 
````

### review_comment · JeonJe · 2026-08-01T09:14:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695314803
- ID: review_comment:3695314803
- 파일: container-with-most-water/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3686711530

````text
높이를 비교하는 if문 안에서 계산하면 더 깔끔할 수 있겟네요!!
감사합니다!!
````

### review_comment · JeonJe · 2026-08-01T09:17:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695319638
- ID: review_comment:3695319638
- 파일: design-add-and-search-words-data-structure/JeonJe.java, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3695045156

````text
영문 소문자 26개만 다루는 Trie라 HashMap 대신 TrieNode[26]를 사용했습니다.

HashMap도 평균 O(1)이지만 해시 계산과 엔트리 탐색 오버헤드 있어, 키 범위가 고정된 경우에는 배열이 조회/삽입 성능 측면에서 더 효율적이라고 판단했습니다. 

공간은 노드당 26개의 참조를 항상 유지하는 trade-off가 있지만, 문제 특성상 감수할 만한 비용이라고 생각했습니다.
````

### review_comment · JeonJe · 2026-08-01T09:20:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695323401
- ID: review_comment:3695323401
- 파일: valid-parentheses/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3695066640

````text
생각 못했던 엣지 케이스네요
디테일한 리뷰 감사합니다!!
````

### review_comment · okyungjin · 2026-08-01T09:44:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2780#discussion_r3695358703
- ID: review_comment:3695358703
- 파일: design-add-and-search-words-data-structure/JeonJe.java, 줄: 23, 원래 줄: 23
- 답글 대상: review_comment:3695045156

````text
> 영문 소문자 26개만 다루는 Trie라 HashMap 대신 TrieNode[26]를 사용했습니다.
> 
> HashMap도 평균 O(1)이지만 해시 계산과 엔트리 탐색 오버헤드 있어, 키 범위가 고정된 경우에는 배열이 조회/삽입 성능 측면에서 더 효율적이라고 판단했습니다.
> 
> 공간은 노드당 26개의 참조를 항상 유지하는 trade-off가 있지만, 문제 특성상 감수할 만한 비용이라고 생각했습니다.

답변 감사드립니다.
직관적으로 HashMap 구조가 먼저 떠올랐는데 다음에는 이 방법도 떠올려볼 수 있을 것 같습니다🙏
````

## [#2781 [okyungjin] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2781)

### review_comment · okyungjin · 2026-07-31T16:02:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3691708916
- ID: review_comment:3691708916
- 파일: design-add-and-search-words-data-structure/okyungjin.py, 줄: 1, 원래 줄: 1

````text
최적화 필요! Trie 자료구조 사용 가능한지 고민해보기
````

### review_comment · dahyeong-yun · 2026-08-01T08:45:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3695261824
- ID: review_comment:3695261824
- 파일: valid-parentheses/okyungjin.py, 줄: 26, 원래 줄: 26

````text
이 케이스가 성공하는 경우가 없을 것 같아요.
````

### review_comment · dahyeong-yun · 2026-08-01T08:46:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3695264444
- ID: review_comment:3695264444
- 파일: valid-parentheses/okyungjin.py, 줄: 13, 원래 줄: 13

````text
미리 dictionary 를 만드니, 아래에서 깔끔하게 접근할 수 있네요 👍🏼 
````

### review_comment · dahyeong-yun · 2026-08-01T08:56:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3695287895
- ID: review_comment:3695287895
- 파일: container-with-most-water/okyungjin.py, 줄: 31, 원래 줄: 31

````text
사소하지만 `right - left` 가 `width`의 개념이고 아래서 반복되는 거 같아, 따로 빼도 괜찮을 것 같아요.
````

### issue_comment · okyungjin · 2026-08-01T09:47:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#issuecomment-5150892993
- ID: issue_comment:5150892993

````text
@dalestudy 풀이 유형 체크
````

### issue_comment · okyungjin · 2026-08-01T09:48:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#issuecomment-5150895230
- ID: issue_comment:5150895230

````text
@dalestudy 코드 리뷰 부탁해
````

### review_comment · dahyeong-yun · 2026-08-01T10:33:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3695427518
- ID: review_comment:3695427518
- 파일: design-add-and-search-words-data-structure/okyungjin.py, 줄: 1, 원래 줄: 1

````text
저는 트라이 문제는 다 skip 했는데, 직관적으로 접근하신 부분에서 트라이의 필요성을 역체감 할 수 있어서 좋았습니다!
````

### review · dahyeong-yun · 2026-08-01T10:35:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#pullrequestreview-4834324854
- ID: review:4834324854
- 리뷰 상태: APPROVED

````text
한 주간 고생 많으셨습니다. 상세히 적어주신 덕분에 공부가 많이 됐습니다. 개인적으로는 표현상 일관된 것을 선호하는 편이라서 max 값을 만드는 과정에서 if 분기와 max 함수를 번갈아 쓰시는 것이 눈에 띄긴 한 것 같아요. 특별한 이유가 있으셨는지가 살짝 궁금하네요. :)
````

### review_comment · okyungjin · 2026-08-01T13:29:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3695700005
- ID: review_comment:3695700005
- 파일: valid-parentheses/okyungjin.py, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:3695261824

````text
> 이 케이스가 성공하는 경우가 없을 것 같아요.

오 그렇네요 감사합니다. 다음 문제 풀때 수정해두겠습니다🙏
````

### review_comment · okyungjin · 2026-08-01T13:29:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#discussion_r3695700448
- ID: review_comment:3695700448
- 파일: container-with-most-water/okyungjin.py, 줄: 31, 원래 줄: 31
- 답글 대상: review_comment:3695287895

````text
의견 감사합니다!
````

### issue_comment · okyungjin · 2026-08-01T13:37:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2781#issuecomment-5151660820
- ID: issue_comment:5151660820

````text
@dahyeong-yun 정성스러운 리뷰 감사드립니다!

값 2개 비교할 때는 if문 사용하고, 그 이상인 곳은 max를 사용했습니다. 리트코드에서 실행해보면 min , max 함수 사용했을 때 if문보다 오버헤드가 큰 것 같더라구요.

리뷰 주신 부분은 다음 문제 풀 때 적용하겠습니다 🙂 감사합니다!

> 한 주간 고생 많으셨습니다. 상세히 적어주신 덕분에 공부가 많이 됐습니다. 개인적으로는 표현상 일관된 것을 선호하는 편이라서 max 값을 만드는 과정에서 if 분기와 max 함수를 번갈아 쓰시는 것이 눈에 띄긴 한 것 같아요. 특별한 이유가 있으셨는지가 살짝 궁금하네요. :)


````

## [#2783 [dahyeong-yun] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2783)

### review_comment · dolphinflow86 · 2026-07-30T06:50:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2783#discussion_r3680594282
- ID: review_comment:3680594282
- 파일: valid-parentheses/dahyeong-yun.java, 줄: 20, 원래 줄: 20

````text
사소하지만, stack에 isEmtpy()가 있다면 사용하시면 좀 더 가독성이 좋을 것 같아요.
````

### review_comment · dolphinflow86 · 2026-07-30T06:51:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2783#discussion_r3680597627
- ID: review_comment:3680597627
- 파일: valid-parentheses/dahyeong-yun.java, 줄: 25, 원래 줄: 25

````text
저도 리뷰 받은 사항인데, map에 key, value로 여는괄호 닫는괄호 쌍을 넣어두고 체크하면 코드가 매우 깔끔해질 것 같습니다.
````

### review_comment · dolphinflow86 · 2026-07-30T06:56:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2783#discussion_r3680624229
- ID: review_comment:3680624229
- 파일: valid-parentheses/dahyeong-yun.java, 줄: 11, 원래 줄: 11

````text
찾아보니 toCharArray가 내부적으로 문자열을 복제헤서 새로 만든다고 하네요.
인덱스 접근으로 s.chatAt(i) 처럼 하시면 불필요한 연산을 줄이실 수 있을 것 같습니다.
````

### review_comment · parkhojeong · 2026-08-01T16:13:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2783#discussion_r3696013706
- ID: review_comment:3696013706
- 파일: spiral-matrix/dahyeong-yun.java, 줄: 34, 원래 줄: 34

````text
주석 내용도 이해가 쉽고 코드도 직관적인 거 같습니다. 

101 을 방문 처리용 값으로 쓰시는데 VISITED 같은 상수로 선언해서 사용하면 더 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-01T16:19:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2783#discussion_r3696025370
- ID: review_comment:3696025370
- 파일: container-with-most-water/dahyeong-yun.java, 줄: 19, 원래 줄: 19

````text
자바의 Math.min은 오버헤드가 적고 가독성을 챙길 수 있어서 내장함수 사용도 좋을 거 같습니다. 19라인에 Math.max 사용하고 있어서 Math.min 사용하면 일관성이 있을 거 같습니다.
````

### review · parkhojeong · 2026-08-01T16:19:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2783#pullrequestreview-4835054269
- ID: review:4835054269
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2784 [dolphinflow86] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2784)

### review_comment · DaleSeo · 2026-07-30T01:08:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3679151827
- ID: review_comment:3679151827
- 파일: container-with-most-water/dolphinflow86.py, 줄: None, 원래 줄: 14

````text
대소 비교는 내장 함수로 표현하면 코드도 간결해지고 의도가 잘 드러나는 것 같더라고요.

```suggestion
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
```
````

### review · DaleSeo · 2026-07-30T01:09:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#pullrequestreview-4814303796
- ID: review:4814303796
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 취향 문제일 수도 있는 사소한 댓글 하나 남겼어요~
````

### review_comment · alphaorderly · 2026-07-30T02:02:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3679377392
- ID: review_comment:3679377392
- 파일: container-with-most-water/dolphinflow86.py, 줄: None, 원래 줄: 14
- 답글 대상: review_comment:3679151827

````text
저도 동의합니다, 미세한 성능 차이에 비해 간결성이 훨씬 좋아져요
````

### review_comment · alphaorderly · 2026-07-30T02:04:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3679383596
- ID: review_comment:3679383596
- 파일: valid-parentheses/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
pair 쌍을 dict를 통해 만들어보시는건 어떨까요?
여는 괄호를 key로 하고 닫는 괄호는 value로 하는거죠!
x in dictionary 연산에서 x는 dictionary의 키 중 하나이면 True인것을 이용하면
코드를 매우 간결하게 구현할수 있으실겁니다!
````

### review_comment · dolphinflow86 · 2026-07-30T06:40:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3680541371
- ID: review_comment:3680541371
- 파일: container-with-most-water/dolphinflow86.py, 줄: None, 원래 줄: 14
- 답글 대상: review_comment:3679151827

````text
안녕하세요. 사실 저도 내장함수 쓰는걸 선호하는데 저번 리뷰에서 내장 함수 사용에 대한 비용에 대한 리뷰가 있어서 이번에는 수동으로 한번 써봤습니다 :)

다만 각 함수등의 내부 동작/복잡도, 호출 오버헤드 등을 인지만 하고 있으면, 가독성이 훨씬 좋아져서 사용하는게 좋은 것 같아요. 

적용했습니다.
두 분 리뷰 감사합니다!
````

### review_comment · dolphinflow86 · 2026-07-30T06:46:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3680572954
- ID: review_comment:3680572954
- 파일: valid-parentheses/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3679383596

````text
와..생각치 못했는데 코드가 엄청 깔끔해지겠네요.
한번 적용 해 보겠습니다. 👍 
````

### review_comment · alphaorderly · 2026-07-31T00:57:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3687301036
- ID: review_comment:3687301036
- 파일: valid-parentheses/dolphinflow86.py, 줄: None, 원래 줄: 16

````text
이부분을 그러니까 `ch in pair` 로 대체 가능하세요!
해상 연산은 pair에 ch가 key로 존재하는지 확인하기 때문에 정확히 동일한 연산으로 작동하게 됩니다.
````

### review_comment · dolphinflow86 · 2026-07-31T09:39:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3689506223
- ID: review_comment:3689506223
- 파일: valid-parentheses/dolphinflow86.py, 줄: None, 원래 줄: 16
- 답글 대상: review_comment:3687301036

````text
아 제가 아래부분만 바꾸고 여기는 안바꿨군요!
수정 완료했습니다. 훨씬 깔끔해요!
````

### review_comment · parkhojeong · 2026-08-01T13:59:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#discussion_r3695749400
- ID: review_comment:3695749400
- 파일: design-add-and-search-words-data-structure/dolphinflow86.py, 줄: 11, 원래 줄: 11

````text
초기 값으로 None이 할당되어서 어떤 값이 이후에 들어올 수 있는지 코드를 전부 읽어야 파악이 가능한 거 같습니다. 타입힌트로 TreeNode 또는 None이 배열의 원소인걸 드러내면 미리 예측이 가능해서 더 좋을 거 같네요. 
````

### review · parkhojeong · 2026-08-01T14:03:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2784#pullrequestreview-4834781962
- ID: review:4834781962
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2785 [DaleSeo] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2785)

### review · yuseok89 · 2026-08-01T11:08:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2785#pullrequestreview-4834540001
- ID: review:4834540001
- 리뷰 상태: APPROVED

````text
Rust를 잘 알지 못해서 디테일한 부분까지는 리뷰 못 드리는 점 아쉽습니다 ㅠ
그래도 search_from이 끝 도달 / 와일드카드 / 일반 문자 세 경우로 나뉘는 구조가 명확해서, Rust를 몰라도 전체 흐름은 잘 따라갈 수 있었습니다 👍
````

## [#2786 [yuseok89] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2786)

### review_comment · alphaorderly · 2026-07-31T13:55:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3690905543
- ID: review_comment:3690905543
- 파일: design-add-and-search-words-data-structure/yuseok89.py, 줄: 1, 원래 줄: 1

````text
제 생각에 너무 좋은 코드인데요, Python의 타입 힌팅을 적극적으로 이제 활용해 보시면 코드의 가독성에 큰 긍정적 영향을 줄것이라고 생각해요!
특히 메서드를 추가 작성할때 input param들의 타입과 return type을 작성하면 개인적으로는 상당한 가독성의 향상이 있다고 생각합니다.
````

### review_comment · alphaorderly · 2026-07-31T13:55:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3690907383
- ID: review_comment:3690907383
- 파일: design-add-and-search-words-data-structure/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3690905543

````text
아 물론 개인적 의견이니 꼭 하실 필요는 없습니다!!!
````

### review_comment · alphaorderly · 2026-07-31T13:58:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3690925909
- ID: review_comment:3690925909
- 파일: spiral-matrix/yuseok89.py, 줄: 1, 원래 줄: 1

````text
와 이건 코드를 아트의 경지로 올리셨군요 ㄷㄷㄷ 대단하십니다.
배우고 갑니다!
````

### review_comment · alphaorderly · 2026-07-31T14:04:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3690966005
- ID: review_comment:3690966005
- 파일: valid-parentheses/yuseok89.py, 줄: None, 원래 줄: 12

````text
`if not stack or pars[stack.pop()] != c:`
제 개인적인 생각으로는 이것으로 수정하면
1. `not stack` 을 통해 스택이 비어있는 경우를 먼저 확인
  > 단축 평가에 의해 stack이 비어 있으면 False를 리턴하기에 or의 뒤에 있는 부분은 실행시 stack에 값이 있음이 확실시 됩니다!
2. `pars[stack.pop()] != c` 
  > 이부분은 stack에 값이 있음이 확실시 되고, 어차피 닫는 기호는 스택에 들어가지 않기 때문에 스택 내부에는 여는 기호만 있는것이 확실시 되기 때문에 get과 기본값을 명시하는것이 크게 필요하지 않다는 생각이 들었습니다.
````

### review · alphaorderly · 2026-07-31T14:10:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#pullrequestreview-4829223714
- ID: review:4829223714
- 리뷰 상태: APPROVED

````text
전반적으로 깔끔한 풀이 잘 봤습니다!
````

### review_comment · njngwn · 2026-07-31T18:09:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3692445546
- ID: review_comment:3692445546
- 파일: spiral-matrix/yuseok89.py, 줄: 4, 원래 줄: 4

````text
진짜 깔끔하게 푸셨네요. 리뷰하러 왔다가 배워갑니다..!!!
````

### review_comment · njngwn · 2026-07-31T18:11:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3692454631
- ID: review_comment:3692454631
- 파일: container-with-most-water/yuseok89.py, 줄: None, 원래 줄: 21

````text
파이썬이니까 세미콜론은 없어도 될 것 같습니다 😄
````

### review_comment · njngwn · 2026-07-31T18:16:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3692481891
- ID: review_comment:3692481891
- 파일: valid-parentheses/yuseok89.py, 줄: None, 원래 줄: 2

````text
공간복잡도를 O(N/2) 라고 생각하신 이유가 있을까요?
````

### review_comment · yuseok89 · 2026-08-01T10:22:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3695412326
- ID: review_comment:3695412326
- 파일: valid-parentheses/yuseok89.py, 줄: None, 원래 줄: 2
- 답글 대상: review_comment:3692481891

````text
잘못 생각했었네요
O(N) 이 맞습니다
리뷰 감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-08-01T10:24:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3695415629
- ID: review_comment:3695415629
- 파일: valid-parentheses/yuseok89.py, 줄: None, 원래 줄: 12
- 답글 대상: review_comment:3690966005

````text
더 좋네요.
막 쓰다보니, 어차피 여는 기호만 있는 것을 기본값으로 처리해버렸네요.
리뷰 감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-08-01T10:25:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2786#discussion_r3695416940
- ID: review_comment:3695416940
- 파일: design-add-and-search-words-data-structure/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3690905543

````text
문제 푸는 코드를 쓰면서는 신경 안쓴 부분이었는데,
리트코드에서 기본으로 주는 코드엔 이미 들어가있네요.
리뷰하는 입장에서도 있는 것이 더 좋을 것 같습니다 !
````

## [#2787 [njngwn] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2787)

### review_comment · ICE0208 · 2026-08-01T12:00:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3695562557
- ID: review_comment:3695562557
- 파일: valid-parentheses/njngwn.py, 줄: 9, 원래 줄: 9

````text
길이가 홀수인 경우 미리 반환해 불필요한 연산을 줄인 점이 좋네요!
````

### review_comment · ICE0208 · 2026-08-01T12:04:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3695568911
- ID: review_comment:3695568911
- 파일: design-add-and-search-words-data-structure/njngwn.py, 줄: 36, 원래 줄: 36

````text
`ch == '.'`인 경우 마지막에 `return False`로 종료되므로, `else`를 제거하면 중첩 깊이를 줄여 코드를 조금 더 간결하게 작성할 수 있을 것 같습니다!
````

### review_comment · ICE0208 · 2026-08-01T12:16:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3695585685
- ID: review_comment:3695585685
- 파일: spiral-matrix/njngwn.py, 줄: None, 원래 줄: 10

````text
현재 방향 전환과 경계 갱신 로직이 정상적으로 동작한다면 `i`, `j`가 행렬 범위를 벗어날 일은 없을 것 같은데, `while` 조건에 좌표 범위 검사까지 추가하신 이유가 따로 있을까요? 어떤 의도로 작성하셨는지 궁금합니다!

````

### review_comment · ICE0208 · 2026-08-01T12:17:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3695587844
- ID: review_comment:3695587844
- 파일: spiral-matrix/njngwn.py, 줄: 1, 원래 줄: 1

````text
오른쪽, 아래, 왼쪽, 위 순서로 이동하면서 경계 범위를 점차 줄여 나가는 방식이 인상적이었습니다. 좋은 로직 잘 보고갑니다!
````

### review · ICE0208 · 2026-08-01T12:20:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#pullrequestreview-4834614247
- ID: review:4834614247
- 리뷰 상태: APPROVED

````text
안녕하세요. 이번 주 코드 리뷰를 맡은 ICE0208입니다.

전반적으로 깔끔하게 작성해 주셨고, 주석이 조금 더 추가되면 이해에 도움이 될 것 같습니다.

추가 의견과 질문은 코멘트로 남겨두었습니다. 이번 주도 고생 많으셨습니다!

````

### review_comment · parkhojeong · 2026-08-01T16:22:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3696036799
- ID: review_comment:3696036799
- 파일: longest-increasing-subsequence/njngwn.py, 줄: None, 원래 줄: 3

````text
seq가 최악의 경우 길이 n만큼 되서 SC는 O(n)이지 않을까요? ex. [1, 2, 3, 4, 5]
````

### review_comment · parkhojeong · 2026-08-01T17:00:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3696123523
- ID: review_comment:3696123523
- 파일: longest-increasing-subsequence/njngwn.py, 줄: 19, 원래 줄: 19

````text
오 python bisect_left 랑 동일하게 구현하셨는데 원래 bisect_left 알고 계셨는지 궁금하네요. https://github.com/python/cpython/blob/7ce7f0bd8511410bf7c42cc5fc88dfafe07874b6/Lib/bisect.py#L74
````

### review_comment · parkhojeong · 2026-08-01T17:01:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3696125145
- ID: review_comment:3696125145
- 파일: longest-increasing-subsequence/njngwn.py, 줄: None, 원래 줄: 12

````text
로직은 찾는 값보다 큰 값 중 가장 작은 데에 덮어 쓰는 동작으로 보이는데요. 주석을 insert, binary search 용어를 사용해서 적으신 이유가 있을까요? 지금 주석은 해당 값을 찾아서(탐색) 그 인덱스에 insert(python) 하는 동작으로 읽혀서요.
````

### review · parkhojeong · 2026-08-01T17:09:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#pullrequestreview-4835084631
- ID: review:4835084631
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다. 복잡도 표기와 주석 수정이 필요해 보여서 request-changed로 남겨두었습니다.
````

### review_comment · njngwn · 2026-08-02T09:23:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3698544080
- ID: review_comment:3698544080
- 파일: longest-increasing-subsequence/njngwn.py, 줄: None, 원래 줄: 3
- 답글 대상: review_comment:3696036799

````text
맞습니다! 최악의 경우 seq가 n까지 자랄 수 있어서 공간복잡도는 O(n)이 맞네요..!!
````

### review_comment · njngwn · 2026-08-02T09:23:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3698545387
- ID: review_comment:3698545387
- 파일: longest-increasing-subsequence/njngwn.py, 줄: None, 원래 줄: 12
- 답글 대상: review_comment:3696125145

````text
아 오해의 소지가 있을 수 있겠네요. overwrite라 고치는게 맞을 것 같습니다. 감사합니다!
````

### review_comment · njngwn · 2026-08-02T09:24:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3698547009
- ID: review_comment:3698547009
- 파일: longest-increasing-subsequence/njngwn.py, 줄: 19, 원래 줄: 19
- 답글 대상: review_comment:3696123523

````text
엇 아뇨 다른 분 코드 리뷰하다가 저런게 존재하는지 나중에야 알게됐어요😂 정보 감사합니다!
````

### review_comment · njngwn · 2026-08-02T09:25:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3698550209
- ID: review_comment:3698550209
- 파일: design-add-and-search-words-data-structure/njngwn.py, 줄: 36, 원래 줄: 36
- 답글 대상: review_comment:3695568911

````text
오 그렇겠네요!! 굳이 else를 넣을 필요가 없었네요
````

### review_comment · njngwn · 2026-08-02T09:26:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2787#discussion_r3698553033
- ID: review_comment:3698553033
- 파일: spiral-matrix/njngwn.py, 줄: None, 원래 줄: 10
- 답글 대상: review_comment:3695585685

````text
i, j가 범위를 벗어난다는 확신이 없어서 추가했던건데, 다시 계산해보니까 빼도 문제가 없겠네요. 감사합니다!
````

## [#2788 [ICE0208] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2788)

### review_comment · daehyun99 · 2026-08-01T07:15:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3694940508
- ID: review_comment:3694940508
- 파일: spiral-matrix/ICE0208.py, 줄: 1, 원래 줄: 1

````text
`inRange` 함수와 `visit`를 활용해서, `matrix`의 범위인지 체크하는 방법도 좋은 것 같네요!
다만, 공간 복잡도가 `matrix`만큼 추가로 필요하게 되네요.

문제에서 `matrix`의 shape을 알 수 있고, `matrix`를 순회하는 과정에서 shape 정보만으로 순회를 할 수 있습니다. 이를 활용하면, 추가적인 메모리 사용 없이 문제를 풀 수 있습니다. 시간이 되신다면, 이 방법으로 풀어보셔도 좋을 것 같아요!
````

### review · daehyun99 · 2026-08-01T07:21:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#pullrequestreview-4834006559
- ID: review:4834006559
- 리뷰 상태: APPROVED

````text
안녕하세요! 이번 주 리뷰를 맡은 김대현입니다.

전반적으로 코드도 깔끔하고 최적화 잘해서 풀어주셨네요.

#282 문제에 대해서만 코멘트를 남겨놨는데, 시간이 되신다면 풀어보시는 것도 좋을 것 같습니다.

고생 많으셨습니다!!!
````

### review_comment · alphaorderly · 2026-08-01T10:28:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695421204
- ID: review_comment:3695421204
- 파일: longest-increasing-subsequence/ICE0208.py, 줄: 1, 원래 줄: 1

````text
N Log N 풀이법이 있습니다! 시도해 보시죠!
````

### review_comment · ICE0208 · 2026-08-01T12:23:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695595299
- ID: review_comment:3695595299
- 파일: longest-increasing-subsequence/ICE0208.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3695421204

````text
알려주셔서 감사합니다! 예전에 `O(n log n)` 풀이와 증명까지 공부했었는데, 지금은 로직만 기억나고 왜 그렇게 동작하는지는 잘 떠오르지 않아 우선 정석적인 `O(n²)` 풀이로 제출했습니다.

말씀해 주신 `O(n log n)` 방식도 다시 찾아보며 공부해 보겠습니다. 감사합니다! ☺️

````

### review_comment · ICE0208 · 2026-08-01T12:38:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695618442
- ID: review_comment:3695618442
- 파일: spiral-matrix/ICE0208.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3694940508

````text
[b8faa50](https://github.com/DaleStudy/leetcode-study/pull/2788/commits/b8faa506ed8abff3cb8ffce59174dc10d930b8fc)
일단 공간 복잡도를 줄이기 위해 별도의 `visit` 배열을 제거하는 방식으로 수정해 보았습니다!

다만 현재는 방문 여부를 표시하기 위해 `matrix`의 값을 직접 변경하고 있고, 말씀해 주신 방법과도 조금 다른 것 같아 나중에 다시 고민해 봐야겠네요 ㅎㅎ

혹시 `top`, `right`, `bottom`, `left` 경계값을 설정한 뒤, 순회하면서 각 경계를 줄여 나가는 방식을 말씀하신 게 맞을까요? 👀

````

### review_comment · parkhojeong · 2026-08-01T13:20:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695684995
- ID: review_comment:3695684995
- 파일: container-with-most-water/ICE0208.py, 줄: 6, 원래 줄: 6

````text
( ) 괄호는 붙이신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-08-01T13:26:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695694608
- ID: review_comment:3695694608
- 파일: spiral-matrix/ICE0208.py, 줄: 25, 원래 줄: 25

````text
in range 와 is visit 을 하나로 묶어서 함수로 추상화 해도 좋을 거 같습니다 
````

### review_comment · parkhojeong · 2026-08-01T13:30:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695700787
- ID: review_comment:3695700787
- 파일: valid-parentheses/ICE0208.java, 줄: 12, 원래 줄: 12

````text
Map.of 사용해서 선언시점에 할당해도 좋을 거 같아요
````

### review · parkhojeong · 2026-08-01T13:33:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#pullrequestreview-4834724994
- ID: review:4834724994
- 리뷰 상태: APPROVED

````text
수고하셨습니다
````

### review_comment · ICE0208 · 2026-08-01T14:00:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695751135
- ID: review_comment:3695751135
- 파일: container-with-most-water/ICE0208.py, 줄: 6, 원래 줄: 6
- 답글 대상: review_comment:3695684995

````text
아뇨 없습니다🤣 다른 언어랑 왔다갔다하니 무의식적으로 괄호로 감싼 것 같네요 ㅎㅎ
````

### review_comment · ICE0208 · 2026-08-01T14:01:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695752294
- ID: review_comment:3695752294
- 파일: spiral-matrix/ICE0208.py, 줄: 25, 원래 줄: 25
- 답글 대상: review_comment:3695694608

````text
그러네요! 좋은 의견 감사드립니다!!
````

### review_comment · ICE0208 · 2026-08-01T14:03:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695755407
- ID: review_comment:3695755407
- 파일: valid-parentheses/ICE0208.java, 줄: 12, 원래 줄: 12
- 답글 대상: review_comment:3695700787

````text
변경되지 않는 고정된 값이니 Map.of()를 사용해도 되겠네요. 알려주셔서 감사합니다!
````

### review_comment · daehyun99 · 2026-08-01T14:13:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695772854
- ID: review_comment:3695772854
- 파일: spiral-matrix/ICE0208.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3694940508

````text
음 아래의 이미지처럼, `matrix`의 `m`과 `n`을 구할 수 있고, 단순히 첫 번째 이동은 `m`만큼, 두번째 이동은 `n`만큼, 세 번째 이동은 `m-1`만큼...하는 것을 말한 것이었습니다

<img width="2004" height="1214" alt="image" src="https://github.com/user-attachments/assets/a8e68b3b-f1cb-40f4-aaf5-c3bd2e1c1d5b" />

````

### review_comment · ICE0208 · 2026-08-01T14:37:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2788#discussion_r3695813867
- ID: review_comment:3695813867
- 파일: spiral-matrix/ICE0208.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3694940508

````text
이런 방식으로도 풀 수 있었네요!
감사합니다🙇‍♂️ 복습할 때 참고하겠습니다👍
````

## [#2789 [daehyun99] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2789)

### review · sangbeenmoon · 2026-08-01T07:11:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2789#pullrequestreview-4833990502
- ID: review:4833990502
- 리뷰 상태: APPROVED

````text
한주도 고생많으셨습니다! 👍 
````

## [#2790 [sangbeenmoon] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2790)

### review_comment · alphaorderly · 2026-08-01T10:21:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3695411458
- ID: review_comment:3695411458
- 파일: design-add-and-search-words-data-structure/sangbeenmoon.py, 줄: None, 원래 줄: 41

````text
이부분은 맞는 단어가 없다는거니까 return False를 하는게 더 맞지 않을까 생각해요!
````

### review_comment · sangbeenmoon · 2026-08-02T05:00:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3697900173
- ID: review_comment:3697900173
- 파일: design-add-and-search-words-data-structure/sangbeenmoon.py, 줄: None, 원래 줄: 41
- 답글 대상: review_comment:3695411458

````text
맞네요 ㅎㅎ 수정했습니다! 👍 
````

### issue_comment · sangbeenmoon · 2026-08-02T05:04:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#issuecomment-5155523871
- ID: issue_comment:5155523871

````text
@DaleStudy/coach 승인
````

### review_comment · parkhojeong · 2026-08-02T06:52:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3698163934
- ID: review_comment:3698163934
- 파일: container-with-most-water/sangbeenmoon.py, 줄: 12, 원래 줄: 12

````text
현재까지 최대의 넓이를 갖는 변수라 answer보단 max_area 같은 것을 쓰는게 더 좋지 않을까 싶어요
````

### review_comment · parkhojeong · 2026-08-02T06:53:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3698166580
- ID: review_comment:3698166580
- 파일: design-add-and-search-words-data-structure/sangbeenmoon.py, 줄: 27, 원래 줄: 27

````text
i >= len(word) 이라 len(word) 보다 큰 값인 경우가 들어오는 것처럼 보일 수도 있을 거 같긴 하네요. == 로 비교하면 더 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-02T06:57:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3698174360
- ID: review_comment:3698174360
- 파일: longest-increasing-subsequence/sangbeenmoon.py, 줄: 72, 원래 줄: 72

````text
seq[-1] 을 사용하시면 더 간결할 거 같네요.
````

### review_comment · parkhojeong · 2026-08-02T07:03:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3698186366
- ID: review_comment:3698186366
- 파일: spiral-matrix/sangbeenmoon.py, 줄: 86, 원래 줄: 86

````text
사소한 부분인데 파이썬의 if else 는 다른 언어들의 삼항 연산자보단 가독성이 개인적으로는 좀 아쉬운 거 같긴합니다. 
`d = (d + 1) % 4` 도 괜찮은 거 같기도 합니다.
````

### review_comment · parkhojeong · 2026-08-02T07:05:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#discussion_r3698191530
- ID: review_comment:3698191530
- 파일: spiral-matrix/sangbeenmoon.py, 줄: 75, 원래 줄: 75

````text
x, row가 섞여 쓰여서 통일이 되어도 좋을 거 같기는 하네요. x, dx, x_len 혹은 row, drow, row_len 으로 맞추면 일관성이 있을 거 같습니다.
````

### review · parkhojeong · 2026-08-02T07:06:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2790#pullrequestreview-4837540688
- ID: review:4837540688
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 사소한 부분들 몇 가지 커멘트 남겼습니다.
````

## [#2791 [Chanz] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2791)

### review_comment · parkhojeong · 2026-08-01T12:34:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2791#discussion_r3695612420
- ID: review_comment:3695612420
- 파일: valid-parentheses/Chanz82.py, 줄: 8, 원래 줄: 8

````text
선언 시점에 할당하면 좀 더 간결해 질 거 같네요.
```suggestion
        ch_map = {
          ")": "(",
          "}": "{",
          "]": "["
        }
```
````

### review_comment · parkhojeong · 2026-08-01T12:41:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2791#discussion_r3695622330
- ID: review_comment:3695622330
- 파일: container-with-most-water/Chanz82.py, 줄: 13, 원래 줄: 13

````text
left == right인 경우는 필요 없어서 `while left < right`로 해줘도 될 거 같습니다.
````

### review · parkhojeong · 2026-08-01T13:01:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2791#pullrequestreview-4834658884
- ID: review:4834658884
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

### review_comment · parkhojeong · 2026-08-01T13:04:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2791#discussion_r3695660438
- ID: review_comment:3695660438
- 파일: design-add-and-search-words-data-structure/Chanz82.py, 줄: 24, 원래 줄: 24

````text
slicing을 쓰면 O(n)이라 slicing을 안 쓰도록 풀어보셔도 좋을 거 같아요.
````

### review_comment · Chanz82 · 2026-08-04T22:32:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2791#discussion_r3716640727
- ID: review_comment:3716640727
- 파일: valid-parentheses/Chanz82.py, 줄: 8, 원래 줄: 8
- 답글 대상: review_comment:3695612420

````text
감사합니다. 이렇게 습관을 들여봐야겠어요!
````

### review_comment · Chanz82 · 2026-08-04T22:34:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2791#discussion_r3716649435
- ID: review_comment:3716649435
- 파일: design-add-and-search-words-data-structure/Chanz82.py, 줄: 24, 원래 줄: 24
- 답글 대상: review_comment:3695660438

````text
아..!! 이거 전에도 비슷한 문제에서 피드백 주셨던 것 같아요. 😂 index로 해봐야겠습니다. 감사합니다!
````

## [#2792 [parkhojeong] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2792)

### review_comment · alphaorderly · 2026-08-02T00:54:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3697109132
- ID: review_comment:3697109132
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
1. getter와 setter를 사용하실 예정이시라면 Python에서는 각 property의 이름 앞에 _ 를 붙이는것이 관례라고 알고 있습니다.
> self._is_end, self._child

2. 해당 문제는 단일 클래스로 해결이 가능한 문제인데, 3개까지 나누는것은 아주 개인적으로는 좀 오버 엔지니어링이 아닐까 하는 생각이 들어요, 
````

### review_comment · alphaorderly · 2026-08-02T00:55:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3697112757
- ID: review_comment:3697112757
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: None, 원래 줄: 5

````text
해당 부분은 클래스 변수를 선언하신것 같은데 삭제해도 무방할것 같아요!
````

### review_comment · alphaorderly · 2026-08-02T00:58:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3697120459
- ID: review_comment:3697120459
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
1의 예시입니다.
_query는 숨기는것에 해당하고 ( private 접근 제어자에 해당 )
query는 보여주는것에 해당합니다 ( public 접근 제어자에 해당 )
```python
def _query(
        self,
        node_index: int,
        seg_left: int,
        seg_right: int,
        qur_left: int,
        qur_right: int,
    ) -> int:
        if seg_right < qur_left or qur_right < seg_left:
            return 0

        if qur_left <= seg_left <= seg_right <= qur_right:
            return self.tree[node_index]

        mid = (seg_left + seg_right) // 2
        left = self._query(node_index * 2, seg_left, mid, qur_left, qur_right)
        right = self._query(node_index * 2 + 1, mid + 1, seg_right, qur_left, qur_right)

        return max(left, right)

def query(self, left: int, right: int) -> int:
    if left > right:
        return 0
    return self._query(1, 0, self.n - 1, left, right)
```
````

### review_comment · alphaorderly · 2026-08-02T00:59:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3697123960
- ID: review_comment:3697123960
- 파일: longest-increasing-subsequence/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
N Log N 풀이도 꼭 한번 시도 해 보시죠!
````

### review_comment · alphaorderly · 2026-08-02T01:01:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3697128715
- ID: review_comment:3697128715
- 파일: valid-parentheses/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
`close_parenthesis_map` 만들어두신 이거 자체가 
`'(' in close_parenthesis_map` 과 같이 사용시 key값에 한해 키에 해당 값이 있는지 체크한다는게 있다는것을 아시나요?
그러면 set을 없애고도 동일한 코드를 그대로 구현할수 있습니다.
````

### review · alphaorderly · 2026-08-02T01:02:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#pullrequestreview-4836329086
- ID: review:4836329086
- 리뷰 상태: APPROVED

````text
한주 고생하셨습니다!

````

### review_comment · parkhojeong · 2026-08-02T05:27:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3697977624
- ID: review_comment:3697977624
- 파일: longest-increasing-subsequence/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697123960

````text
네 그렇게도 풀어보겠습니다. 감사합니다
````

### review_comment · parkhojeong · 2026-08-02T06:02:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698057117
- ID: review_comment:3698057117
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
_는 private에 대한 네이밍 컨벤션으로 알고 있는데 getter, setter에 _를 붙이는 건 어떤 관례일까요?
https://docs.python.org/3/tutorial/classes.html#private-variables

````

### review_comment · parkhojeong · 2026-08-02T06:03:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698059613
- ID: review_comment:3698059613
- 파일: longest-increasing-subsequence/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697123960

````text
https://github.com/DaleStudy/leetcode-study/pull/2792/commits/37d9a1348c6c433cfc1821540d0d8dfb10c5a141 bisect_left 이용해서 다시 풀어봤습니다.
````

### review_comment · parkhojeong · 2026-08-02T06:04:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698063034
- ID: review_comment:3698063034
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: None, 원래 줄: 5
- 답글 대상: review_comment:3697112757

````text
인스턴스 변수는 __init__ 쪽으로 옮겨주었습니다. https://github.com/DaleStudy/leetcode-study/pull/2792/commits/75410ea130cd0a2d5b1cc25cabe27b4db89813b9 

파이썬 공식 문서)
https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables 
````

### review_comment · parkhojeong · 2026-08-02T06:05:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698067485
- ID: review_comment:3698067485
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
pep 8 에선 단순 getter, setter는 별도의 함수로 제공하기 보단 노출하는 것을 가이드해서 변경해주었습니다. https://github.com/DaleStudy/leetcode-study/commit/75410ea130cd0a2d5b1cc25cabe27b4db89813b9    

`For simple public data attributes, it is best to expose just the attribute name, without complicated accessor/mutator methods.` 
https://peps.python.org/pep-0008/#designing-for-inheritance
````

### review_comment · parkhojeong · 2026-08-02T06:07:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698071068
- ID: review_comment:3698071068
- 파일: valid-parentheses/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697128715

````text
set 없이 구현하도록 변경했습니다. https://github.com/DaleStudy/leetcode-study/pull/2792/commits/ce2ca44b19d0078c8f5acc77cc58c7d91d1f46ff
````

### review_comment · alphaorderly · 2026-08-02T06:08:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698072232
- ID: review_comment:3698072232
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
보통 객체지향 클래스에서 Getter와 Setter를 쓰는 가장 중요한 이유는 정보 은닉 때문이고
이때 자바 C++같은 언어는 은닉할 프로퍼티가 private 키워드를 사용하는것이니까요.
사실 파이썬은 Getter, Setter와는 안 어울리고 사용할 이유도 없는 언어라고 생각해요! 
````

### review_comment · parkhojeong · 2026-08-02T06:36:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698131609
- ID: review_comment:3698131609
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
전체적으로 정리해주었습니다. 중간 계층인 Trie는 불필요해서 제거해주었어요. https://github.com/DaleStudy/leetcode-study/pull/2792/commits/fb47ca2bacdd47d9d99d57877658a0c3a3e49c63
````

### review_comment · parkhojeong · 2026-08-02T06:46:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698151297
- ID: review_comment:3698151297
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
파이썬에서 getter, setter와 어울리지 않는다는건 어떤 말씀이실까요? 파이썬에도 접근 과정에서 제어나 동작이 필요한 부분은 property 를 사용하도록 권장되고 있고 필요하다고 봅니다.  https://docs.python.org/3/library/functions.html#property
클래스를 사용하면 OOP의 패러다임을 따라서 사용하는게 맞고 언어랑은 크게 상관 없다고 생각합니다.

````

### review_comment · alphaorderly · 2026-08-02T07:04:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2792#discussion_r3698189605
- ID: review_comment:3698189605
- 파일: design-add-and-search-words-data-structure/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3697109132

````text
제가 말씀드린 건 `property` 자체가 불필요하다는 의미라기보다는, 정보 은닉을 목적으로 모든 필드에 단순 getter와 setter를 만드는 방식은 Python의 관례와 잘 맞지 않는다는 의미였습니다.

Python에서는 단순한 public 데이터라면 그대로 노출하는 편을 권장하고, 이후 값의 검증이나 변환, 계산처럼 접근 과정에 별도의 동작이 필요해졌을 때 `property`를 사용하는 방식이 일반적이라고 알고 있습니다.

따라서 `property`는 Java나 C++의 `private` 필드를 감싸는 전통적인 getter/setter와 완전히 같은 개념이라기보다는, 기존의 프로퍼티 접근 문법을 유지하면서 그 과정에 로직을 끼워 넣는 관리형 속성 또는 훅에 더 가깝다고 생각합니다.

객체지향의 원칙 자체는 언어와 무관할 수 있지만, 이를 표현하는 방식과 관례는 언어마다 다르기 때문에 Python에서는 Python의 관례에 맞게 사용하는 것이 자연스럽다고 봅니다.

마지막으로 공식 문서를 근거로 말씀해 주시는 부분은 저도 충분히 이해하고 있습니다! 다만 지금 논의하는 내용은 기능의 존재 여부보다는 그 기능을 어떤 맥락에서 사용하는 것이 자연스러운지에 관한 부분이라, 문서 링크를 계속 인용하는 방식보다는 서로의 해석과 근거를 중심으로 이야기해 보면 좋을 것 같습니다.
````

## [#2793 [alphaorderly] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2793)

### review_comment · alphaorderly · 2026-08-02T01:21:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#discussion_r3697194041
- ID: review_comment:3697194041
- 파일: unique-paths/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
2D DP에서 dp 내용을 출력하고
대각선으로 보면 Pascal Triangle이 만들어집니다.
이것대로 Combination 연산으로 하셔도 맨 아래 코드를 얻을수 있으세요!
````

### review_comment · parkhojeong · 2026-08-07T16:10:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#discussion_r3737135330
- ID: review_comment:3737135330
- 파일: longest-substring-without-repeating-characters/alphaorderly.py, 줄: 22, 원래 줄: 22

````text
left를 하나씩 옮기지 않고 중복되는 인덱스 바로 다음으로 옮겨주는 방식으로 최적화 해볼 수 있을 거 같네요
````

### review_comment · parkhojeong · 2026-08-07T16:17:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#discussion_r3737181350
- ID: review_comment:3737181350
- 파일: set-matrix-zeroes/alphaorderly.py, 줄: None, 원래 줄: 18

````text
row_check, col_check가 어떤 의미인지 알기는 어려운 거 같아서 적절한 네이밍 해주시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-07T16:28:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#discussion_r3737242477
- ID: review_comment:3737242477
- 파일: unique-paths/alphaorderly.py, 줄: 53, 원래 줄: 53

````text
오 이렇게도 풀 수 있군요. 패턴이 있는 거 같아 보이긴 했는데 수식 도출이 잘 안되더라구요. 이런 풀이 아이디어는 어떻게 얻으셨는지 궁금하네요.
````

### review · parkhojeong · 2026-08-07T16:31:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#pullrequestreview-4884556724
- ID: review:4884556724
- 리뷰 상태: COMMENTED

````text
수고하셨습니다. 풀이와 관계 없는 커밋은 정리 부탁드립니다.
````

### review_comment · parkhojeong · 2026-08-07T17:08:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#discussion_r3737470319
- ID: review_comment:3737470319
- 파일: reverse-linked-list/alphaorderly.py, 줄: 23, 원래 줄: 23

````text
첫 노드를 가리키는 head가 순회하는 노드로 사용되어서 실제로는 두 가지 의미를 가지는 거 같습니다. 순회 중인 노드를 위한 별도의 변수를 사용하는게 어떨까요?
````

### issue_comment · alphaorderly · 2026-08-08T23:34:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2793#issuecomment-5228753482
- ID: issue_comment:5228753482

````text
@parkhojeong 
나중에 리뷰 부탁드려요! 코드 수정을 하니까 다시 취소가 되었네요

````

## [#2794 [freemjstudio] WEEK 06 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2794)

### review_comment · njngwn · 2026-08-02T11:06:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2794#discussion_r3698791301
- ID: review_comment:3698791301
- 파일: valid-parentheses/freemjstudio.py, 줄: 20, 원래 줄: 20

````text
이 조건들을 전부 묶어도 괜찮을 것 같네요!
````

### review_comment · njngwn · 2026-08-02T11:06:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2794#discussion_r3698792333
- ID: review_comment:3698792333
- 파일: valid-parentheses/freemjstudio.py, 줄: 2, 원래 줄: 2

````text
시간복잡도와 공간복잡도를 따로 적어놔도 좋을 것 같습니다!
````

### review_comment · njngwn · 2026-08-02T11:07:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2794#discussion_r3698793793
- ID: review_comment:3698793793
- 파일: valid-parentheses/freemjstudio.py, 줄: 2, 원래 줄: 2

````text
전체적으로 코드가 깔끔하고 좋네요! 수고하셨습니다~
````

### review_comment · parkhojeong · 2026-08-02T14:03:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2794#discussion_r3699274646
- ID: review_comment:3699274646
- 파일: valid-parentheses/freemjstudio.py, 줄: 6, 원래 줄: 6

````text
한 개인 경우 뿐 아니라 홀수인 경우로 최적화가 가능할 거 같네요.
````

### review · parkhojeong · 2026-08-02T14:07:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2794#pullrequestreview-4838702878
- ID: review:4838702878
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

### issue_comment · parkhojeong · 2026-08-02T14:09:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2794#issuecomment-5158426438
- ID: issue_comment:5158426438

````text
@freemjstudio pr 제목과 프로젝트 주차 확인 부탁드립니다. 
````

## [#2795 [parkhojeong] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2795)

### review_comment · alphaorderly · 2026-08-05T04:50:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3718022827
- ID: review_comment:3718022827
- 파일: set-matrix-zeroes/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
이거 재귀때문에 공간복잡도 O(max(m, n)) 일텐데 패턴분석이 이상하게 되어 있네요
훨씬 간단한 공간복잡도 O(1) 풀이도 있어요! 
````

### review_comment · alphaorderly · 2026-08-05T04:54:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3718037670
- ID: review_comment:3718037670
- 파일: unique-paths/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maze = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                maze[i][j] = maze[i - 1][j] + maze[i][j - 1]

        return maze[m - 1][n - 1]
```

칸 채운다고 생각하시면 복잡한 if 없이도 충분히 가능하세요!

그리고
1. 공간복잡도 O(n)
2. 공간복잡도 O(1)

인 풀이도 있으니까 해보시면 좋을것 같네요
````

### review_comment · alphaorderly · 2026-08-05T05:00:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3718060148
- ID: review_comment:3718060148
- 파일: unique-paths/parkhojeong.py, 줄: None, 원래 줄: 4

````text
이 부분을 이렇게 만드시면 동일한 `row` 객체의 레퍼런스가 행의 개수만큼 반복됩니다. 따라서 한 행의 열 값을 변경하면 다른 모든 행의 값도 함께 바뀌는 대참사가 일어날 수 있어요.

예를 들면 아래 코드는:

```python
a = [0] * 5
b = [a] * 5

a[1] = 1

print(*b, sep="\n")
```

다음과 같이 모든 행의 두 번째 값이 함께 변경됩니다.

```text
[0, 1, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 1, 0, 0, 0]
[0, 1, 0, 0, 0]
```

각 행을 독립적인 리스트로 만들려면 리스트 컴프리헨션을 사용하는 것이 안전합니다.

```python
grid = [[0] * m for _ in range(n)]
```

다만 현재 풀이가 정상적으로 작동한 원리는 1차원 DP를 활용하는 방식과 정확히 동일합니다. 따라서 여기서 공간 복잡도를 최적화하는 아이디어도 자연스럽게 떠올리실 수 있을 것 같아요!

````

### review_comment · alphaorderly · 2026-08-05T05:20:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3718146229
- ID: review_comment:3718146229
- 파일: reverse-linked-list/parkhojeong.py, 줄: None, 원래 줄: 11

````text
next는 파이썬 내장 함수랑 이름이 겹쳐서 ( 아마 leetcode에서도 색상으로 다르게 보이실거에요 )
사용을 자제하시는게 어떠실까 싶습니다.
````

### review_comment · alphaorderly · 2026-08-05T05:20:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3718149006
- ID: review_comment:3718149006
- 파일: set-matrix-zeroes/parkhojeong.py, 줄: None, 원래 줄: 18

````text
파이썬이라 가능하다지만, 정수 행렬에 문자열을 넣는것은 좀 별로이지 않을까 싶습니다.
````

### review_comment · alphaorderly · 2026-08-05T11:30:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3720176915
- ID: review_comment:3720176915
- 파일: longest-substring-without-repeating-characters/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        ch_to_idx = {}
        start_idx = 0

        i = 0
        length_of_longest_substring = 1

        for i, ch in enumerate(s):
            if ch in ch_to_idx and ch_to_idx[ch] >= start_idx:
                start_idx = ch_to_idx[ch] + 1

            ch_to_idx[ch] = i
            length_of_longest_substring = max(i - start_idx + 1, length_of_longest_substring)


        return length_of_longest_substring
```

제 생각엔 ans를 구하는것을 따로 분리해서 분기에 공통로직이 많은것 보다는 이렇게

경우를 크게 따지지 않고 전부 하는게 가독성이 좋지 않을까 라는 의견이 있습니다.

2개의 항목을 가지는 max 함수는  O(1)의 시간복잡도를 가지기 때문에 O(N) 루프 안에 돌려도 큰 성능상 문제가 없을것으로 보여서요
````

### review_comment · parkhojeong · 2026-08-06T17:47:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3730911112
- ID: review_comment:3730911112
- 파일: reverse-linked-list/parkhojeong.py, 줄: None, 원래 줄: 11
- 답글 대상: review_comment:3718146229

````text
감사합니다. 다른 이름으로 변경 해주었습니다.
````

### review_comment · parkhojeong · 2026-08-06T17:49:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3730917791
- ID: review_comment:3730917791
- 파일: unique-paths/parkhojeong.py, 줄: None, 원래 줄: 4
- 답글 대상: review_comment:3718060148

````text
짚어주셔서 감사합니다. 가끔씩 실수하는 부분인데 우연히 통과됐네요. 한 칼럼씩 계산하는 방식으로 풀이 업데이트 해보았습니다.
````

### review_comment · parkhojeong · 2026-08-06T17:49:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3730920042
- ID: review_comment:3730920042
- 파일: unique-paths/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3718037670

````text
O(1)으로도 풀어보겠습니다. 감사합니다.
````

### review_comment · parkhojeong · 2026-08-06T17:50:33Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3730924825
- ID: review_comment:3730924825
- 파일: set-matrix-zeroes/parkhojeong.py, 줄: None, 원래 줄: 18
- 답글 대상: review_comment:3718149006

````text
같은 타입 중 입력 값 범위에 해당하지 않는 sys.maxsize 쓰도록 변경했습니다. 
````

### review_comment · JeonJe · 2026-08-08T07:52:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3740287417
- ID: review_comment:3740287417
- 파일: number-of-islands/parkhojeong.py, 줄: 4, 원래 줄: 4

````text
저도 이번에 DFS로 풀면서 재귀 깊이가 걸렸던 부분이라 공유드려요 🙂

  grid를 "0"으로 덮어 visited를 없앤 건 깔끔한데, 재귀 깊이가 섬 크기(= 칸 수)에 비례해서 제약(m, n <= 300)상 최악 90,000이 쌓일 수 있을 것 같아요 파이썬 기본 재귀 한도는 1,000으로 알고있습니다! 채점 케이스에 이만한 단일 섬이 없어서 통과한 것 같아요.

 deque로 반복 BFS(또는 명시적 스택)로 바꾸면 좌표가 콜 시간복잡도는 O(m·n)으로 해결 가능할 것 같습니다!!
````

### review_comment · parkhojeong · 2026-08-08T14:15:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2795#discussion_r3740837308
- ID: review_comment:3740837308
- 파일: number-of-islands/parkhojeong.py, 줄: 4, 원래 줄: 4
- 답글 대상: review_comment:3740287417

````text
재귀 한도 고려해서 interactive dfs 로 다시 풀어보았습니다. 감사합니다
````

## [#2796 [JeonJe] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2796)

### review_comment · parkhojeong · 2026-08-07T16:43:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3737326251
- ID: review_comment:3737326251
- 파일: longest-substring-without-repeating-characters/JeonJe.java, 줄: 11, 원래 줄: 11

````text
의미를 드러내는 네이밍 사용하시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-07T16:46:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3737348147
- ID: review_comment:3737348147
- 파일: longest-substring-without-repeating-characters/JeonJe.java, 줄: 19, 원래 줄: 19

````text
각 문자의 인덱스를 저장해두면 중복 발생시 한 칸씩 옮기지 않아도 되서 최적화가 가능할 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-07T16:51:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3737376205
- ID: review_comment:3737376205
- 파일: number-of-islands/JeonJe.java, 줄: 15, 원래 줄: 15

````text
사소하지만 복잡도 표기는 m * n 인데 변수 순서는 n, m이라서 순서가 왜 바뀌어있지 생각이 들었습니다. for loop에서도 m부터 나와서 m, n 순서로 선언되면 좀 더 자연스러울 거 같은데 n, m 순서로 쓰신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-08-07T16:53:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3737389847
- ID: review_comment:3737389847
- 파일: number-of-islands/JeonJe.java, 줄: 17, 원래 줄: 17

````text
in-place 마킹하는 방식도 고려하셨을 거 같은데 혹시 이 문제에서 visited 를 사용하신 이유가 있을까요?
````

### review · parkhojeong · 2026-08-07T17:01:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#pullrequestreview-4884817392
- ID: review:4884817392
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 항상 깔끔한 풀이 올려주셔서 감사합니다. 사소한 커멘트 몇 개 남겼습니다.
````

### review_comment · JeonJe · 2026-08-08T07:55:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3740292187
- ID: review_comment:3740292187
- 파일: longest-substring-without-repeating-characters/JeonJe.java, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3737326251

````text
temp보다 창 안에 들어있는 문자들이니 window나 charsInWindow가 더 좋은 네이밍 같네요.
감사합니다!
````

### review_comment · JeonJe · 2026-08-08T07:56:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3740293263
- ID: review_comment:3740293263
- 파일: longest-substring-without-repeating-characters/JeonJe.java, 줄: 19, 원래 줄: 19
- 답글 대상: review_comment:3737348147

````text
  Map<Character, Integer>로 마지막 인덱스를 들고 있으면 left = Math.max(left, idx + 1)로 한 번에 점프할 수 있겠네요.

 안쪽 루프가 사라져서 상수도 줄고 읽기도 더 좋을 것 같습니다. 감사합니다

````

### review_comment · JeonJe · 2026-08-08T08:00:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3740299256
- ID: review_comment:3740299256
- 파일: number-of-islands/JeonJe.java, 줄: 15, 원래 줄: 15
- 답글 대상: review_comment:3737376205

````text
습관적으로 n, m을 행으로 뒀는데 헷갈리지 않게 다른 변수를 쓰는 방향을 고려해야겠네요 감사합니다!


````

### review_comment · JeonJe · 2026-08-08T08:02:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2796#discussion_r3740301183
- ID: review_comment:3740301183
- 파일: number-of-islands/JeonJe.java, 줄: 17, 원래 줄: 17
- 답글 대상: review_comment:3737389847

````text
요 부분도 조금 습관적으로 visited 배열을 사용했는데 리뷰해주신대로 inplace 방식으로 grid를 업데이트 하는게 더 좋았을 것 같네요.
감사합니다!!
````

## [#2798 [ICE0208] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2798)

### review_comment · dolphinflow86 · 2026-08-08T02:51:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2798#discussion_r3739803615
- ID: review_comment:3739803615
- 파일: longest-substring-without-repeating-characters/ICE0208.java, 줄: 5, 원래 줄: 5

````text
문제에서 주어지는 입력값인 아스키 코드 값 범위로 제한두신것이 인상적이네요!
저는 set을 사용했는데 spacial locality, 캐시 히트율 등에서도 배열로 구현한게 더 좋아보입니다.
````

### review_comment · dolphinflow86 · 2026-08-08T02:59:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2798#discussion_r3739814642
- ID: review_comment:3739814642
- 파일: unique-paths/ICE0208.java, 줄: 16, 원래 줄: 16

````text
깔끔하게 잘 풀여주셨네요. 다만 시간, 공간복잡도 분석을 주석에 같이 써주시면 좋을 것 같습니다!
````

### review · dolphinflow86 · 2026-08-08T02:59:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2798#pullrequestreview-4887920251
- ID: review:4887920251
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

### review_comment · ICE0208 · 2026-08-08T10:13:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2798#discussion_r3740480190
- ID: review_comment:3740480190
- 파일: unique-paths/ICE0208.java, 줄: 16, 원래 줄: 16
- 답글 대상: review_comment:3739814642

````text
리뷰 감사합니다!  🙌
다음주 문제풀이부터는 주석에 복잡도도 분석해서 남겨놓아야겠네요 🫡
````

## [#2799 [dolphinflow86] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2799)

### review_comment · alphaorderly · 2026-08-06T13:11:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3729039586
- ID: review_comment:3729039586
- 파일: reverse-linked-list/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
제 개인적인 생각에는요! head를 리턴 혹은 어디에도 쓰지 않으니 current를 쓰시는 부분 그대로 head를 쓰셔도 되지 않을까?
하는 생각이 들어요!

그리고 파이썬의 `a, b = b, a`처럼 쓸수 있는 문법을 활용하시면 while loop 안을 1줄로 줄이실수도 있답니다!
````

### review_comment · dolphinflow86 · 2026-08-07T15:17:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3736790741
- ID: review_comment:3736790741
- 파일: reverse-linked-list/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3729039586

````text
오 그렇네요!

리뷰 받으면서 파이썬 문법에 조금씩 익숙해지는 것 같습니다.

리뷰 감사합니다.
````

### review_comment · parkhojeong · 2026-08-07T17:15:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3737515253
- ID: review_comment:3737515253
- 파일: number-of-islands/dolphinflow86.py, 줄: 17, 원래 줄: 17

````text
python의 `a <= x < b` 쓰면 이런 형태도 가능한데 or 사용해주신게 더 명확한 거 같기는 하네요.
```
if not (
    0 <= row < rows 
    and 0 <= col < cols 
    and grid[row][col] == "1"
):
```

````

### review_comment · parkhojeong · 2026-08-07T17:16:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3737520017
- ID: review_comment:3737520017
- 파일: number-of-islands/dolphinflow86.py, 줄: None, 원래 줄: 8

````text
rows, cols가 길이로 보이지 않고 배열 같은 변수가 담기는 거처럼 보이는 거 같습니다. 길이를 나타내는 네이밍을 사용하시면 어떨까요?
````

### review_comment · parkhojeong · 2026-08-07T17:18:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3737529168
- ID: review_comment:3737529168
- 파일: reverse-linked-list/dolphinflow86.py, 줄: 13, 원래 줄: 13

````text
next가 예약어여서 _node를 붙여주신 거 같네요. 다른 네이밍들이랑 일관성을 맞추시는 건 어떨까요?
````

### review_comment · parkhojeong · 2026-08-07T17:21:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3737545165
- ID: review_comment:3737545165
- 파일: longest-substring-without-repeating-characters/dolphinflow86.py, 줄: 14, 원래 줄: 14

````text
left를 하나씩 증가하지 않고 각 문자의 인덱스를 저장해서 점프하는 방식으로도 조금 더 최적화가 가능하니 풀어보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-08-07T17:21:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#pullrequestreview-4885045965
- ID: review:4885045965
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

### review_comment · yuseok89 · 2026-08-08T05:32:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3740078167
- ID: review_comment:3740078167
- 파일: number-of-islands/dolphinflow86.py, 줄: 25, 원래 줄: 25

````text
코드 자체는 깔끔해지는데, 사전에 체크해서 쌓지 않아도 될 call stack 이 쌓이는 부분은 있는 것 같습니다.
````

### review_comment · yuseok89 · 2026-08-08T05:34:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3740087214
- ID: review_comment:3740087214
- 파일: unique-paths/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
재귀 DP + 메모이제이션으로 잘 구현해주신 것 같습니다.
````

### review_comment · yuseok89 · 2026-08-08T05:37:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#discussion_r3740096489
- ID: review_comment:3740096489
- 파일: unique-paths/dolphinflow86.py, 줄: 6, 원래 줄: 6

````text
dfs 함수를 uniquePaths 안에 구현하면, 인자 개수를 줄일 수 있을 것 같습니다.
````

### review · yuseok89 · 2026-08-08T05:38:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2799#pullrequestreview-4888216230
- ID: review:4888216230
- 리뷰 상태: APPROVED

````text
코멘트가 몇 개 있긴한데, 큰 부분은 아니라 approve 합니다.
코멘트는 시간 있을 때 여유롭게 봐주세요.
한 주 고생 많으셨습니다 👍 💯 
````

## [#2800 [yuseok89] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2800)

### review_comment · parkhojeong · 2026-08-07T17:27:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3737580330
- ID: review_comment:3737580330
- 파일: reverse-linked-list/yuseok89.py, 줄: None, 원래 줄: 15

````text
next는 파이썬의 내장 함수라 다른 변수명을 사용하시는게 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-07T17:30:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3737595635
- ID: review_comment:3737595635
- 파일: unique-paths/yuseok89.py, 줄: None, 원래 줄: 13

````text
세미콜론이 잘못 들어가 있네요
```suggestion
        return cnt[n - 1]
```
````

### review_comment · parkhojeong · 2026-08-07T17:34:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3737617611
- ID: review_comment:3737617611
- 파일: longest-substring-without-repeating-characters/yuseok89.py, 줄: None, 원래 줄: 8

````text
`for r in ...` 때문에 여기 r = 0 할당은 불필요한 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-07T17:40:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3737648953
- ID: review_comment:3737648953
- 파일: longest-substring-without-repeating-characters/yuseok89.py, 줄: None, 원래 줄: 14

````text
left를 한 칸씩 이동하고 있는데 각 문자의 인덱스를 활용하면 조금 더 최적화가 가능할 거 같습니다.
````

### review · parkhojeong · 2026-08-07T17:40:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#pullrequestreview-4885131558
- ID: review:4885131558
- 리뷰 상태: COMMENTED

````text
수고하셨습니다.
````

### review_comment · parkhojeong · 2026-08-07T17:41:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3737657983
- ID: review_comment:3737657983
- 파일: longest-substring-without-repeating-characters/yuseok89.py, 줄: None, 원래 줄: 2

````text
공간 복잡도 표기가 잘못되어 있네요. 수정 부탁드립니다
````

### review_comment · yuseok89 · 2026-08-08T05:25:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740065860
- ID: review_comment:3740065860
- 파일: reverse-linked-list/yuseok89.py, 줄: None, 원래 줄: 15
- 답글 대상: review_comment:3737580330

````text
수정했습니다.
감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-08-08T05:26:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740066578
- ID: review_comment:3740066578
- 파일: unique-paths/yuseok89.py, 줄: None, 원래 줄: 13
- 답글 대상: review_comment:3737595635

````text
언어를 왔다갔다하다보니 들어가버렸네요 ㅠ 수정했습니다. 감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-08-08T05:26:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740067260
- ID: review_comment:3740067260
- 파일: longest-substring-without-repeating-characters/yuseok89.py, 줄: None, 원래 줄: 8
- 답글 대상: review_comment:3737617611

````text
풀이 방식을 바꾸면서 코드 전체가 바뀌었습니다.
감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-08-08T05:26:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740067781
- ID: review_comment:3740067781
- 파일: longest-substring-without-repeating-characters/yuseok89.py, 줄: None, 원래 줄: 14
- 답글 대상: review_comment:3737648953

````text
좋은 방법이네요 ! 배웠습니다.
감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-08-08T05:27:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740068129
- ID: review_comment:3740068129
- 파일: longest-substring-without-repeating-characters/yuseok89.py, 줄: None, 원래 줄: 2
- 답글 대상: review_comment:3737657983

````text
수정했습니다.
감사합니다 🙏 
````

### review_comment · daehyun99 · 2026-08-08T05:45:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740110303
- ID: review_comment:3740110303
- 파일: number-of-islands/yuseok89.py, 줄: 7, 원래 줄: 7

````text
참고로만 말씀드리면, 문제에서의 `m`과 `n`의 의미와 반대로네요.
````

### review_comment · daehyun99 · 2026-08-08T05:49:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740116476
- ID: review_comment:3740116476
- 파일: set-matrix-zeroes/yuseok89.py, 줄: 10, 원래 줄: 10

````text
> 참고로만 말씀드리면, 문제에서의 `m`과 `n`의 의미와 반대로네요.

여기도요!
````

### review_comment · daehyun99 · 2026-08-08T05:52:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#discussion_r3740120844
- ID: review_comment:3740120844
- 파일: unique-paths/yuseok89.py, 줄: 1, 원래 줄: 1

````text
오 이런 방법으로도 풀 수 있군요! 많이 배워갑니다.
````

### review · daehyun99 · 2026-08-08T05:53:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2800#pullrequestreview-4888259695
- ID: review:4888259695
- 리뷰 상태: APPROVED

````text
이번 주도 고생 많으셨습니다!!!
````

## [#2801 [daehyun99] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2801)

### review_comment · alphaorderly · 2026-08-07T16:42:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3737320288
- ID: review_comment:3737320288
- 파일: longest-substring-without-repeating-characters/daehyun99.py, 줄: 8, 원래 줄: 8

````text
해당 로직이 하단의 while과 겹치지 않을까요?
중복 로직을 제거할수 있을것 같아요!
````

### review_comment · alphaorderly · 2026-08-07T16:42:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3737324966
- ID: review_comment:3737324966
- 파일: reverse-linked-list/daehyun99.py, 줄: 1, 원래 줄: 1

````text
해당 문제는 조금 더 코드 라인 수를 확 줄일수 있는 문제에요!
시도 한번 해보시는것도 좋겠어요!
````

### review_comment · daehyun99 · 2026-08-08T06:04:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3740138623
- ID: review_comment:3740138623
- 파일: longest-substring-without-repeating-characters/daehyun99.py, 줄: 8, 원래 줄: 8
- 답글 대상: review_comment:3737320288

````text
문제 풀 때, `longest = max(longest, len(seen))` 코드가 문자열 제거 없이 추가만 되는 상황에만 실행되도록 하고 싶어서, 위처럼 작성했었습니다!

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        longest = 0

        for c in s:
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            longest = max(longest, len(seen))
        return longest

```

적용했더니 확실히 더 깔끔해지는군요! 성능도 크게 차이는 나지 않는 것 같습니다!
````

### review_comment · daehyun99 · 2026-08-08T06:07:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3740142345
- ID: review_comment:3740142345
- 파일: reverse-linked-list/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3737324966

````text
수정했습니다!

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        return prv
```
````

### review_comment · dahyeong-yun · 2026-08-08T11:28:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3740581192
- ID: review_comment:3740581192
- 파일: number-of-islands/daehyun99.py, 줄: 11, 원래 줄: 11

````text
방문처리를 스택으로 하는 방법도 있네요. 재귀 보다 디버그가 더 편할 수 있겠네요 👍🏼 
````

### review_comment · dahyeong-yun · 2026-08-08T11:40:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3740598678
- ID: review_comment:3740598678
- 파일: unique-paths/daehyun99.py, 줄: 3, 원래 줄: 3

````text
m = 3, n = 7 인경우 다음과 같이 더해가면서 테이블을 만드는 것 같은데요.

m/n | 0 | 1 | 2 | 3 | 4 | 5 | 6
-- | -- | -- | -- | -- | -- | -- | --
0 | 1 | 1 | 1 | 1 | 1 | 1 | 1
1 | 1 | 2 | 3 | 4 | 5 | 6 | 7
2 | 1 | 3 | 6 | 10 | 15 | 21 | 28

이 경우에 그럼 초기에 x = 0, y = 0인 경우는 무조건 1이되니까 애초에 1로 초기화 하면 분기를 좀 줄일 수 있지 않을 까 싶네요.

````

### review · dahyeong-yun · 2026-08-08T11:42:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#pullrequestreview-4888721984
- ID: review:4888721984
- 리뷰 상태: APPROVED

````text
고생하셨습니다! 다른 분과 리뷰하면서 개선안까지 보여주셔서 공부가 많이 됐습니다 👍🏼 
````

### review_comment · parkhojeong · 2026-08-09T02:21:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3742341846
- ID: review_comment:3742341846
- 파일: longest-substring-without-repeating-characters/daehyun99.py, 줄: 14, 원래 줄: 14

````text
방문한 문자의 인덱스를 사용하면 한 칸씩 이동하는걸 점프하는 형태로 변경이 가능하니 풀어보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-09T02:26:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3742353519
- ID: review_comment:3742353519
- 파일: set-matrix-zeroes/daehyun99.py, 줄: 11, 원래 줄: 11

````text
in 연산이 별도로 있어서 O(n) 만큼의 시간이 더 필요해지는데요. 내부 포문에서 maxtrix[i][j] == 0 인 경우를 체크하고 있으므로 col과 같이 row 로직을 처리해도 좋을 거 같습니다. 의도하신 바도 0이 보이면 해당 로우와 칼럼을 set에 넣어주는 것으로 보여서요.
````

### review_comment · parkhojeong · 2026-08-09T02:28:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3742357333
- ID: review_comment:3742357333
- 파일: set-matrix-zeroes/daehyun99.py, 줄: 14, 원래 줄: 14

````text
칼럼 로직은 in-place인데 로우 로직은 배열을 만들어 할당하는 방식을 사용하신 이유가 있을까요?
````

### review_comment · parkhojeong · 2026-08-09T02:32:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3742366022
- ID: review_comment:3742366022
- 파일: reverse-linked-list/daehyun99.py, 줄: 18, 원래 줄: 18

````text
사용하는 포인터가 3개인데 right, left, pointer 라는 이름이 어떤 값들인지 알기가 조금 어려웠던 거 같습니다. 현재 보고 있는 포인터를 기준으로 이전 노드와 다음 노드만을 사용하니 의미를 드러내도록 네이밍을 하시는 건 어떨까요? 
````

### review_comment · parkhojeong · 2026-08-09T02:37:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#discussion_r3742376854
- ID: review_comment:3742376854
- 파일: unique-paths/daehyun99.py, 줄: 4, 원래 줄: 4

````text
계산 과정에서 이전 칼럼만 필요해서 칼럼 하나만을 가지고 1차원 dp 로 풀어보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-08-09T02:37:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2801#pullrequestreview-4890335731
- ID: review:4890335731
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2802 [dahyeong-yun] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2802)

### review_comment · alphaorderly · 2026-08-07T16:49:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#discussion_r3737361696
- ID: review_comment:3737361696
- 파일: unique-paths/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
오오 회원님은 해당 로직 어떻게 찾아내셨나요?
````

### review_comment · dahyeong-yun · 2026-08-08T01:13:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#discussion_r3739623683
- ID: review_comment:3739623683
- 파일: unique-paths/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3737361696

````text
길찾기 그림이 어렸을 떄 순열 조합 풀던거랑 비슷한 거 같아서 해봤어요 :) 아래로 가는 화살표와 오른쪽으로 가는 화살표의 조합으로 풀었는데 처음엔 숫자가 너무 커서 오버플로우가 되는 경우가 있더라구요. 그래서 힌트를 좀 얻었는데 연속된 k개의 숫자 곱은 k!로 나누어 떨어지기 때문에 매 루프마다 나누는 식으로 오버플로우를 없애는 식으로 풀어봤습니다.
````

### review_comment · parkhojeong · 2026-08-08T17:03:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#discussion_r3741144575
- ID: review_comment:3741144575
- 파일: number-of-islands/dahyeong-yun.java, 줄: 41, 원래 줄: 41

````text
재귀 깊이가 최대 m x n 까지 가능해서 재귀를 사용하지 않고 풀어보시면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-08T17:06:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#discussion_r3741153494
- ID: review_comment:3741153494
- 파일: number-of-islands/dahyeong-yun.java, 줄: 23, 원래 줄: 23

````text
cover라는 함수명이 무엇을 하는지 드러나는 거 같지는 않아서 의미가 드러나도록 바꿔주면 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-08T17:09:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#discussion_r3741159980
- ID: review_comment:3741159980
- 파일: unique-paths/dahyeong-yun.java, 줄: 10, 원래 줄: 10

````text
주석에 있는 n과  변수의 n 이 같은 단어인데 다른 의미로 쓰이는 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-08T17:14:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#discussion_r3741168317
- ID: review_comment:3741168317
- 파일: unique-paths/dahyeong-yun.java, 줄: 17, 원래 줄: 17

````text
어떤 의도로 푸셨는지 코드로 많이 드러나있던 거 같습니다. 덕분에 비교적 쉽게 이해할 수 있었던 거 같아요.
````

### review · parkhojeong · 2026-08-08T17:14:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2802#pullrequestreview-4889256997
- ID: review:4889256997
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 사소한 커멘트 몇 개 남겼습니다. 
````

## [#2803 [Chanz] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2803)

### review_comment · okyungjin · 2026-08-08T08:53:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2803#discussion_r3740371443
- ID: review_comment:3740371443
- 파일: reverse-linked-list/Chanz82.py, 줄: 9, 원래 줄: 9

````text
8라인이 필요할까요? 바로 아래 코드에서 `head`로 덮어써지네요
````

### review · okyungjin · 2026-08-08T08:54:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2803#pullrequestreview-4888513685
- ID: review:4888513685
- 리뷰 상태: APPROVED

````text
풀이 잘 봤습니다. 이후에 확인이 어려워서 승인처리해요.
이번 주도 고생하셨습니다! 다음 주도 파이팅하세요 : ) 
````

### review_comment · parkhojeong · 2026-08-08T11:35:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2803#discussion_r3740591738
- ID: review_comment:3740591738
- 파일: reverse-linked-list/Chanz82.py, 줄: 12, 원래 줄: 12

````text
dummy는 어떤 값이 담기는지 알기가 어려운데요. 의미에 맞는 네이밍을 하시는 건 어떨까요?
````

### review · parkhojeong · 2026-08-08T11:36:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2803#pullrequestreview-4888731388
- ID: review:4888731388
- 리뷰 상태: APPROVED

````text
수고하셨습니다 
````

### review_comment · parkhojeong · 2026-08-08T11:39:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2803#discussion_r3740596489
- ID: review_comment:3740596489
- 파일: longest-substring-without-repeating-characters/Chanz82.py, 줄: 5, 원래 줄: 5

````text
visited는 단순히 방문했던 것만 담는 것처럼 느껴지는데요. 인덱스를 담는다는 걸 나타내는 건 어떨까요? 
````

## [#2805 [sangbeenmoon] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2805)

### review_comment · ICE0208 · 2026-08-08T10:29:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#discussion_r3740500855
- ID: review_comment:3740500855
- 파일: number-of-islands/sangbeenmoon.py, 줄: 44, 원래 줄: 44

````text
별도의 visited 배열을 사용하지 않고, 방문한 grid의 값을 직접 변경하는 in-place 방식으로도 최적화가 가능해 보입니다!
````

### review_comment · ICE0208 · 2026-08-08T10:39:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#discussion_r3740514992
- ID: review_comment:3740514992
- 파일: set-matrix-zeroes/sangbeenmoon.py, 줄: 50, 원래 줄: 50

````text
matrix[0][0]을 첫 번째 행의 마커처럼 활용하면 set_zero_first_row 같은 별도의 변수 없이도 처리할 수 있었군요! 🫢
````

### review_comment · ICE0208 · 2026-08-08T10:41:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#discussion_r3740516964
- ID: review_comment:3740516964
- 파일: unique-paths/sangbeenmoon.py, 줄: 25, 원래 줄: 25

````text
현재 2차원 DP를 사용하고 있는데, 1차원 DP로 공간 복잡도를 최적화해서 풀어보셔도 좋을 것 같습니다!
````

### review · ICE0208 · 2026-08-08T10:45:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#pullrequestreview-4888638220
- ID: review:4888638220
- 리뷰 상태: APPROVED

````text
고생 많으셨습니다! 몇 가지 코멘트 남겨두었습니다~ 🙂
````

### review_comment · parkhojeong · 2026-08-08T11:24:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#discussion_r3740575900
- ID: review_comment:3740575900
- 파일: longest-substring-without-repeating-characters/sangbeenmoon.py, 줄: 28, 원래 줄: 28

````text
적절한 네이밍 해주시면 좋을 거 같습니다
````

### review_comment · parkhojeong · 2026-08-08T11:24:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#discussion_r3740576502
- ID: review_comment:3740576502
- 파일: longest-substring-without-repeating-characters/sangbeenmoon.py, 줄: 40, 원래 줄: 40

````text
로그는 제거 부탁드립니다
````

### review · parkhojeong · 2026-08-08T11:32:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2805#pullrequestreview-4888717444
- ID: review:4888717444
- 리뷰 상태: COMMENTED

````text
수고하셨습니다
````

## [#2806 [freemjstudio] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2806)

### review · parkhojeong · 2026-08-08T13:51:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2806#pullrequestreview-4888916153
- ID: review:4888916153
- 리뷰 상태: APPROVED

````text
수고하셨습니다
````

### review · parkhojeong · 2026-08-08T14:16:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2806#pullrequestreview-4888962528
- ID: review:4888962528
- 리뷰 상태: CHANGES_REQUESTED

````text
주차 설정, pr 제목 등 pr 체크리스트 항목들 확인 부탁드립니다. 
````

### issue_comment · parkhojeong · 2026-08-15T01:19:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2806#issuecomment-5299777617
- ID: issue_comment:5299777617

````text
@freemjstudio 커멘트 확인 부탁드립니다. 
````

### issue_comment · freemjstudio · 2026-08-17T10:17:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2806#issuecomment-5314771072
- ID: issue_comment:5314771072

````text
@parkhojeong 주차 설정 완료했습니다 !! 
````

## [#2807 [DaleSeo] WEEK 07 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2807)

### review_comment · parkhojeong · 2026-08-08T16:51:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2807#discussion_r3741119473
- ID: review_comment:3741119473
- 파일: number-of-islands/DaleSeo.rs, 줄: 10, 원래 줄: 10

````text
sink라는 이름도 직관적이고 함수로 분리하니 훨씬 가독성이 좋네요.
````

### review · parkhojeong · 2026-08-08T16:55:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2807#pullrequestreview-4889225412
- ID: review:4889225412
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2810 [alphaorderly] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2810)

### review_comment · alphaorderly · 2026-08-11T07:05:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#discussion_r3755901942
- ID: review_comment:3755901942
- 파일: longest-repeating-character-replacement/alphaorderly.py, 줄: 34, 원래 줄: 34

````text
이거 상수라 1이네요, O(N)이 시간복잡도입니다.
````

### review_comment · dahyeong-yun · 2026-08-14T22:43:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#discussion_r3787609511
- ID: review_comment:3787609511
- 파일: longest-repeating-character-replacement/alphaorderly.py, 줄: 56, 원래 줄: 56

````text
세그먼트 트리는 저한테는 좀 생소한 개념인데 흥미롭네요! 혹시 초기 트리가 4배 정도가 필요하다는 것이 어떤 식으로 도출이 됐는지 알 수 있을까요?
````

### review_comment · dahyeong-yun · 2026-08-14T22:46:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#discussion_r3787621559
- ID: review_comment:3787621559
- 파일: reverse-bits/alphaorderly.py, 줄: 6, 원래 줄: 6

````text
리턴할 수는 왼쪽으로 비트 연산하고, 원본 수는 오른쪽으로 비트 연산하면서 자연스럽게 거꾸로 비트가 쌓이네요. 비트 연산은 좀 감이 안와서 미루고 있었는데 덕분에 이해가 됐습니다!
````

### review_comment · dahyeong-yun · 2026-08-14T22:49:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#discussion_r3787632489
- ID: review_comment:3787632489
- 파일: clone-graph/alphaorderly.py, 줄: 22, 원래 줄: 22

````text
value가 unique 조건이 있으니, 간단히 인덱스로도 생성 여부를 기록하고 조회할 수 있네요. 좋은 아이디어네요! 
````

### review · dahyeong-yun · 2026-08-14T23:19:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#pullrequestreview-4941716966
- ID: review:4941716966
- 리뷰 상태: APPROVED

````text
항상 열정 가지고 하시는 모습에 동기 부여를 많이 받습니다! 이번 주 저는 못푼 문제가 많은데 코드 보면서 공부를 많이 하고 가네요~ 고생하셨습니다! 
````

### review_comment · alphaorderly · 2026-08-15T02:51:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#discussion_r3788306322
- ID: review_comment:3788306322
- 파일: longest-repeating-character-replacement/alphaorderly.py, 줄: 56, 원래 줄: 56
- 답글 대상: review_comment:3787609511

````text
세그먼트 트리의 원소 갯수는 반드시 4*N보다 작은데요, 혹시 모르니까 안전하게 + 1 해서 쓰는거에요!
````

### review_comment · alphaorderly · 2026-08-15T02:52:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2810#discussion_r3788308343
- ID: review_comment:3788308343
- 파일: reverse-bits/alphaorderly.py, 줄: 6, 원래 줄: 6
- 답글 대상: review_comment:3787621559

````text
맞습니다!
````

## [#2811 [dahyeong-yun] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2811)

### review_comment · alphaorderly · 2026-08-12T02:42:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2811#discussion_r3763218637
- ID: review_comment:3763218637
- 파일: reverse-bits/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
한번 쉬프트 연산자를 활용해보시는건 어떨까요?
방금 저도 자바로 풀어봤는데 11줄까지 코드를 줄일수 있었어요!
`if ((n & 1) == 1) answer |= 1;`
이런 느낌으로 연산이 됩니다.
````

### review_comment · alphaorderly · 2026-08-12T02:44:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2811#discussion_r3763224690
- ID: review_comment:3763224690
- 파일: reverse-bits/dahyeong-yun.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3763218637

````text
또한 쉬프트연산자 쓰시면 별도의 스택같은 자료형이 필요 없기때문에 성능도 좋을거에요!
````

### review_comment · JeonJe · 2026-08-14T15:01:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2811#discussion_r3784868990
- ID: review_comment:3784868990
- 파일: reverse-bits/dahyeong-yun.java, 줄: 8, 원래 줄: 8

````text
저는 시프트로 비트를 하나씩 꺼내 자리에 얹는 방식으로 풀었는데, 스택에 담았다가 반대로 꺼내는 접근도 있군요. "뒤집는다"는 동작이 스택에 그대로 드러나서 의도가 잘 읽혔습니다.

두 부분이 눈에 들어 왔는데,
1. getLast() 후 removeLast()는 pollLast() 하나로도 될 것 같습니다!
2. 그리고 answer += bit * Math.pow(2, j) 부분인데, Math.pow가 double을 반환하다 보니 암묵적 (int) 로 변환됩니다. 이 부분을 bit << j로 쓰면 정수 연산만으로 끝나서, 20만 건 기준으로는 333ms에서 35ms로 줄어들더라고요. 복잡도는 똑같이 O(1)이라 통과에는 영향이 없지만 상수 차이가 있어서 공유드려봅니다!
````

### review_comment · JeonJe · 2026-08-14T15:12:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2811#discussion_r3784954068
- ID: review_comment:3784954068
- 파일: longest-repeating-character-replacement/dahyeong-yun.java, 줄: 32, 원래 줄: 32

````text
코드 잘 읽었습니다!
count 26칸을 더한 total이 윈도우에 들어 있는 글자 수, 즉 윈도우 길이고, count[maxCountAlphabet]이 그 안에서 가장 많이 나온 문자의 개수네요. 
그래서 total - count[maxCountAlphabet] <= k가 "바꿔야 할 개수가 k 이하인가"로 표현이 되네요!

저는 위 부분을 left, right와 windowLength로 표현했는데, 이번에 카운트의 합으로 length를 표현할 수 있다는걸 배워갑니다!
````

### review_comment · dahyeong-yun · 2026-08-15T00:53:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2811#discussion_r3788035356
- ID: review_comment:3788035356
- 파일: reverse-bits/dahyeong-yun.java, 줄: 8, 원래 줄: 8
- 답글 대상: review_comment:3784868990

````text
와우.. 상세한 설명 감사해요. 고민이 거기까지 미치지 못했는데 시야가 넓어지는 느낌이네요!
````

## [#2812 [JeonJe] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2812)

### review_comment · yuseok89 · 2026-08-15T12:42:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2812#discussion_r3789375755
- ID: review_comment:3789375755
- 파일: longest-common-subsequence/JeonJe.java, 줄: 1, 원래 줄: 1

````text
공간에서 좀 더 최적화가 가능합니다. 참고하세요
````

### review · yuseok89 · 2026-08-15T12:45:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2812#pullrequestreview-4943854344
- ID: review:4943854344
- 리뷰 상태: APPROVED

````text
한 주 고생많으셨습니다 !
````

### review_comment · JeonJe · 2026-08-16T00:45:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2812#discussion_r3790618251
- ID: review_comment:3790618251
- 파일: longest-common-subsequence/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3789375755

````text
dp[i][j]가 i행과 i+1행만 참조하기 때문에, 한 배열로 제자리 덮어쓰면서 대각선 값만 변수로 넘기면 O(min(m, n))로 가능하겠네요.  감사합니다!
````

## [#2813 [yuseok89] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2813)

### review_comment · alphaorderly · 2026-08-12T15:42:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2813#discussion_r3767953372
- ID: review_comment:3767953372
- 파일: longest-common-subsequence/yuseok89.py, 줄: 1, 원래 줄: 1

````text
깔끔한 해결 잘 봤습니다!
공간복잡도의 최적화가 가능하니 시도 해 보시면 좋을것 같아요!
````

### review_comment · yuseok89 · 2026-08-14T14:34:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2813#discussion_r3784619891
- ID: review_comment:3784619891
- 파일: longest-common-subsequence/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3767953372

````text
의견 감사합니다.
더 좋아졌네요
````

### review_comment · alphaorderly · 2026-08-14T14:48:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2813#discussion_r3784737843
- ID: review_comment:3784737843
- 파일: longest-common-subsequence/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3767953372

````text
오 이런 방식도 엄청 깔끔하네요, 저도 배우고 갑니다!
````

### review · essaysir · 2026-08-14T22:11:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2813#pullrequestreview-4941557633
- ID: review:4941557633
- 리뷰 상태: APPROVED

````text
이번 한 주도 고생하셨습니다!! 연휴 잘 쉬시고, 다음 주도 같이 화이팅 해봐요!!
````

## [#2814 [essaysir] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2814)

### review_comment · alphaorderly · 2026-08-13T02:17:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3771908087
- ID: review_comment:3771908087
- 파일: reverse-bits/essaysir.java, 줄: 1, 원래 줄: 1

````text
Stringbuilder 대신에
0으로부터 시작해서 << 로 한번 쉬프팅하고
(n >>> i) & 1의 값으로 or 연산해 보시는건 어떨까요?
````

### review_comment · essaysir · 2026-08-14T04:22:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3781090004
- ID: review_comment:3781090004
- 파일: reverse-bits/essaysir.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3771908087

````text
한 번 다른 방법으로도 풀어보도록 하겠습니다!!
````

### review_comment · dolphinflow86 · 2026-08-14T14:36:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3784636665
- ID: review_comment:3784636665
- 파일: palindromic-substrings/essaysir.java, 줄: 8, 원래 줄: 8

````text
@essaysir 여기 로직 보면, 매번 모든 substring을 자르고 팰린드롬을 검사해서 O(N^3) 시간이 소요되는데, 각 인덱스를 중심점으로 잡고 양옆으로 확장해 나가는 방식을 사용하면 O(N^2) 시간 복잡도와 O(1) 공간 복잡도로 훨씬 효율적으로 최적화할 수 있을 것 같습니다. 한번 참고해보셔요.
````

### review_comment · dolphinflow86 · 2026-08-14T14:41:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3784688481
- ID: review_comment:3784688481
- 파일: longest-repeating-character-replacement/essaysir.java, 줄: 26, 원래 줄: 26

````text
@essaysir HashMap과 Collections.max()를 활용해서 슬라이딩 윈도우 조건을 깔끔하게 작성해주셨네요!

다만 이 문제에서는 알파벳 대문자 26개만 다루는 조건상, int[] count = new int[26] 크기의 배열을 사용하고, maxCount 변수를 매 루프마다 새로 구하는 대신 maxCount = Math.max(maxCount, ++count[ch]) 형태로 추적하면 HashMap 오버헤드와 max 탐색 과정을 줄여 실행 속도를 훨씬 향상시킬 수 있을 것 같습니다.
````

### review_comment · dolphinflow86 · 2026-08-14T14:44:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3784707839
- ID: review_comment:3784707839
- 파일: clone-graph/essaysir.java, 줄: 39, 원래 줄: 39

````text
@essaysir 한 가지 사소한 부분인데요, 반복문 내부에 선언된 List<Node> curs = nei.neighbors; 변수가 아래 로직에서 사용되지 않는 것 같아서 정리하는게 좋아보입니다.
````

### review · dolphinflow86 · 2026-08-14T14:44:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#pullrequestreview-4938257308
- ID: review:4938257308
- 리뷰 상태: APPROVED

````text
수고많으셨어요~
````

### review_comment · alphaorderly · 2026-08-14T14:49:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3784747308
- ID: review_comment:3784747308
- 파일: longest-common-subsequence/essaysir.java, 줄: 1, 원래 줄: 1

````text
너무 깔끔하게 잘 해결하셨네요, 
공간복잡도 최적화도 한번 해보시죠!
````

### review_comment · alphaorderly · 2026-08-14T14:59:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3784844506
- ID: review_comment:3784844506
- 파일: longest-repeating-character-replacement/essaysir.java, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:3784688481

````text
맞아요 똑같은 O(N)이지만 이건 실행 시간 차이가 좀 나더군요
````

### review_comment · alphaorderly · 2026-08-14T15:00:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3784855683
- ID: review_comment:3784855683
- 파일: reverse-bits/essaysir.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3771908087

````text
깔끔하게 잘 리팩터랭 하셨네요! 근데 진짜 문자열 연산 필요 없어요 제가 자바로 풀어봤거든요!
````

### review_comment · essaysir · 2026-08-14T22:08:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2814#discussion_r3787464056
- ID: review_comment:3787464056
- 파일: clone-graph/essaysir.java, 줄: 39, 원래 줄: 39
- 답글 대상: review_comment:3784707839

````text
@dolphinflow86 좋은 코드 리뷰 감사합니다!! 하면서, 다음에 풀면서는 위에서 말씀하신 사항들에 대해서 더 생각해보고 풀도록 하겠습니다!! ㅎㅎ  
````

## [#2815 [dolphinflow86] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2815)

### review · daehyun99 · 2026-08-15T06:09:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2815#pullrequestreview-4943055755
- ID: review:4943055755
- 리뷰 상태: APPROVED

````text
안녕하세요! 이번 주도 고생 많으셨습니다!!
````

## [#2816 [daehyun99] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2816)

### review_comment · parkhojeong · 2026-08-15T17:00:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2816#discussion_r3789819040
- ID: review_comment:3789819040
- 파일: clone-graph/daehyun99.py, 줄: None, 원래 줄: 1

````text
시간 복잡도에 노드 뿐 아니라 간선도 포함되어야 할 거 같습니다. 
````

### review_comment · parkhojeong · 2026-08-15T17:03:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2816#discussion_r3789826076
- ID: review_comment:3789826076
- 파일: longest-repeating-character-replacement/daehyun99.py, 줄: None, 원래 줄: 2

````text
공간 복잡도 표기가 잘못 되어 있네요. 
````

### review · parkhojeong · 2026-08-15T17:10:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2816#pullrequestreview-4944283837
- ID: review:4944283837
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다. 복잡도 표기만 수정해주시면 될 거 같습니다!
````

### review_comment · daehyun99 · 2026-08-16T05:47:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2816#discussion_r3791070484
- ID: review_comment:3791070484
- 파일: clone-graph/daehyun99.py, 줄: None, 원래 줄: 1
- 답글 대상: review_comment:3789819040

````text
그렇군요! `O(N + E)`네요
````

### issue_comment · parkhojeong · 2026-08-18T02:48:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2816#issuecomment-5322873060
- ID: issue_comment:5322873060

````text
@daehyun99 커멘트 드린 부분 반영하신 후에 리뷰 요청 부탁드립니다.
````

### issue_comment · daehyun99 · 2026-08-19T07:29:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2816#issuecomment-5338917907
- ID: issue_comment:5338917907

````text
> @daehyun99 커멘트 드린 부분 반영하신 후에 리뷰 요청 부탁드립니다.

업데이트했습니다. 확인 부탁드려요!
````

## [#2817 [tigermint] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2817)

### review_comment · ICE0208 · 2026-08-15T14:21:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2817#discussion_r3789532911
- ID: review_comment:3789532911
- 파일: reverse-bits/tigermint.kt, 줄: 1, 원래 줄: 1

````text
코틀린의 비트 연산자는 엄청 직관적이네요!!
````

### review · ICE0208 · 2026-08-15T14:25:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2817#pullrequestreview-4944005391
- ID: review:4944005391
- 리뷰 상태: APPROVED

````text
다음주 문제풀이도 파이팅입니다~!
````

## [#2818 [ICE0208] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2818)

### review_comment · parkhojeong · 2026-08-15T15:01:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2818#discussion_r3789602281
- ID: review_comment:3789602281
- 파일: longest-repeating-character-replacement/ICE0208.java, 줄: 21, 원래 줄: 21

````text
`right - left + 1` 부분을 변수로 선언하는 건 어떨까요?
````

### review_comment · parkhojeong · 2026-08-15T15:04:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2818#discussion_r3789607821
- ID: review_comment:3789607821
- 파일: longest-repeating-character-replacement/ICE0208.java, 줄: 1, 원래 줄: 1

````text
심플하게 풀어주셔서 이해가 잘 되네요
````

### review · parkhojeong · 2026-08-15T15:04:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2818#pullrequestreview-4944077851
- ID: review:4944077851
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

### review_comment · ICE0208 · 2026-08-15T16:00:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2818#discussion_r3789712727
- ID: review_comment:3789712727
- 파일: longest-repeating-character-replacement/ICE0208.java, 줄: 21, 원래 줄: 21
- 답글 대상: review_comment:3789602281

````text
코드 가독성에 도움이 될 수 있겠네요. 감사합니다👍
````

### review_comment · ICE0208 · 2026-08-15T16:01:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2818#discussion_r3789713246
- ID: review_comment:3789713246
- 파일: longest-repeating-character-replacement/ICE0208.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3789607821

````text
리뷰 감사합니다!
````

## [#2820 [sangbeenmoon] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2820)

### review_comment · parkhojeong · 2026-08-15T17:35:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2820#discussion_r3789880975
- ID: review_comment:3789880975
- 파일: longest-repeating-character-replacement/sangbeenmoon.java, 줄: 31, 원래 줄: 31

````text
돌려보니 성능이 좋은 편은 아니라서 조금 더 최적화 시도해보셔도 좋을 거 같습니다.
````

### review_comment · parkhojeong · 2026-08-15T17:41:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2820#discussion_r3789891778
- ID: review_comment:3789891778
- 파일: longest-repeating-character-replacement/sangbeenmoon.java, 줄: 45, 원래 줄: 45

````text
이쪽에서 오버헤드가 살짝 있어 보이네요. 단순하게 빈도 배열만 사용해보시는 건 어떨까요?
````

### review · parkhojeong · 2026-08-15T17:44:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2820#pullrequestreview-4944352533
- ID: review:4944352533
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

## [#2821 [freemjstudio] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2821)

### review_comment · parkhojeong · 2026-08-15T17:14:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2821#discussion_r3789844137
- ID: review_comment:3789844137
- 파일: reverse-bits/freemjstudio.py, 줄: 14, 원래 줄: 14

````text
문자열 조작 없이 비트 연산과 같은 방식 등으로 풀어보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-08-15T17:25:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2821#pullrequestreview-4944318468
- ID: review:4944318468
- 리뷰 상태: CHANGES_REQUESTED

````text
수고하셨습니다. 

스터디 규칙을 아직 숙지하지 못하신 것 같은데 해당 문서 확인 부탁드립니다. https://github.com/DaleStudy/leetcode-study/wiki

````

## [#2822 [alphaorderly] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2822)

### review_comment · DaleSeo · 2026-08-20T04:03:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#discussion_r3818523098
- ID: review_comment:3818523098
- 파일: minimum-window-substring/alphaorderly.py, 줄: None, 원래 줄: 4

````text
어떤 기준으로 `O(1)`이라고 판단하셨는지 궁금합니다.
````

### review_comment · DaleSeo · 2026-08-20T04:05:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#discussion_r3818529777
- ID: review_comment:3818529777
- 파일: maximum-product-subarray/alphaorderly.py, 줄: None, 원래 줄: 9

````text
여기 양수, 음수라는 표현이 맞나요? 코드 상으로는 그냥 단순 최대, 최소값을 저장하는 것 같아서요.
````

### review_comment · DaleSeo · 2026-08-20T04:07:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#discussion_r3818535629
- ID: review_comment:3818535629
- 파일: sum-of-two-integers/alphaorderly.py, 줄: None, 원래 줄: 24

````text
nit: `left`는 루프 안에서 매번 새로 할당되므로 여기서 굳이 초기화할 필요가 없을 것 같습니다.
````

### review · DaleSeo · 2026-08-20T04:08:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#pullrequestreview-4978953056
- ID: review:4978953056
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 훌륭하게 잘 푸셔서 아주 사소한 질문만 남깁니다.
````

### review_comment · alphaorderly · 2026-08-20T04:10:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#discussion_r3818548824
- ID: review_comment:3818548824
- 파일: maximum-product-subarray/alphaorderly.py, 줄: None, 원래 줄: 9
- 답글 대상: review_comment:3818529777

````text
거시적으로 보면 맞다고 생각해서 적었어요!
만약 nums의 모든 수가 양수로만 이루어져 있다면 음수가 아니지만
음수가 하나라도 있다면 음수의 곱으로 인해 해당 내용과 비슷하게 되니까요!
````

### review_comment · alphaorderly · 2026-08-20T04:11:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#discussion_r3818550399
- ID: review_comment:3818550399
- 파일: minimum-window-substring/alphaorderly.py, 줄: None, 원래 줄: 4
- 답글 대상: review_comment:3818523098

````text
으아 이건 실수네요 O(N) 입니다.
````

### issue_comment · alphaorderly · 2026-08-20T04:17:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#issuecomment-5351292854
- ID: issue_comment:5351292854

````text
@DaleSeo 의논해주신 부분 보고 수정했습니다! 바쁘신데 댓글 감사합니다!!!
````

### review · yuseok89 · 2026-08-20T14:57:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2822#pullrequestreview-4984131770
- ID: review:4984131770
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
많이 배웁니다.
````

## [#2823 [njngwn] WEEK 08 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2823)

### review_comment · parkhojeong · 2026-08-17T16:58:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2823#discussion_r3797376015
- ID: review_comment:3797376015
- 파일: longest-repeating-character-replacement/njngwn.py, 줄: 17, 원래 줄: 17

````text
좋은 접근인 거 같습니다
````

### review_comment · parkhojeong · 2026-08-17T16:59:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2823#discussion_r3797382046
- ID: review_comment:3797382046
- 파일: palindromic-substrings/njngwn.py, 줄: 20, 원래 줄: 20

````text
초기값만 다르고 로직은 동일해서 헬퍼함수 하나를 두면 의도가 더 명확해질 거 같네요
````

### review_comment · parkhojeong · 2026-08-17T17:01:35Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2823#discussion_r3797393222
- ID: review_comment:3797393222
- 파일: reverse-bits/njngwn.py, 줄: 8, 원래 줄: 8

````text
스택 없이 비트 연산으로 구현해보셔도 좋을 거 같습니다.
````

### review · parkhojeong · 2026-08-17T17:02:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2823#pullrequestreview-4952847399
- ID: review:4952847399
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 커멘트 간단히 남겨보았어요. 
주차가 지나서 바로 머지하도록 하겠습니다. 
````

## [#2824 [yuseok89] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2824)

### review_comment · alphaorderly · 2026-08-20T00:07:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2824#discussion_r3817663858
- ID: review_comment:3817663858
- 파일: linked-list-cycle/yuseok89.py, 줄: 1, 원래 줄: 1

````text
조건문 부분에 같은지 비교를 하는것도 꽤 괜찮은 아이디어시네요!
다만 아주 개인적인 의견인데, slow와 fast를 비교하는것은 참조를 비교하는거라 is를 쓰는게 더 낫지 않을까? 하는 생각이 있었어요
좋은 코드 보고 갑니다!
````

### review_comment · DaleSeo · 2026-08-20T03:47:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2824#discussion_r3818463034
- ID: review_comment:3818463034
- 파일: linked-list-cycle/yuseok89.py, 줄: None, 원래 줄: 12

````text
노드가 하나뿐이고 순환이 없는 입력이라면 `fast`가 `None`으로 시작하므로, 반복문 안의 `if not fast` 가 곧바로 `False`를 반환해 줄텐데요. 그렇다면 여기서 `not head.next`까지 확인하는 것은 어떤 경우를 대응하기 위한 목적인가요?
````

### review · DaleSeo · 2026-08-20T03:48:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2824#pullrequestreview-4978886033
- ID: review:4978886033
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

### review_comment · yuseok89 · 2026-08-21T15:06:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2824#discussion_r3831335630
- ID: review_comment:3831335630
- 파일: linked-list-cycle/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3817663858

````text
더 명확해지겠네요.
반영해보겠습니다.
감사합니다 !
````

### review_comment · yuseok89 · 2026-08-21T15:07:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2824#discussion_r3831342104
- ID: review_comment:3831342104
- 파일: linked-list-cycle/yuseok89.py, 줄: None, 원래 줄: 12
- 답글 대상: review_comment:3818463034

````text
조금 과하게 생각한 것 같습니다.
말씀 하신대로, not head 만으로 충분합니다.
감사합니다 !
````

## [#2825 [DaleSeo] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2825)

### review · dolphinflow86 · 2026-08-21T12:42:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2825#pullrequestreview-4993317380
- ID: review:4993317380
- 리뷰 상태: APPROVED

````text
maximum-product-subarray 풀이 잘 보았습니다!
이 문제는 음수가 곱해지는 상황 때문에 if문이나 복잡한 max/min 비교식이 들어가기 쉬운데, [max * num, min * num, num] 배열과 Rust 이터레이터를 활용하여 잘 풀어주신 것 같습니다.

수고하셨습니다!
````

## [#2826 [dolphinflow86] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2826)

### review_comment · dahyeong-yun · 2026-08-22T09:43:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2826#discussion_r3835737058
- ID: review_comment:3835737058
- 파일: maximum-product-subarray/dolphinflow86.py, 줄: None, 원래 줄: 22

````text
```suggestion
                cur_max, cur_min = cur_min, cur_max
```
사소한 건데, 파이썬은 다중할당이 가능하다고 알고 있어서 tmp를 없앨 수 있을 것 같아요.
````

### review_comment · dahyeong-yun · 2026-08-22T10:07:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2826#discussion_r3835775765
- ID: review_comment:3835775765
- 파일: sum-of-two-integers/dolphinflow86.py, 줄: 8, 원래 줄: 8

````text
파이썬은 정수 오버플로우가 없어서, 별도 체크가 필요하군요!
````

### review_comment · dahyeong-yun · 2026-08-22T10:14:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2826#discussion_r3835787236
- ID: review_comment:3835787236
- 파일: minimum-window-substring/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
못 풀었던 문제인데 직관적으로 풀이 덕분에 이해가 됐습니댜! 두 .0포인터를 같은 방향으로 보내면서 left가 right를 따라 잡아 가는 중에 문자의 카운트를 비교하는 거네요. 
````

### review · dahyeong-yun · 2026-08-22T10:15:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2826#pullrequestreview-4999873816
- ID: review:4999873816
- 리뷰 상태: APPROVED

````text
고생하셨습니다. 제 풀이와 유사한 부분 더러 있어서 제가 쓰는 java와 표현 상의 차이를 더 느꼈던거 같아요. 변수명이나 코드 흐름이 직관적이라서 읽기가 편했습니다! 주차는 제가 9주차로 설정을 했는데 확인 한번 부탁드려요.
````

### issue_comment · dolphinflow86 · 2026-08-22T14:20:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2826#issuecomment-5380871680
- ID: issue_comment:5380871680

````text
> 고생하셨습니다. 제 풀이와 유사한 부분 더러 있어서 제가 쓰는 java와 표현 상의 차이를 더 느꼈던거 같아요. 변수명이나 코드 흐름이 직관적이라서 읽기가 편했습니다! 주차는 제가 9주차로 설정을 했는데 확인 한번 부탁드려요.

주차 설정이 안되어었네요. 세팅 감사합니다! 그리고 리뷰도 감사합니다.
한 주간 고생하셨습니다!
````

## [#2827 [dahyeong-yun] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2827)

### review_comment · njngwn · 2026-08-21T14:00:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2827#discussion_r3830823410
- ID: review_comment:3830823410
- 파일: linked-list-cycle/dahyeong-yun.java, 줄: 23, 원래 줄: 23

````text
2가지 방법으로 풀어보신게 좋네요!! 코드도 깔끔하구요 👍
````

### review_comment · njngwn · 2026-08-21T14:01:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2827#discussion_r3830834936
- ID: review_comment:3830834936
- 파일: maximum-product-subarray/dahyeong-yun.java, 줄: 10, 원래 줄: 10

````text
이 코드가 없어도 어차피 반복문을 안돌고 answer가 반환될 것 같은데, 굳이 넣으신 이유가 있을까요? 
````

### review_comment · njngwn · 2026-08-21T16:07:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2827#discussion_r3831790007
- ID: review_comment:3831790007
- 파일: pacific-atlantic-water-flow/dahyeong-yun.java, 줄: 29, 원래 줄: 29

````text
dfs에 매개변수로 넘기는 것도 고려해보면 좋을 것 같습니다!
코딩테스트에서는 상관없거나 조금 과할 수도 있을 것 같긴 한데,

- dfs가 외부 상태(this.heights 등)에 의존하지 않게 되어서, 이 Solution 인스턴스가 재사용되거나 여러 스레드에서 동시에 호출될 때 상태가 꼬일 위험이 없어질 것 같습니다.
- 또 dfs 시그니처만 봐도 이 함수가 뭘 필요로 하는지 바로 드러나서, 나중에 이 함수만 따로 읽거나 테스트할 때도 더 편할 것 같습니다.

다만 파라미터가 늘어나는 트레이드오프는 있어서, 지금처럼 코딩테스트용으로 1회성 로직이면 지금 방식도 충분히 괜찮을 것 같네요! 
````

### review_comment · njngwn · 2026-08-21T16:08:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2827#discussion_r3831794863
- ID: review_comment:3831794863
- 파일: pacific-atlantic-water-flow/dahyeong-yun.java, 줄: 24, 원래 줄: 24

````text
알고리즘 설명이 되어있어 좋네요! 수고 많으셨습니다!!
````

### review_comment · dahyeong-yun · 2026-08-22T14:15:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2827#discussion_r3836219210
- ID: review_comment:3836219210
- 파일: maximum-product-subarray/dahyeong-yun.java, 줄: 10, 원래 줄: 10
- 답글 대상: review_comment:3830834936

````text
이 코드가 공간복잡도 최적화를 하면서 정리되가던 코드라 이전 흔적이 남은 것 같네요. 말씀하신대로 삭제되도 되는 라인이네요!
````

### review_comment · dahyeong-yun · 2026-08-22T14:19:10Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2827#discussion_r3836226135
- ID: review_comment:3836226135
- 파일: pacific-atlantic-water-flow/dahyeong-yun.java, 줄: 29, 원래 줄: 29
- 답글 대상: review_comment:3831790007

````text
네네. dfs 쓸 때마다 메서드 파라미터와 상태를 만드는 것 사이에서 고민이 드는 것 같아요. 상태를 갖는 필드를 만드는 걸 선호하지 않는데, 문제를 풀 때 너무 지저분하고 헷갈려서 인스턴스 변수를 두고 풀게 되더라구요. 주의점을 환기 해주셔서 도움이 됐습니다. 여차하면 이너 클래스로 파라미터를 정리하는 방법도 있겠으나, 코딩테스트 본연의 목적과 환경에 집중하려고 해요!
````

## [#2828 [njngwn] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2828)

### issue_comment · DaleSeo · 2026-08-23T01:19:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2828#issuecomment-5383554384
- ID: issue_comment:5383554384

````text
@njngwn 님, 다음 PR부터는 주차 설정이 누락되지 않도록 주의 부탁드리겠습니다. 본 PR은 제가 설정해드릴께요 :)

<img width="1802" height="854" alt="2026-08-23 at 10 18 51" src="https://github.com/user-attachments/assets/91f7fd57-662a-4b19-8efd-ebb463fb8302" />

````

### issue_comment · njngwn · 2026-08-23T13:14:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2828#issuecomment-5386184826
- ID: issue_comment:5386184826

````text
> @njngwn 님, 다음 PR부터는 주차 설정이 누락되지 않도록 주의 부탁드리겠습니다. 본 PR은 제가 설정해드릴께요 :)
> 
> <img alt="2026-08-23 at 10 18 51" width="1802" height="854" src="https://private-user-images.githubusercontent.com/5466341/639946203-91f7fd57-662a-4b19-8efd-ebb463fb8302.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODc0OTA4MTMsIm5iZiI6MTc4NzQ5MDUxMywicGF0aCI6Ii81NDY2MzQxLzYzOTk0NjIwMy05MWY3ZmQ1Ny02NjJhLTRiMTktOGVmZC1lYmI0NjNmYjgzMDIucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDgyMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA4MjNUMTMwODMzWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YTU0OGM0ZWU1YjQ1ZTRjNmEyODE1YTdkOWY3M2RlNGE1OTQzYWM5ZDI0ZTcxOWRjOTI5OTU2Y2MwMTUwMzFhZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.cLKoLoVacErAO7Xk971ISEz5WbNfellyZ7tQR0qUUlM">

@DaleSeo  아이고 죄송해요😭 그리고 감사합니다!!! 다음번에는 놓치지 않고 확인하겠습니다!!
````

## [#2829 [sangbeenmoon] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2829)

### review_comment · parkhojeong · 2026-08-22T13:50:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2829#discussion_r3836170837
- ID: review_comment:3836170837
- 파일: pacific-atlantic-water-flow/sangbeenmoon.py, 줄: 23, 원래 줄: 23

````text
ny == 0, ny == m -1 일 때 처리되는 로직을 예상했는데 -1, m 이 되었을때 처리를 하셨네요. 인덱스를 벗어난 경우로 처리해주신 이유가 있을까요?
````

### review · parkhojeong · 2026-08-22T13:50:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2829#pullrequestreview-5000300057
- ID: review:5000300057
- 리뷰 상태: APPROVED

````text
수고하셨습니다.
````

## [#2830 [tigermint] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2830)

### review · parkhojeong · 2026-08-22T15:47:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2830#pullrequestreview-5000502225
- ID: review:5000502225
- 리뷰 상태: APPROVED

````text
수고하셨습니다~
````

## [#2831 [daehyun99] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2831)

### review_comment · parkhojeong · 2026-08-22T13:32:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#discussion_r3836139963
- ID: review_comment:3836139963
- 파일: pacific-atlantic-water-flow/daehyun99.py, 줄: 20, 원래 줄: 20

````text
이 부분이 잘 이해가 안되서 그런데 혹시 어떤 의도로 푸셨는지 설명 해주실 수 있을까요?
````

### review_comment · parkhojeong · 2026-08-22T13:34:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#discussion_r3836142951
- ID: review_comment:3836142951
- 파일: minimum-window-substring/daehyun99.py, 줄: 43, 원래 줄: 43

````text
혹시 어떤 방식으로 푸신건지 설명 부탁드려도 될까요?
````

### review · parkhojeong · 2026-08-22T13:39:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#pullrequestreview-5000273014
- ID: review:5000273014
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 
````

### review_comment · daehyun99 · 2026-08-22T16:46:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#discussion_r3836509979
- ID: review_comment:3836509979
- 파일: pacific-atlantic-water-flow/daehyun99.py, 줄: 20, 원래 줄: 20
- 답글 대상: review_comment:3836139963

````text
음...
queue나 stack처럼 접근해서 풀었습니다. (`matrix`를 queue로 생각하시면 편하실 것 같습니다)

예를 들어, Pacific으로 무조건 흐르는 위치는 행이 0이거나, 열이 0이면 흐르는데요.
Pacific으로 흐르는 열들을 `matrix`에 넣고, 해당 위치의 값과 같거나 큰 주변의 좌표를 `check()` 함수에서 찾고, `matrix`에 추가하는 형태입니다.

마찬가지로, Atlantic에서도 동일한 과정을 진행 후, 교집합을 찾으면 두 바다로 모두 흐르는 위치만 남게 됩니다.

<img width="1109" height="554" alt="Image" src="https://github.com/user-attachments/assets/0f34ca24-d270-4793-bc42-b7de82d84bfe" />
````

### review_comment · daehyun99 · 2026-08-22T17:00:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#discussion_r3836538088
- ID: review_comment:3836538088
- 파일: minimum-window-substring/daehyun99.py, 줄: 43, 원래 줄: 43
- 답글 대상: review_comment:3836142951

````text
먼저 `check`에다가 찾아야하는 각 문자열들의 갯수를 찾고요.

그 후, `s`에 들어있는 문자열들에 1씩 빼줍니다.(line 6 ~8)

그러면, `check` 안의 값이 무조건 음수이거나 0이여야 t의 조건을 다 만족하게 됩니다.

이 상황에서 line 13 ~ 19 코드로 t의 조건을 만족하는 s의 끝에서부터 시작하는 `left` 인덱스 좌표를 찾고, `right`는 `len(s)-1`가 됩니다.

그 다음에는 `right`를 왼쪽으로 옮겨가면서, `t` 조건을 만족하는지 확인합니다(`check` 안에 양수가 존재하는지),

예를 들어, 아래의 경우 `s[right]`가 `C`일 때, t에는 C가 들어가야해서, right에 -1를 더할 수가 없는데요.
이때, `left`를 옮겨가면서 `s[left]`가 `C`인 경우를 찾습니다.
만약 찾았다면, `right`를 -1할 수 있습니다.

그 후, 원래의 정답 문자열의 길이와 새로 찾은 `s[left:right]`의 길이를 비교 후, 길이가 짧은 문자열을 정답으로 반환하게 됩니다.


<img width="1318" height="466" alt="Image" src="https://github.com/user-attachments/assets/b1a1b7af-fc25-40c1-84ee-f87c2cab0aab" />
````

### review_comment · parkhojeong · 2026-08-23T04:44:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#discussion_r3837718915
- ID: review_comment:3837718915
- 파일: pacific-atlantic-water-flow/daehyun99.py, 줄: 20, 원래 줄: 20
- 답글 대상: review_comment:3836139963

````text
바다 쪽에서 시작해서 찾는 방식이군요. 상세히 설명 해주셔서 쉽게 이해했습니다. 감사합니다.
````

### review_comment · parkhojeong · 2026-08-23T04:48:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2831#discussion_r3837724731
- ID: review_comment:3837724731
- 파일: minimum-window-substring/daehyun99.py, 줄: 43, 원래 줄: 43
- 답글 대상: review_comment:3836142951

````text
설명 해주신 내용이랑 코드 보면서 좀 더 살펴보겠습니다. 감사합니다!
````

## [#2832 [parkhojeong] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2832)

### review_comment · ICE0208 · 2026-08-22T15:10:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2832#discussion_r3836324821
- ID: review_comment:3836324821
- 파일: linked-list-cycle/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
visited 를 사용해서 이전에 방문한 노드인지 판단하는 로직이 직관적이라 이해하기 쉽네요!
`플로이드 순환 찾기 알고리즘` 을 이용해서 공간 복잡도를 줄일 수 있을 것 같습니다!
````

### review_comment · ICE0208 · 2026-08-22T15:16:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2832#discussion_r3836335178
- ID: review_comment:3836335178
- 파일: pacific-atlantic-water-flow/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
저도 처음에는 각 좌표에서 DFS를 시작하는 방식으로 풀었는데, 생각해야 할 조건이 많아 조금 복잡해지더라고요!
반대로 각 바다의 경계에서 시작해서 도달 가능한 좌표를 확인하는 방식으로 풀어보니 조금 더 간단하게 구현할 수 있었습니다. 참고용으로 코멘트 남겨놓습니다 :)
````

### review · ICE0208 · 2026-08-22T15:17:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2832#pullrequestreview-5000440210
- ID: review:5000440210
- 리뷰 상태: APPROVED

````text
9주차 문제 풀이도 수고 많으셨습니다! 👍
````

### review_comment · parkhojeong · 2026-08-22T15:45:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2832#discussion_r3836392436
- ID: review_comment:3836392436
- 파일: linked-list-cycle/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3836324821

````text
감사합니다. 그렇게도 한 번 풀어보겠습니다
````

### review_comment · parkhojeong · 2026-08-22T15:46:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2832#discussion_r3836394271
- ID: review_comment:3836394271
- 파일: pacific-atlantic-water-flow/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3836335178

````text
반대로 시작하는 것도 괜찮겠네요. 알려주신 방식으로도 풀어보겠습니다. 감사합니다!
````

## [#2833 [ICE0208] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2833)

### review · alphaorderly · 2026-08-22T15:14:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2833#pullrequestreview-5000445749
- ID: review:5000445749
- 리뷰 상태: APPROVED

````text
깔끔하게 잘 해결하셨네요!
````

## [#2834 [alphaorderly] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2834)

### review · yuseok89 · 2026-08-29T01:11:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2834#pullrequestreview-5056153765
- ID: review:5056153765
- 리뷰 상태: APPROVED

````text
이번 한주도 고생하셨습니다.
항상 많이 배웁니다.
````

## [#2835 [freemjstudio] WEEK 09 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2835)

### review_comment · alphaorderly · 2026-08-23T09:35:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2835#discussion_r3838186371
- ID: review_comment:3838186371
- 파일: linked-list-cycle/freemjstudio.py, 줄: 1, 원래 줄: 1

````text
https://blog.naver.com/occidere/222260962156
플로이드의 토끼와 거북이 알고리즘을 아신다면 더 쉽게 하실수 있으세요!
````

### review_comment · freemjstudio · 2026-08-23T09:45:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2835#discussion_r3838202477
- ID: review_comment:3838202477
- 파일: linked-list-cycle/freemjstudio.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3838186371

````text
주차가 지났는데도 리뷰해주셔서 감사합니다 ㅠ
참고해보겠습니다 :) 
````

### review_comment · alphaorderly · 2026-08-24T02:48:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2835#discussion_r3840390727
- ID: review_comment:3840390727
- 파일: pacific-atlantic-water-flow/freemjstudio.py, 줄: 1, 원래 줄: 1

````text
https://velog.io/@revo3325/%EB%8B%A4%EC%A4%91-%EC%8B%9C%EC%9E%91%EC%A0%90-BFS
다중시작점 BFS를 통해 성능을 100배가량 향상시킬수 있으세요!
대서양과 태평양에 인접한 cell들에서만 시작하게 할수 있고, 한번의 BFS로 압축이 가능하거든요!
````

### review · alphaorderly · 2026-08-24T02:48:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2835#pullrequestreview-5004196469
- ID: review:5004196469
- 리뷰 상태: APPROVED

````text
고생하셨습니다! 이번엔 제목도 알맞게 잘 지어주셨네요!
````

### review_comment · alphaorderly · 2026-08-24T02:49:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2835#discussion_r3840393297
- ID: review_comment:3840393297
- 파일: pacific-atlantic-water-flow/freemjstudio.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3840390727

````text
<img width="540" height="104" alt="image" src="https://github.com/user-attachments/assets/5d8f4b7c-f368-47f1-be0e-7c86f03336b1" />    

거짓말이 아니라 진짜로요!
````

## [#2836 [yuseok89] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2836)

### review_comment · alphaorderly · 2026-08-24T13:57:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3844132979
- ID: review_comment:3844132979
- 파일: invert-binary-tree/yuseok89.py, 줄: 1, 원래 줄: 1

````text
앞의 if가 이미 리턴을 하고 있어서 else 를 크게 쓰지 않으셔도 되지 않을까? 라는 생각이 듭니다!
또한 cur_node 를 만들지 않으시고 root를 직접 바꾸셔도 정답처리 되실거에요!
````

### review_comment · yuseok89 · 2026-08-27T15:19:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3873146856
- ID: review_comment:3873146856
- 파일: invert-binary-tree/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3844132979

````text
좋네요 !
감사합니다 🙏 
````

### review_comment · alphaorderly · 2026-08-27T15:21:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3873164877
- ID: review_comment:3873164877
- 파일: course-schedule/yuseok89.py, 줄: 1, 원래 줄: 1

````text
정말 깔끔하게 잘 해결해 주셨는데요!
제 생각에 is_completed에 수료를 완료한 과목의 갯수만 기록해도 가능하지 않을까? 라는 생각이 들었어요
어떤지 한번 생각해보시면 더욱 좋을것 같습니다!
````

### review_comment · alphaorderly · 2026-08-27T15:24:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3873188142
- ID: review_comment:3873188142
- 파일: jump-game/yuseok89.py, 줄: 1, 원래 줄: 1

````text
상당히 깔끔한 그리디네요! 잘 보고 갑니다
````

### review_comment · alphaorderly · 2026-08-27T15:26:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3873204194
- ID: review_comment:3873204194
- 파일: search-in-rotated-sorted-array/yuseok89.py, 줄: 1, 원래 줄: 1

````text
깔끔하게 잘 해결해 주셨는데요, 해당 문제는 단일  while로도 해결 가능하답니다!
한번 시도해보시면 좋을것 같아요
````

### review_comment · JeonJe · 2026-08-29T00:16:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3884839341
- ID: review_comment:3884839341
- 파일: search-in-rotated-sorted-array/yuseok89.py, 줄: None, 원래 줄: 15

````text
r = (l + n - 1) % n에서 % n의 역할이 조금 더 쉽게 읽히면 좋겠다는 생각이 들었습니다. 회전이 없어서 피벗이 0일 때 l - 1 = -1이 되는 걸 n - 1로 돌려막는 용도로 보이는데, 처음 읽으면 왜 모듈러가 나오는지 한 번 되짚어봐야 하더라고요. 첫 루프가 끝난 l에 이름을 붙이고 두 분기에서 l, r을 둘 다 명시해주면 코드가 좀 더 길어지더라도 읽기는 쉬워질 것 같아요. 예를 들어
```
  pivot = l
  if target >= nums[0]:
      l, r = 0, (pivot - 1 if pivot else n - 1)
  else:
      l, r = pivot, n - 1
```

````

### review_comment · JeonJe · 2026-08-29T00:28:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3884875022
- ID: review_comment:3884875022
- 파일: course-schedule/yuseok89.py, 줄: 15, 원래 줄: 16

````text
 라운드마다 for idx in range(numCourses)로 전체 과목을 다시 훑고 있어서, 라운드 수 × 과목 수만큼 계산이 예상됩니다. 선수관계가 0 → 1 → 2 → ...처럼 한 줄로 이어지면 라운드가 과목 수만큼 생기는데, 제약 상한인 2000과목이면 라운드가 2001회 돌고 스캔이 400만 번 일어나서 O(V² + E)에 가까울 것 같아요.

in_deg가 감소하는 그 자리에서 0이 됐는지 바로 판정해두면 "다음에 처리할 과목을 찾는" 단계가 통째로 없어지고, 각 과목과 각 간선을 한 번씩만 보게 되어 O(V + E)로 줄일 수 있지 않을까 합니다.
````

### review_comment · yuseok89 · 2026-08-29T01:45:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3885095263
- ID: review_comment:3885095263
- 파일: search-in-rotated-sorted-array/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3873204194

````text
그렇네요 감사합니다 !
````

### review_comment · yuseok89 · 2026-08-29T01:45:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3885095904
- ID: review_comment:3885095904
- 파일: course-schedule/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3873164877

````text
덕분에 많은 공부가 되네요
감사합니다 !
````

### review_comment · yuseok89 · 2026-08-29T01:45:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2836#discussion_r3885096548
- ID: review_comment:3885096548
- 파일: course-schedule/yuseok89.py, 줄: 15, 원래 줄: 16
- 답글 대상: review_comment:3884875022

````text
덕분에 많은 공부가 되네요
감사합니다 !
````

## [#2837 [JeonJe] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2837)

### review_comment · alphaorderly · 2026-08-25T12:59:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2837#discussion_r3853185252
- ID: review_comment:3853185252
- 파일: search-in-rotated-sorted-array/JeonJe.java, 줄: 1, 원래 줄: 1

````text
피봇 포인트를 찾아서 하는것도 꽤 좋은 아이디어시네요!
다만 한번의 binary search로 해결하싷수도 있어요!
````

### review_comment · alphaorderly · 2026-08-26T02:33:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2837#discussion_r3859188128
- ID: review_comment:3859188128
- 파일: invert-binary-tree/JeonJe.java, 줄: 16, 원래 줄: 16

````text
해당 두 부분이 각각의 서브트리를 리턴하니까 이걸 그대로 사용해서 root.left와 root.right에 넣어도 좋지 않을까 하는 생각이 있습니다!
````

### review_comment · JeonJe · 2026-08-26T11:25:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2837#discussion_r3862242330
- ID: review_comment:3862242330
- 파일: invert-binary-tree/JeonJe.java, 줄: 16, 원래 줄: 16
- 답글 대상: review_comment:3859188128

````text
반환된 서브트리를 root.left와 root.right에 다시 넣을지 고민했는데,
각 서브트리를 제자리에서 변경하므로 다시 대입하지 않는 방식으로 구현했습니다.
의도를 더 명확하게 표현할 수 있는 제안 감사합니다!
````

### review_comment · JeonJe · 2026-08-26T11:31:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2837#discussion_r3862286642
- ID: review_comment:3862286642
- 파일: search-in-rotated-sorted-array/JeonJe.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3853185252

````text
말씀해주신 제안을 생각해보니, mid를 기준으로 정렬된 구간을 확인하고
타깃이 해당 범위에 있는지에 따라 탐색 범위를 줄여가는 방식으로
피벗 위치를 먼저 구하지 않고도 한 번의 이진 탐색으로 해결할 수 있었네요. 감사합니다!
````

### review · daehyun99 · 2026-08-29T06:12:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2837#pullrequestreview-5057140712
- ID: review:5057140712
- 리뷰 상태: APPROVED

````text
안녕하세요! 이번 주도 고생 많으셨습니다!!
````

## [#2838 [daehyun99] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2838)

### review_comment · alphaorderly · 2026-08-28T11:42:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3880293078
- ID: review_comment:3880293078
- 파일: invert-binary-tree/daehyun99.py, 줄: 1, 원래 줄: 1

````text
bfs같은 추가 함수 없이도 구현 가능하시지 않을까요?
````

### review_comment · alphaorderly · 2026-08-28T12:22:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3880527934
- ID: review_comment:3880527934
- 파일: course-schedule/daehyun99.py, 줄: 1, 원래 줄: 1

````text
사이클 확인하는 방식으로 해결하셨네요! 위상정렬로도 해결 가능합니다!
````

### review_comment · alphaorderly · 2026-08-28T12:25:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3880542307
- ID: review_comment:3880542307
- 파일: merge-k-sorted-lists/daehyun99.py, 줄: 1, 원래 줄: 1

````text
해당 풀이도 분명 올바른 정답을 도출해 내지만
추가 공간복잡도가 소요 될 뿐 만 아니라
연결 리스트를 이용해 더 빠르게 해결하는것이 아니기 때문에
해당 부분을 염두에 두고 다시 해결해 보시는게 어떨까? 싶습니다
````

### review_comment · alphaorderly · 2026-08-28T12:29:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3880566667
- ID: review_comment:3880566667
- 파일: search-in-rotated-sorted-array/daehyun99.py, 줄: 1, 원래 줄: 1

````text
단일 while로도 해결이 가능한 문제이긴 해요! 한번 시도 해 보시는것을 추천드립니다.
````

### review_comment · dolphinflow86 · 2026-08-28T14:58:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3881613807
- ID: review_comment:3881613807
- 파일: invert-binary-tree/daehyun99.py, 줄: 11, 원래 줄: 11

````text
함수이름이 bfs인데 동작은 재귀 기반 dfs로 보이네요!
````

### review · dolphinflow86 · 2026-08-28T14:58:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#pullrequestreview-5052291877
- ID: review:5052291877
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

### review_comment · dolphinflow86 · 2026-08-28T15:00:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3881633399
- ID: review_comment:3881633399
- 파일: search-in-rotated-sorted-array/daehyun99.py, 줄: 4, 원래 줄: 4

````text
회전된 배열에서 피봇(pivot)을 1차 이진 탐색으로 먼저 구한 뒤, target의 범위를 좁혀 2차 이진 탐색을 수행하는 2 pass 풀이가 직관적이어서 인상 깊습니다!
````

### review_comment · daehyun99 · 2026-08-29T07:12:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3885903441
- ID: review_comment:3885903441
- 파일: invert-binary-tree/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3880293078

````text
네 가능합니다!

구현할 때, `stack`이나 `que`를 쓰는 게 메모리 효율성이 떨어질 것이라고 생각햇는데...
막상 비교해보니 크게 차이가 없군요!😅

```py
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        que = deque()
        que.append(root)

        while len(que) > 0 :
            node = que.pop()
            node.left, node.right = node.right, node.left

            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)

        return root
```
````

### review_comment · daehyun99 · 2026-08-29T07:30:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3885936197
- ID: review_comment:3885936197
- 파일: course-schedule/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3880527934

````text
덕분에 Kahn 알고리즘도 알아가네요! 코멘트 감사합니다.
````

### review_comment · daehyun99 · 2026-08-29T08:03:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3885994890
- ID: review_comment:3885994890
- 파일: merge-k-sorted-lists/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3880542307

````text
공간복잡도를 최적화했더니, 이번엔 시간복잡도가 높아졌네요ㅎㅎ

나중에 다시 풀어봐야겠습니다.

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        idx = 0
        min_val = float("inf")
        dummy = ListNode()
        curr = dummy

        while any(lists):
            min_val = float("inf")
            for i in range(len(lists)):
                if lists[i] is not None:
                    if lists[i].val <= min_val:
                        idx = i
                        min_val = lists[i].val
            
            curr.next = ListNode(min_val)
            curr = curr.next
            lists[idx] = lists[idx].next
        return dummy.next
```
````

### review_comment · daehyun99 · 2026-08-29T08:19:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3886021586
- ID: review_comment:3886021586
- 파일: search-in-rotated-sorted-array/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3880566667

````text
풀어봤습니다

```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
            
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if target == nums[l]:
                return l
            if target == nums[m]:
                return m
            if target == nums[r]:
                return r
            if nums[l] <= nums[m] <= nums[r]:
                if target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[l] <= nums[m] and nums[r] <= nums[m]:
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[l] and nums[m] <= nums[r]:
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

```
````

### review_comment · daehyun99 · 2026-08-29T08:19:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3886022963
- ID: review_comment:3886022963
- 파일: invert-binary-tree/daehyun99.py, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3881613807

````text
생각해보니 그렇네요ㅎㅎ
````

### review_comment · alphaorderly · 2026-08-29T08:41:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3886066463
- ID: review_comment:3886066463
- 파일: invert-binary-tree/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3880293078

````text
오 iterative하게 하는것도 확실히 좋네요!
````

### review_comment · alphaorderly · 2026-08-29T08:43:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2838#discussion_r3886068986
- ID: review_comment:3886068986
- 파일: merge-k-sorted-lists/daehyun99.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3880542307

````text
힌트를 하나 드리자면 우리는 lists 라는 연결리스트가 잔뜩 있는 곳에서 "가장 작은 값" 을 가진 연결리스트를 빠르게 가져와야 하고 그 뒤에 "다음으로 작은 연결리스트"를 빠르게 찾아야 합니다.
해당 과정을 아주 손쉽게 할수 있는 자료구조가 있죠!
````

## [#2839 [dolphinflow86] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2839)

### review_comment · alphaorderly · 2026-08-29T08:50:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2839#discussion_r3886081461
- ID: review_comment:3886081461
- 파일: course-schedule/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
상당히 깔끔한 풀이시네요!
````

### review · dahyeong-yun · 2026-08-29T10:25:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2839#pullrequestreview-5057703164
- ID: review:5057703164
- 리뷰 상태: APPROVED

````text
고생하셨습니다. 전반적으로 잘 풀어주셔서 코멘트는 따로 남기지 않았습니다. 제가 못푼 문제 들도 덕분에 공부가 되었습니다 감사합니다! 
````

## [#2840 [dahyeong-yun] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2840)

### review_comment · Yiseull · 2026-08-29T06:49:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2840#discussion_r3885863319
- ID: review_comment:3885863319
- 파일: invert-binary-tree/dahyeong-yun.java, 줄: 16, 원래 줄: 16

````text
두 자식이 모두 null일 때, 어차피 null끼리 스왑해도 결과가 같으니까, `if(root.left != null || root.right != null)` 조건문이 없는게 더 가독성 측면에서 좋을 것 같아요~!
````

### review · Yiseull · 2026-08-29T06:50:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2840#pullrequestreview-5057209049
- ID: review:5057209049
- 리뷰 상태: APPROVED

````text
문제 푸느라 고생하셨습니다!!👍
````

### review_comment · dahyeong-yun · 2026-08-29T10:27:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2840#discussion_r3886317659
- ID: review_comment:3886317659
- 파일: invert-binary-tree/dahyeong-yun.java, 줄: 16, 원래 줄: 16
- 답글 대상: review_comment:3885863319

````text
그렇네요. 편향트리에서 null 케이스가 나왔을 때 거기까지 생각이 미쳤어야 했네요. 코멘트 감사합니다 :)
````

## [#2842 [sangbeenmoon] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2842)

### review_comment · alphaorderly · 2026-08-29T08:44:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2842#discussion_r3886071269
- ID: review_comment:3886071269
- 파일: course-schedule/sangbeenmoon.py, 줄: 1, 원래 줄: 1

````text
효율적인 사이클 탐색 알고리즘을 사용하셨네요
깔끔한 코드 잘 보고 갑니다.
````

### review_comment · alphaorderly · 2026-08-29T08:46:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2842#discussion_r3886073838
- ID: review_comment:3886073838
- 파일: jump-game/sangbeenmoon.py, 줄: 1, 원래 줄: 1

````text
해당 문제는 DP로도 접근이 가능하지만 놀랍게 그리디하게도 풀수 있으세요!
````

### review_comment · ICE0208 · 2026-08-29T13:23:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2842#discussion_r3886686947
- ID: review_comment:3886686947
- 파일: course-schedule/sangbeenmoon.py, 줄: 1, 원래 줄: 1

````text
DFS로 탐색하면서 사이클 여부를 판별하는 방법이군요!
좋은 풀이 잘 보고 갑니다 👍

````

### review · ICE0208 · 2026-08-29T13:23:24Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2842#pullrequestreview-5058168331
- ID: review:5058168331
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

## [#2843 [ICE0208] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2843)

### review_comment · parkhojeong · 2026-08-29T12:55:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2843#discussion_r3886632561
- ID: review_comment:3886632561
- 파일: course-schedule/ICE0208.java, 줄: 10, 원래 줄: 10

````text
graph 변수에 어떤 값이 들어가는지 관련 코드를 찾아 보고나서 이해가 되었던 거 같습니다. prerequisiteCourse 에 대한 nextCourses가 담기는데 의미를 나타내도록 네이밍을 하면 더 좋을 거 같습니다. 
````

### review_comment · parkhojeong · 2026-08-29T13:02:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2843#discussion_r3886646484
- ID: review_comment:3886646484
- 파일: course-schedule/ICE0208.java, 줄: 1, 원래 줄: 1

````text
graph와 indegree를 초기화 하는 부분과 실제 판단하는 부분으로 크게 나뉘는데 어디까지가 초기화고 어디부터가 실제 판단 로직인지 바로 알기는 어려웠던 거 같습니다. 초기화하는 부분 정도만 함수로 빼거나 초기화/판단 로직 구분이 되도록 주석으로 나타내면 어떨까 싶네요~
````

### review · parkhojeong · 2026-08-29T13:03:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2843#pullrequestreview-5058113065
- ID: review:5058113065
- 리뷰 상태: APPROVED

````text
간결하게 풀어주셔서 이해가 잘 되었습니다. 수고하셨습니다!
````

### review_comment · ICE0208 · 2026-08-29T13:28:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2843#discussion_r3886697097
- ID: review_comment:3886697097
- 파일: course-schedule/ICE0208.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3886646484

````text
그럴 수 있겠네요! 좋은 피드백 감사합니다 👍
````

## [#2844 [parkhojeong] WEEK 10 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2844)

### review_comment · alphaorderly · 2026-08-30T03:16:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2844#discussion_r3888339083
- ID: review_comment:3888339083
- 파일: merge-k-sorted-lists/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
특정 배열에서 동적으로 최소값을 찾는 자료구조가 있죠!
지금은 3000ms정도 시간이 소요되는데 이건 "출제자가 배우길 의도한 정답" 과는 좀 거리가 있을 것 같습니다.
시간복잡도를 최적화 해 보시는 것을 시도해 보시면 좋겠네요!
````

### review_comment · alphaorderly · 2026-08-30T03:21:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2844#discussion_r3888347413
- ID: review_comment:3888347413
- 파일: merge-k-sorted-lists/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3888339083

````text
최적화 하시면 5~11ms정도로 가능하십니다!
````

### review_comment · alphaorderly · 2026-08-30T03:23:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2844#discussion_r3888351012
- ID: review_comment:3888351012
- 파일: jump-game/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
해당 풀이는 Amortized O(N)에 가깝긴 하지만 개인적으로 불필요한 부분 **( 가장 멀리 갈수 있는 거리만 확인하면 되는데 모든 거리에 대해 갈수 있는지 여부를 확인함 )** 이 저장되어 있다는게 맘에 걸리네요
실제로 최적화시 시간은 4배가량 빨라질수 있고 공간 복잡도 또한 추가공간 O(1)에 가능하십니다.
````

### review_comment · alphaorderly · 2026-08-30T03:24:50Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2844#discussion_r3888353126
- ID: review_comment:3888353126
- 파일: invert-binary-tree/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
제 생각에 DFS 함수를 개별 구현하지 않고 invertTree 메서드 자체에서 바로 재귀하는것이 더 낫지 않을까? 싶습니다.
````

## [#2846 [alphaorderly] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2846)

### review_comment · dahyeong-yun · 2026-09-05T08:38:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2846#discussion_r3940031999
- ID: review_comment:3940031999
- 파일: reorder-list/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
중간을 미리 뒤집어 두고, 순방향이랑 역방향을 엇갈려 놓으면 풀리는 거군요. 이런 문제는 바로 아이디어가 떠오르시는지 궁금하네요.
````

### review_comment · dahyeong-yun · 2026-09-05T09:53:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2846#discussion_r3940207914
- ID: review_comment:3940207914
- 파일: missing-number/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
`XOR`도 교환법칙이 성립하는 군요. 깔끔하고 간결하게 풀어지네요.
````

### review · dahyeong-yun · 2026-09-05T11:19:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2846#pullrequestreview-5120541770
- ID: review:5120541770
- 리뷰 상태: COMMENTED

````text
한 주 수고하셨습니다. 제가 못푼 문제도 주석과 코드 덕에 참고가 됐네요 감사합니다!
````

### review_comment · alphaorderly · 2026-09-05T11:22:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2846#discussion_r3940428479
- ID: review_comment:3940428479
- 파일: reorder-list/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3940031999

````text
연결리스트 문제를 많이 풀다보니 직감이 오더리구요 ㅎㅎ
````

### review_comment · alphaorderly · 2026-09-05T11:23:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2846#discussion_r3940429305
- ID: review_comment:3940429305
- 파일: missing-number/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3940207914

````text
다른 비트마스킹 문제들에서도 해당 성질을 유용하게 사용하는게 많이 있기도 해서요!
````

### review_comment · okyungjin · 2026-09-05T14:07:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2846#discussion_r3940858352
- ID: review_comment:3940858352
- 파일: missing-number/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3940207914

````text
오... 이런 방법도 있군요
````

## [#2847 [dahyeong-yun] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2847)

### review_comment · alphaorderly · 2026-09-04T07:01:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2847#discussion_r3931679366
- ID: review_comment:3931679366
- 파일: missing-number/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
오 이런 방법도 있네요! 배워갑니다!!
````

### review_comment · yuseok89 · 2026-09-05T15:32:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2847#discussion_r3941091321
- ID: review_comment:3941091321
- 파일: reorder-list/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
SC O(1) 로 풀리는 풀이도 있으니 참고하세요 ~
````

### review · yuseok89 · 2026-09-05T15:33:49Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2847#pullrequestreview-5121849011
- ID: review:5121849011
- 리뷰 상태: APPROVED

````text
한 주 고생많으셨습니다 ~
````

## [#2848 [yuseok89] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2848)

### review_comment · alphaorderly · 2026-09-04T07:06:05Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3931706286
- ID: review_comment:3931706286
- 파일: binary-tree-maximum-path-sum/yuseok89.py, 줄: 1, 원래 줄: 1

````text
엄청 깔끔하게 해결하셨네요, 잘 보고 갑니다!
````

### review_comment · alphaorderly · 2026-09-04T07:06:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3931708722
- ID: review_comment:3931708722
- 파일: merge-intervals/yuseok89.py, 줄: 1, 원래 줄: 1

````text
구현 상당히 깔끔하게 잘 하셨네요
````

### review_comment · alphaorderly · 2026-09-04T07:08:19Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3931720042
- ID: review_comment:3931720042
- 파일: reorder-list/yuseok89.py, 줄: 1, 원래 줄: 1

````text
와우 엄청 깔끔하게 잘 푸셨네요
````

### review_comment · dolphinflow86 · 2026-09-04T16:17:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3935888024
- ID: review_comment:3935888024
- 파일: reorder-list/yuseok89.py, 줄: None, 원래 줄: 2

````text
@yuseok89 요거 재귀 호출인데 공간 복잡도가 재귀 호출 깊이만큼이라 O(N) 까지 깊어집니다.
한번 확인해보시면 좋을 것 같아요!
````

### review · dolphinflow86 · 2026-09-04T16:18:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#pullrequestreview-5115425473
- ID: review:5115425473
- 리뷰 상태: APPROVED

````text
수고많으셨습니다!
````

### review_comment · dolphinflow86 · 2026-09-04T16:23:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3935946491
- ID: review_comment:3935946491
- 파일: binary-tree-maximum-path-sum/yuseok89.py, 줄: None, 원래 줄: 2

````text
@yuseok89 여기도 공간복잡도가 스택 깊이만큼 깊어지는 부분 확인 해 보시면 좋을 것 같습니다~!
````

### review_comment · yuseok89 · 2026-09-04T16:56:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3936214654
- ID: review_comment:3936214654
- 파일: binary-tree-maximum-path-sum/yuseok89.py, 줄: None, 원래 줄: 2
- 답글 대상: review_comment:3935946491

````text
공간복잡도 계산 하면서 재귀부분을 자꾸 빼먹네요.
리뷰 감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-09-04T16:56:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2848#discussion_r3936217662
- ID: review_comment:3936217662
- 파일: reorder-list/yuseok89.py, 줄: None, 원래 줄: 2
- 답글 대상: review_comment:3935888024

````text
리뷰 감사합니다 🙏
````

## [#2849 [dolphinflow86] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2849)

### review_comment · alphaorderly · 2026-09-05T01:48:11Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3939047547
- ID: review_comment:3939047547
- 파일: merge-intervals/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
깔끔하게 잘 해결하셨네요!
다만 sort에 key는 적용하실 필요가 있으실지 한번 생각해 보시는것도 좋을것 같아요!
````

### review_comment · alphaorderly · 2026-09-05T01:48:38Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3939048765
- ID: review_comment:3939048765
- 파일: missing-number/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
해당문제는 사실상 본체가 공간복잡도 O(1)에 해결하는거라 한번 해보시죠!
````

### review_comment · alphaorderly · 2026-09-05T01:48:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3939049628
- ID: review_comment:3939049628
- 파일: reorder-list/dolphinflow86.py, 줄: 1, 원래 줄: 1

````text
깔끔한 풀이시네여!
````

### review · parkhojeong · 2026-09-05T11:45:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#pullrequestreview-5121115628
- ID: review:5121115628
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

### review_comment · okyungjin · 2026-09-05T11:47:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3940515328
- ID: review_comment:3940515328
- 파일: merge-intervals/dolphinflow86.py, 줄: None, 원래 줄: 10

````text
문제에 `1 <= intervals.length <= 104` 조건이 있기는 합니다!
````

### review · okyungjin · 2026-09-05T11:48:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#pullrequestreview-5121126958
- ID: review:5121126958
- 리뷰 상태: APPROVED

````text
수고하셨습니다!
````

### review_comment · dolphinflow86 · 2026-09-05T12:37:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3940651168
- ID: review_comment:3940651168
- 파일: missing-number/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3939048765

````text
감사합니다. 한번 시도 해 보겠습니다!
````

### review_comment · dolphinflow86 · 2026-09-05T12:42:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3940660112
- ID: review_comment:3940660112
- 파일: merge-intervals/dolphinflow86.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3939047547

````text
오 넵 짚어주셔서 감사합니다! 그냥 sort만 해도 되겠네요!
반영했습니다.
````

### review_comment · dolphinflow86 · 2026-09-05T12:42:42Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2849#discussion_r3940660818
- ID: review_comment:3940660818
- 파일: merge-intervals/dolphinflow86.py, 줄: None, 원래 줄: 10
- 답글 대상: review_comment:3940515328

````text
오 넵 따로 early return이 필요없겠네요. 감사합니다!
반영했습니다.
````

## [#2850 [okyungjin] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2850)

### review_comment · Yiseull · 2026-09-05T12:50:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2850#discussion_r3940677276
- ID: review_comment:3940677276
- 파일: missing-number/okyungjin.py, 줄: 43, 원래 줄: 43

````text
두 가지 문제 풀이로, 시간복잡도 더 개선된 풀이 보여주신 게 좋네요!👍
````

### review · Yiseull · 2026-09-05T12:57:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2850#pullrequestreview-5121341784
- ID: review:5121341784
- 리뷰 상태: APPROVED

````text
문제 푸느라 고생하셨습니다!👍
````

### issue_comment · okyungjin · 2026-09-05T13:57:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2850#issuecomment-5552295395
- ID: issue_comment:5552295395

````text
> 문제 푸느라 고생하셨습니다!👍

감사합니다❤️
````

## [#2851 [parkhojeong] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2851)

### review_comment · Yiseull · 2026-09-05T12:42:46Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2851#discussion_r3940660982
- ID: review_comment:3940660982
- 파일: missing-number/parkhojeong.py, 줄: 4, 원래 줄: 4

````text
정답 범위는 항상 0~n이니까 max 대신 len을 쓰면 더 효율적일 것 같아요!
````

### review_comment · Yiseull · 2026-09-05T12:46:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2851#discussion_r3940668576
- ID: review_comment:3940668576
- 파일: missing-number/parkhojeong.py, 줄: 7, 원래 줄: 7

````text
`num_set = set(range(N + 1))` 로 한 줄에 됩니다! 그리고 크로드한테 물어보니까 저 코드는 파이썬 레벨 루프가 C 레벨로 내려가서 눈에 띄게 빨라진다고 합니다!!👍
````

### review · Yiseull · 2026-09-05T12:48:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2851#pullrequestreview-5121324555
- ID: review:5121324555
- 리뷰 상태: APPROVED

````text
리뷰를 늦게 남겨서, 제 코멘트는 참고만 하시고 바로 머지하시면 될 것 같아요! 문제 푸느라 고생하셨습니다!!👍 
````

## [#2853 [Yiseull] WEEK 11 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2853)

### review_comment · okyungjin · 2026-09-05T14:11:21Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2853#discussion_r3940868783
- ID: review_comment:3940868783
- 파일: missing-number/Yiseull.java, 줄: 1, 원래 줄: 1

````text
파이썬에는 sum 함수가 있어서 찾아보니 자바에서는 아래와 같이 작성할 수 있는 것 같습니다!
for로 합산하는 것과 차이가 있으려나요?

Arrays.stream(nums).sum();
````

### review_comment · okyungjin · 2026-09-05T14:17:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2853#discussion_r3940887408
- ID: review_comment:3940887408
- 파일: merge-intervals/Yiseull.java, 줄: 1, 원래 줄: 1

````text
저는 정답 배열을 선언했는데, intervals 배열을 인플레이스로 수정한 후에 슬라이스하셨군요
````

### review · okyungjin · 2026-09-05T14:17:48Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2853#pullrequestreview-5121524794
- ID: review:5121524794
- 리뷰 상태: APPROVED

````text
고생하셨습니다🙂
````

### review_comment · Yiseull · 2026-09-06T05:29:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2853#discussion_r3943084856
- ID: review_comment:3943084856
- 파일: merge-intervals/Yiseull.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3940887408

````text
네넹! okyungjin님 리뷰 달 때 안그래도 인플레이스 방법 말씀드리려다가 말았었는데, 클로드 말로는 자바에서 인플레이스가 의미 있었던 건 ArrayList 증설 + 구간마다 clone() + toArray 복사가 한꺼번에 사라졌기 때문인데, 파이썬은 없어지는 게 리스트 객체 하나와 append 호출뿐이라 자바만큼에 큰 이득은 아니라고 하더라구요!
````

### review_comment · Yiseull · 2026-09-06T05:49:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2853#discussion_r3943119112
- ID: review_comment:3943119112
- 파일: missing-number/Yiseull.java, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3940868783

````text
자바에서 for문이랑 stream이랑 약간의 성능이랑 동작 차이가 있는데, 저는 이 풀이에서는 그런것까진 따지지 않고 for문을 쓰긴 했어요 ㅎ

클로드한테 물어보니 아래일 때 어떤 걸 선택하는게 좋은지 정리해주네요~!

- 데이터 변환·집계 파이프라인(filter → map → collect, groupingBy) → stream이 압도적으로 읽기 좋습니다
- 인덱스가 필요하거나 두 리스트를 동시에 순회 → for문
- 루프 내에서 외부 상태를 바꿔야 함 → for문 (stream에서 하면 side effect라 병렬 시 깨집니다)
- 조기 종료 + 복잡한 조건 분기 → for문
- 원시 타입 대량 연산의 핫패스 → for문, 혹은 IntStream
````

## [#2854 [alphaorderly] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2854)

### review_comment · yuseok89 · 2026-09-11T13:32:09Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2854#discussion_r3989614909
- ID: review_comment:3989614909
- 파일: serialize-and-deserialize-binary-tree/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
deserialize 를 재귀로 구현한 부분이 좋네요 !
````

### review · yuseok89 · 2026-09-11T13:38:04Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2854#pullrequestreview-5179201181
- ID: review:5179201181
- 리뷰 상태: APPROVED

````text
이번 한 주도 고생많으셨습니다.
````

### review_comment · alphaorderly · 2026-09-11T13:56:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2854#discussion_r3989832728
- ID: review_comment:3989832728
- 파일: serialize-and-deserialize-binary-tree/alphaorderly.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3989614909

````text
회원님 코드도 엄청 인상적이였어요! 깔끔하게 잘 하셨더라구요!
````

## [#2855 [yuseok89] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2855)

### review_comment · alphaorderly · 2026-09-09T13:23:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2855#discussion_r3968935301
- ID: review_comment:3968935301
- 파일: same-tree/yuseok89.py, 줄: 1, 원래 줄: 1

````text
너무 깔끔하고 좋은 코드이신데요!
얼리 리턴을 사용하시면 코드의 depth를 줄일수 있지 않을까 하는 아주 미세한 아쉬움이 있습니다!
물론 개인의 취향이긴 합니다!
````

### review_comment · DaleSeo · 2026-09-11T02:26:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2855#discussion_r3985403638
- ID: review_comment:3985403638
- 파일: non-overlapping-intervals/yuseok89.py, 줄: 2, 원래 줄: 2

````text
`sorted()`는 새 리스트를 만들지 않나요? 그럼 공간 복잡도가 `O(N)`이 될 수도 있겠네요.
````

### review_comment · DaleSeo · 2026-09-11T02:28:18Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2855#discussion_r3985413274
- ID: review_comment:3985413274
- 파일: remove-nth-node-from-end-of-list/yuseok89.py, 줄: 11, 원래 줄: 11

````text
`fwd`는 `forward`로 바로 읽히는데, `flw`는 `follow`의 줄임이겠죠?
````

### review · DaleSeo · 2026-09-11T02:29:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2855#pullrequestreview-5174420522
- ID: review:5174420522
- 리뷰 상태: APPROVED

````text
12주차도 수고하셨습니다! 얼마 안 남았네요 :)
````

### review_comment · yuseok89 · 2026-09-14T06:21:56Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2855#discussion_r4002661971
- ID: review_comment:4002661971
- 파일: remove-nth-node-from-end-of-list/yuseok89.py, 줄: 11, 원래 줄: 11
- 답글 대상: review_comment:3985413274

````text
늦게 확인했네요. 맞습니다. follow 입니다. 다음엔 좀 더 가독성 좋게 작성해보겠습니다.
````

### review_comment · yuseok89 · 2026-09-14T06:22:41Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2855#discussion_r4002665324
- ID: review_comment:4002665324
- 파일: non-overlapping-intervals/yuseok89.py, 줄: 2, 원래 줄: 2
- 답글 대상: review_comment:3985403638

````text
O(N) 이 맞겠네요.
이런 부분이 인터뷰에서 잘 못하고 있는 부분인 것 같습니다.
캐치해주셔서 감사합니다 ! :pray: 
````

## [#2856 [DaleSeo] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2856)

### review · dolphinflow86 · 2026-09-11T15:42:15Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2856#pullrequestreview-5180595156
- ID: review:5180595156
- 리뷰 상태: APPROVED

````text
@DaleSeo 깔끔하게 풀어주신 Rust 풀이 잘 보았습니다. sort_unstable_by_key 사용해서 추가 메모리 없이 in-place로 상수공간 처리 잘 되어있어서 효율적이네요! 수고하셨습니다!
````

## [#2857 [dolphinflow86] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2857)

### review · parkhojeong · 2026-09-11T18:07:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2857#pullrequestreview-5182016451
- ID: review:5182016451
- 리뷰 상태: APPROVED

````text
이번 주도 수고하셨습니다!
````

## [#2858 [parkhojeong] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2858)

### review_comment · alphaorderly · 2026-09-13T07:11:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2858#discussion_r3999045420
- ID: review_comment:3999045420
- 파일: remove-nth-node-from-end-of-list/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
이거 Single pass로 해결하는게 진짜 괜찮던데 한번 시도 해 보시는것도 좋겠네요
````

### review_comment · alphaorderly · 2026-09-13T07:12:20Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2858#discussion_r3999045984
- ID: review_comment:3999045984
- 파일: same-tree/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
초반에 엄청나게 많은 조건들 정리하는게 가독성 상 좋지 않을까요?
````

### review · alphaorderly · 2026-09-13T07:12:40Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2858#pullrequestreview-5189963819
- ID: review:5189963819
- 리뷰 상태: APPROVED

````text
고생하셨습니다.
````

### review_comment · parkhojeong · 2026-09-13T13:08:52Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2858#discussion_r3999704294
- ID: review_comment:3999704294
- 파일: remove-nth-node-from-end-of-list/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3999045420

````text
네 한 번 시도해보겠습니다!
````

### review_comment · parkhojeong · 2026-09-13T13:09:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2858#discussion_r3999704673
- ID: review_comment:3999704673
- 파일: same-tree/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:3999045984

````text
정리하는게 좋겠네요. 감사합니다!
````

## [#2859 [dahyeong-yun] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2859)

### review_comment · okyungjin · 2026-09-12T09:41:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2859#discussion_r3995814510
- ID: review_comment:3995814510
- 파일: non-overlapping-intervals/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
end 기준으로 정렬한 후에 **남길 구간의 개수**를 세고, 전체 구간의 개수에서 빼주는 로직으로 이해했습니다.
저는 **제거할 구간의 개수**를 세도록 구현했는데 이 점이 다르네요. 
````

### review_comment · okyungjin · 2026-09-12T09:43:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2859#discussion_r3995824620
- ID: review_comment:3995824620
- 파일: remove-nth-node-from-end-of-list/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
달레 스터디 리뷰에도 있는데 공간 복잡도 O(1)로 개선할 수 있는 것 같습니다 ㅎㅎ
저번 주 문제 중에 비슷한 방법이 있던 것 같아요

> 개선 제안: 공간 복잡도를 줄이려면 더블 포인터(스피닝) 기법으로 O(1) 공간으로 개선할 수 있습니다.


````

### review_comment · okyungjin · 2026-09-12T09:52:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2859#discussion_r3995859061
- ID: review_comment:3995859061
- 파일: same-tree/dahyeong-yun.java, 줄: 1, 원래 줄: 1

````text
재귀 사용해서 DFS로 깔끔하게 풀어주셨네요.
혹시 DFS 풀이를 선택하신 이유가 있을까요?
````

### review · okyungjin · 2026-09-12T09:52:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2859#pullrequestreview-5186033958
- ID: review:5186033958
- 리뷰 상태: APPROVED

````text
고생하셨습니다 : )
````

## [#2860 [okyungjin] WEEK 12 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2860)

### review · parkhojeong · 2026-09-12T13:45:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2860#pullrequestreview-5186575863
- ID: review:5186575863
- 리뷰 상태: APPROVED

````text
수고 많으셨습니다!
````

## [#2861 [alphaorderly] WEEK 13 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2861)

### review_comment · DaleSeo · 2026-09-18T00:27:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2861#discussion_r4042592461
- ID: review_comment:4042592461
- 파일: find-median-from-data-stream/alphaorderly.py, 줄: 17, 원래 줄: 17

````text
오, `heappush_max`와 `heappop_max`는 처음 보네요. 덕분에 새로운 API 배워가네요 👍
````

### review_comment · DaleSeo · 2026-09-18T00:32:01Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2861#discussion_r4042619893
- ID: review_comment:4042619893
- 파일: kth-smallest-element-in-a-bst/alphaorderly.py, 줄: 26, 원래 줄: 26

````text
아래 `while right:` 때문에 이 가드는 필요없지 않을까요?
````

### review · DaleSeo · 2026-09-18T00:32:17Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2861#pullrequestreview-5242804985
- ID: review:5242804985
- 리뷰 상태: APPROVED

````text
수고하셨습니다. 화이팅!
````

### review_comment · alphaorderly · 2026-09-18T00:33:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2861#discussion_r4042630788
- ID: review_comment:4042630788
- 파일: find-median-from-data-stream/alphaorderly.py, 줄: 17, 원래 줄: 17
- 답글 대상: review_comment:4042592461

````text
3.14에서 추가되었더라구요!!
원래는 불편함 때문에 MaxHeap 클래스를 따로 만들어 쓰는 편이였는데 너무 좋아요
````

### review_comment · alphaorderly · 2026-09-18T00:34:59Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2861#discussion_r4042638701
- ID: review_comment:4042638701
- 파일: kth-smallest-element-in-a-bst/alphaorderly.py, 줄: 26, 원래 줄: 26
- 답글 대상: review_comment:4042619893

````text
맞네요!!
````

## [#2862 [DaleSeo] WEEK 13 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2862)

### review_comment · yuseok89 · 2026-09-19T12:14:03Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2862#discussion_r4053143388
- ID: review_comment:4053143388
- 파일: insert-interval/DaleSeo.rs, 줄: 1, 원래 줄: 1

````text
이 풀이 좋네요. 많이 배웠습니다!
````

### review · yuseok89 · 2026-09-19T12:14:29Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2862#pullrequestreview-5255682660
- ID: review:5255682660
- 리뷰 상태: APPROVED

````text
한 주도 수고많으셨습니다 !
````

## [#2863 [yuseok89] WEEK 13 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2863)

### review_comment · dolphinflow86 · 2026-09-19T11:19:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2863#discussion_r4053050143
- ID: review_comment:4053050143
- 파일: insert-interval/yuseok89.py, 줄: None, 원래 줄: 24

````text
1 pass로 깔끔하게 병합하신 아이디어가 좋은 것 같습니다. TD는 TC의 오타가 맞을까요?
````

### review_comment · dolphinflow86 · 2026-09-19T11:20:13Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2863#discussion_r4053051773
- ID: review_comment:4053051773
- 파일: lowest-common-ancestor-of-a-binary-search-tree/yuseok89.py, 줄: None, 원래 줄: 2

````text
공간복잡도가 재귀 호출의 분석이 빠져있는 것 같습니다 :)
````

### review · dolphinflow86 · 2026-09-19T11:20:23Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2863#pullrequestreview-5255584178
- ID: review:5255584178
- 리뷰 상태: APPROVED

````text
이번주도 수고 많으셨습니다!
````

### review_comment · yuseok89 · 2026-09-19T11:44:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2863#discussion_r4053093848
- ID: review_comment:4053093848
- 파일: lowest-common-ancestor-of-a-binary-search-tree/yuseok89.py, 줄: None, 원래 줄: 2
- 답글 대상: review_comment:4053051773

````text
맞습니다. 리뷰 감사합니다 🙏 
````

### review_comment · yuseok89 · 2026-09-19T11:44:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2863#discussion_r4053094193
- ID: review_comment:4053094193
- 파일: insert-interval/yuseok89.py, 줄: None, 원래 줄: 24
- 답글 대상: review_comment:4053050143

````text
오타 수정했습니다. 감사합니다 !
````

## [#2864 [dolphinflow86] WEEK 13 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2864)

### review · parkhojeong · 2026-09-19T14:49:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2864#pullrequestreview-5256062008
- ID: review:5256062008
- 리뷰 상태: COMMENTED

````text
이번 주도 수고하셨습니다. 이전 주차 풀이가 포함되어 있는데 제거 부탁드립니다~
````

## [#2866 [okyungjin] WEEK 14 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2866)

### review_comment · okyungjin · 2026-09-21T16:20:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4064123056
- ID: review_comment:4064123056
- 파일: meeting-rooms/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4064081776

````text
@dalestudy 유형 불일치야? 모범답안 알려줘
````

### review_comment · alphaorderly · 2026-09-23T02:14:39Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4078405774
- ID: review_comment:4078405774
- 파일: binary-tree-level-order-traversal/okyungjin.py, 줄: 1, 원래 줄: 1

````text
확실히 레벨오더는 큐를 쓰는게 가장 깔끔한거 같긴 해요
````

### review_comment · alphaorderly · 2026-09-23T02:15:34Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4078409511
- ID: review_comment:4078409511
- 파일: house-robber-ii/okyungjin.py, 줄: 1, 원래 줄: 1

````text
진짜 함수로 일반화 하는게 맞았나 싶기도 하네요 
깔끔한 코드 좋아요!
````

### review_comment · alphaorderly · 2026-09-23T02:16:08Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4078412167
- ID: review_comment:4078412167
- 파일: meeting-rooms-ii/okyungjin.py, 줄: 1, 원래 줄: 1

````text
오 ㅋㅋㅋ 저랑 거의 완벽하게 동일한 풀이를 사용하셨네요
신기합니다!
````

### review_comment · okyungjin · 2026-09-23T12:22:55Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4082353021
- ID: review_comment:4082353021
- 파일: meeting-rooms-ii/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4078412167

````text
고민하다가 도저히 모르겠어서 클로드의 도움을 살짝 받았습니다 ㅎㅎ
해답이 재밌었어요 👍
````

### review_comment · okyungjin · 2026-09-23T12:23:57Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4082361677
- ID: review_comment:4082361677
- 파일: binary-tree-level-order-traversal/okyungjin.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4078405774

````text
오홍 체감을 위해 다른 방법으로도 풀어봐야겠네요
````

### review_comment · yuseok89 · 2026-09-25T14:13:28Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4105367476
- ID: review_comment:4105367476
- 파일: counting-bits/okyungjin.py, 줄: 13, 원래 줄: 13

````text
반환값은 복잡도에 포함하지 않은것이지요?
````

### review · yuseok89 · 2026-09-25T16:19:26Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#pullrequestreview-5318713102
- ID: review:5318713102
- 리뷰 상태: APPROVED

````text
지난주차 문제까지 풀어주시고 열정적이십니다 👏 👏 
이번주도 고생 많으셨습니다 !
````

### review_comment · okyungjin · 2026-09-26T08:34:32Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2866#discussion_r4110716905
- ID: review_comment:4110716905
- 파일: counting-bits/okyungjin.py, 줄: 13, 원래 줄: 13
- 답글 대상: review_comment:4105367476

````text
> 반환값은 복잡도에 포함하지 않은것이지요?

@yuseok89 네 맞습니다! 
````

## [#2867 [yuseok89] WEEK 14 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2867)

### review_comment · alphaorderly · 2026-09-23T02:10:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2867#discussion_r4078387281
- ID: review_comment:4078387281
- 파일: binary-tree-level-order-traversal/yuseok89.py, 줄: 1, 원래 줄: 1

````text
엄청 깔끔하게 잘 해결하셨네요!
정말 아주 억지로 트집잡자면 재귀가 트리의 높이만큼 스택이 쌓이니까 Iterative하게 시도해 보는거를 한번 해보시는것도 좋다는 정도려나요?
깔끔한 코드 잘 보고 갑니다!
````

### review_comment · alphaorderly · 2026-09-23T02:10:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2867#discussion_r4078390234
- ID: review_comment:4078390234
- 파일: binary-tree-level-order-traversal/yuseok89.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4078387281

````text
진짜 회원님 코드 볼때마다 느끼는거지만 Leetcode Study 처음 오셨을때랑 지금이랑 차이가 어마어마하신것 같아서 대단한거 같아요
고생이 많으십니다!
````

### review_comment · alphaorderly · 2026-09-23T02:12:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2867#discussion_r4078396280
- ID: review_comment:4078396280
- 파일: counting-bits/yuseok89.py, 줄: 1, 원래 줄: 1

````text
상당히 깔끔하게 잘 해결하셨네요!
````

### review_comment · alphaorderly · 2026-09-23T02:13:02Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2867#discussion_r4078399303
- ID: review_comment:4078399303
- 파일: house-robber-ii/yuseok89.py, 줄: 1, 원래 줄: 1

````text
오 문제를 함수로 일반화 하신다음에 따로 두가지 경우로 구현하셨네요
그 덕분에 코드가 상당히 가독성이 좋아지는것 같아요!
````

### review · alphaorderly · 2026-09-23T02:13:27Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2867#pullrequestreview-5286098366
- ID: review:5286098366
- 리뷰 상태: APPROVED

````text
좋아요!
````

## [#2868 [alphaorderly] WEEK 14 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2868)

### review_comment · DaleSeo · 2026-09-24T23:02:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2868#discussion_r4099342605
- ID: review_comment:4099342605
- 파일: word-search-ii/alphaorderly.py, 줄: 83, 원래 줄: 83

````text
굳이 ans에 세트를 할당하고 마지막에 다시 리스트로 바꿀 이유가 있을까요? 같은 단어가 다시 추가될 수 있는 경우가 있는지 생각해보시면 좋을 것 같습니다.
````

### review_comment · DaleSeo · 2026-09-24T23:04:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2868#discussion_r4099355304
- ID: review_comment:4099355304
- 파일: house-robber-ii/alphaorderly.py, 줄: 5, 원래 줄: 5

````text
점화식을 보면 길이가 n인 리스트 대신에 변수 2개만 있어도 충분할 것 같네요? 메모리 최적화의 기회가 보입니다.
````

### review · DaleSeo · 2026-09-24T23:05:31Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2868#pullrequestreview-5311234380
- ID: review:5311234380
- 리뷰 상태: APPROVED

````text
추선 연휴에도 거르지 않고 문제푸는 모습 멋집니다! 👍
````

### review_comment · parkhojeong · 2026-09-27T03:28:07Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2868#discussion_r4113956030
- ID: review_comment:4113956030
- 파일: house-robber-ii/alphaorderly.py, 줄: 27, 원래 줄: 27

````text
하나의 루프에서 두 가지 동작을 하네요. prev2, prev1 변수를 사용하는 하나의 헬퍼 함수를 두면 공간 복잡도가 O(1)로 줄고 가독성도 개선할 수 있을 거 같습니다.
````

### review · parkhojeong · 2026-09-27T03:28:37Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2868#pullrequestreview-5328696386
- ID: review:5328696386
- 리뷰 상태: APPROVED

````text
이번 주도 수고하셨습니다.
````

## [#2869 [DaleSeo] WEEK 14 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2869)

### review_comment · alphaorderly · 2026-09-26T02:17:44Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2869#discussion_r4109858231
- ID: review_comment:4109858231
- 파일: house-robber-ii/DaleSeo.rs, 줄: 1, 원래 줄: 1

````text
러스트 코드는 볼때마다 느끼는거지만 엄청 복잡하게 느껴지는것 같아요 그러면서 로직은 엄청 깔끔하게 보여서 또 신기합니다!
고생하셨습니다!
````

### review · parkhojeong · 2026-09-26T12:50:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2869#pullrequestreview-5325956466
- ID: review:5325956466
- 리뷰 상태: APPROVED

````text
이번 주도 수고하셨습니다~!
````

### review_comment · DaleSeo · 2026-09-26T16:43:58Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2869#discussion_r4112029745
- ID: review_comment:4112029745
- 파일: house-robber-ii/DaleSeo.rs, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4109858231

````text
러스트의 매력입니다 ㅎㅎ
````

## [#2870 [parkhojeong] WEEK 14 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2870)

### review_comment · alphaorderly · 2026-09-26T02:04:36Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4109824201
- ID: review_comment:4109824201
- 파일: binary-tree-level-order-traversal/parkhojeong.py, 줄: 13, 원래 줄: 14

````text
deque의 경우 deque([root]) 처럼 리스트를 제공해서 바로 초기화가 가능하세요!
````

### review_comment · alphaorderly · 2026-09-26T02:05:47Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4109827075
- ID: review_comment:4109827075
- 파일: binary-tree-level-order-traversal/parkhojeong.py, 줄: None, 원래 줄: 29

````text
매 레벨마다 데크를 새로 초기화 하기 보다는 한 레벨에서 우리가 사용할 부모의 갯수를 알고 있다면 while 같이 모든 데크의 내용을 부모로 쓰기 보다는 우리가 필요한 만큼만 써서 하나의 데크를 계속 재활용 할수 있지 않을까요?
````

### review_comment · alphaorderly · 2026-09-26T02:08:12Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4109832689
- ID: review_comment:4109832689
- 파일: counting-bits/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
우리가 이전에 계산한 값들을 활용한다면 더 빠른 계산이 가능하지 않을까 해요

예를 들어 5의 경우 101이죠? 근데 이걸 오른쪽으로 쉬프트를 해주면 10이 되구요 이건 2가 될거에요

2의 1 비트 갯수가 1개라는것은 우리가 이전에 미리 계산해 둘수 있고, 101에서 맨 오른쪽 비트값이 1인지는 x & 1 같은 연산 혹은 x % 2 와 같은 연산으로 바로 확인이 가능하죠

이와 비슷하게 11011의 비트 갯수는 1101 + (11011의 마지막 비트가 1인가) 로 일반화 할수 있을거에요
````

### review_comment · alphaorderly · 2026-09-26T02:11:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4109842119
- ID: review_comment:4109842119
- 파일: house-robber-ii/parkhojeong.py, 줄: 1, 원래 줄: 1

````text
정말 깔끔하게 풀어주시긴 했는데요! 만약 실제 코딩 테스트에서 꼬리질문이 들어온다면  
`왜 dp 배열의 이름을 prefix_sum이라고 하셨나요?` 같은 질문이 나올 수도 있을 것 같아요.

prefix sum의 경우에는 실제로 맨 앞 인덱스부터 자기 자신의 인덱스까지 값이 누적되어 있어야 하는데, 해당 경우에는 도둑이 집을 연달아 털 수 없어서 중간중간 끊기는 값이 저장되니까요! 그래서 `prefix_sum`보다는 `dp` 같은 이름이 조금 더 적절하지 않을까 싶습니다.
````

### review_comment · parkhojeong · 2026-09-26T14:59:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4111739548
- ID: review_comment:4111739548
- 파일: counting-bits/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4109832689

````text
계산된 비트 사용하도록 최적화 해주었습니다~
````

### review_comment · parkhojeong · 2026-09-26T15:00:53Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4111743338
- ID: review_comment:4111743338
- 파일: house-robber-ii/parkhojeong.py, 줄: 1, 원래 줄: 1
- 답글 대상: review_comment:4109842119

````text
별도 함수를 선언해서 가독성을 좀 개선해봤습니다~
````

### review_comment · parkhojeong · 2026-09-26T15:01:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4111746619
- ID: review_comment:4111746619
- 파일: binary-tree-level-order-traversal/parkhojeong.py, 줄: None, 원래 줄: 29
- 답글 대상: review_comment:4109827075

````text
> 매 레벨마다 데크를 새로 초기화 하기 보다는 한 레벨에서 우리가 사용할 부모의 갯수를 알고 있다면 while 같이 모든 데크의 내용을 부모로 쓰기 보다는 우리가 필요한 만큼만 써서 하나의 데크를 계속 재활용 할수 있지 않을까요?

무슨 말씀인지 잘 이해가 되지 않아서 다시 한 번 설명해주시면 감사하겠습니다.
````

### review_comment · parkhojeong · 2026-09-26T15:02:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4111749958
- ID: review_comment:4111749958
- 파일: binary-tree-level-order-traversal/parkhojeong.py, 줄: 13, 원래 줄: 14
- 답글 대상: review_comment:4109824201

````text
오 몰랐네요~ 감사합니다!
````

### review_comment · alphaorderly · 2026-09-26T15:05:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4111759406
- ID: review_comment:4111759406
- 파일: binary-tree-level-order-traversal/parkhojeong.py, 줄: None, 원래 줄: 29
- 답글 대상: review_comment:4109827075

````text
```
size = len(deque)
```
이런식으로 현재 데크의 길이를 가져온 다음에
```
for _ in range(size):
```
로 원래 데크의 크기만큼만 순회하도록 하는겁니다, 이러면 새로 추가되는 자식들은 해당 루프에서 순회될 일이 아예 없으니까 데크를 새로 만들 필요가 일절 없게 되지요
````

### review · alphaorderly · 2026-09-26T15:06:25Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#pullrequestreview-5326329615
- ID: review:5326329615
- 리뷰 상태: APPROVED

````text
너무 좋습니다!
````

### review_comment · parkhojeong · 2026-09-26T15:22:14Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2870#discussion_r4111804398
- ID: review_comment:4111804398
- 파일: binary-tree-level-order-traversal/parkhojeong.py, 줄: None, 원래 줄: 29
- 답글 대상: review_comment:4109827075

````text
개수 사용해서 루프 돌도록 개선해주었습니다~
````

## [#2873 [dolphinflow86] WEEK 14 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2873)

### review_comment · parkhojeong · 2026-09-27T03:14:16Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2873#discussion_r4113927783
- ID: review_comment:4113927783
- 파일: house-robber-ii/dolphinflow86.py, 줄: 20, 원래 줄: 20

````text
prev2, prev1 을 사용하니 로직이 더 명확하게 보이네요.
````

### review · parkhojeong · 2026-09-27T03:21:06Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2873#pullrequestreview-5328669694
- ID: review:5328669694
- 리뷰 상태: APPROVED

````text
이번 주도 수고하셨습니다!
````

## [#2874 [DaleSeo] WEEK 15 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2874)

### review · alphaorderly · 2026-09-30T01:52:54Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2874#pullrequestreview-5360566452
- ID: review:5360566452
- 리뷰 상태: APPROVED

````text
중앙점을 찾아서 늘려나가면서 가장 긴 회문을 찾는것을 깔끔하게 구현하신것 같습니다!
고생하셨습니다!
````

## [#2876 [alphaorderly] WEEK 15 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2876)

### review_comment · yuseok89 · 2026-10-03T14:03:51Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2876#discussion_r4173464014
- ID: review_comment:4173464014
- 파일: subtree-of-another-tree/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
이런 방법도 있군요
````

### review_comment · yuseok89 · 2026-10-03T14:04:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2876#discussion_r4173465268
- ID: review_comment:4173465268
- 파일: rotate-image/alphaorderly.py, 줄: 1, 원래 줄: 1

````text
간결하게 나왔네요 !
````

### review · yuseok89 · 2026-10-03T14:04:45Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2876#pullrequestreview-5401141675
- ID: review:5401141675
- 리뷰 상태: APPROVED

````text
15주동안 고생 많이 하셨습니다
````

## [#2877 [yuseok89] WEEK 15 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2877)

### review_comment · dolphinflow86 · 2026-10-02T14:42:22Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2877#discussion_r4166787207
- ID: review_comment:4166787207
- 파일: subtree-of-another-tree/yuseok89.py, 줄: 39, 원래 줄: 39

````text
같은 트리인 경우 가지치기로 처리하신 부분이 인상깊네요!
풀이 잘 보았습니다!
````

### review · dolphinflow86 · 2026-10-02T14:42:43Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2877#pullrequestreview-5393125635
- ID: review:5393125635
- 리뷰 상태: APPROVED

````text
지난 15주간 정말 고생 많으셨습니다!
````

### issue_comment · yuseok89 · 2026-10-03T14:05:30Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2877#issuecomment-5969919745
- ID: issue_comment:5969919745

````text
> 지난 15주간 정말 고생 많으셨습니다!

고생많으셨습니다 !! 💯 
````

## [#2878 [dolphinflow86] WEEK 15 Solutions](https://github.com/DaleStudy/leetcode-study/pull/2878)

### review · parkhojeong · 2026-10-04T02:32:00Z
- 원문: https://github.com/DaleStudy/leetcode-study/pull/2878#pullrequestreview-5403938665
- ID: review:5403938665
- 리뷰 상태: APPROVED

````text
마지막 주까지 수고 많으셨습니다!
````

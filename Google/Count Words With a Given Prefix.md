# Count Words With a Given Prefix

- **Topic:** #string #linear-scan #binary-search #prefix
- **Updated:** Oct 15, 2026

## 문제

사전순으로 정렬된 문자열 배열 `words`와 문자열 `prefix`가 주어진다. **`prefix`로 시작하는 단어의 개수**를 반환한다.

접두사란 문자열의 맨 앞부분이다. 단어 전체가 `prefix`와 같아도 포함하며, 중복 단어는 각각 센다.

```text
입력: words = ["app", "apple", "application", "banana"], prefix = "app"
출력: 3
설명: "app", "apple", "application"이 "app"으로 시작한다.

입력: words = ["apple", "banana", "cherry"], prefix = "cat"
출력: 0

입력: words = ["car", "car", "card", "care", "dog"], prefix = "car"
출력: 4
```

## 풀이: 선형 탐색

단어를 처음부터 끝까지 한 번 순회하고, `word.startswith(prefix)`가 참일 때마다 카운트를 1 증가시킨다. 마지막에 카운트를 반환한다.

```python
from typing import List


class Solution:
    def countWords(self, words: List[str], prefix: str) -> int:
        count = 0

        for word in words:
            if word.startswith(prefix):
                count += 1

        return count
```

`startswith`는 문자열이 지정된 접두사로 시작하는지 확인한다.

```python
"apple".startswith("app")   # True
"app".startswith("app")     # True: 단어 전체와 같아도 포함
"snapple".startswith("app") # False: 중간에 등장하는 것은 제외
"ap".startswith("app")      # False: 단어가 접두사보다 짧음
```

### 순회 예시

`prefix = "app"`일 때:

| 현재 단어 | `startswith(prefix)` | 처리 후 `count` |
| --- | --- | --- |
| `"app"` | `True` | 1 |
| `"apple"` | `True` | 2 |
| `"application"` | `True` | 3 |
| `"banana"` | `False` | 3 |

## 왜 맞는가?

매 반복이 끝날 때 `count`는 **지금까지 확인한 단어 중 `prefix`로 시작하는 단어의 개수**이다. 각 단어를 정확히 한 번 확인하고 조건에 맞는 경우에만 1을 더하므로, 순회가 끝나면 전체 배열의 정답이 된다.

## 복잡도

`n`은 단어 개수, `p`는 접두사 길이이다.

- **시간: O(n × p)**. 단어 `n`개를 확인하며, `startswith`는 단어당 최악 O(p)의 문자 비교를 한다. 접두사 길이를 상수로 보면 단어 개수에 대해 O(n)이다.
- **추가 공간: O(1)**. 별도 결과 배열이나 문자열 복사 없이 카운터만 유지한다.

## 풀이 2: 이진 탐색으로 양쪽 경계 찾기

`words`가 **사전순으로 정렬되어 있으므로**, 같은 접두사로 시작하는 단어들은 연속해서 모여 있다. 각 단어의 앞 `p = len(prefix)`글자인 `word[:p]`만 비교해도 정렬 순서는 유지된다.

두 번의 이진 탐색으로 다음 경계를 찾는다.

1. `start`: `word[:p] >= prefix`인 첫 위치 (lower bound).
2. `end`: `word[:p] > prefix`인 첫 위치 (upper bound).

그러면 `[start, end)`에 있는 단어들만 접두사가 일치하므로 정답은 **`end - start`**이다. 조건을 만족하는 위치가 없으면 배열 길이 `n`을 경계로 사용한다.

```python
from typing import List


class Solution:
    def countWords(self, words: List[str], prefix: str) -> int:
        p = len(prefix)
        n = len(words)

        # prefix 이상인 첫 위치
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if words[mid][:p] < prefix:
                left = mid + 1
            else:
                right = mid
        start = left

        # prefix보다 큰 첫 위치
        left, right = start, n
        while left < right:
            mid = (left + right) // 2
            if words[mid][:p] <= prefix:
                left = mid + 1
            else:
                right = mid
        end = left

        return end - start
```

### 경계 예시

```text
words       = ["ant", "app", "apple", "application", "banana"]
word[:3]    = ["ant", "app", "app",   "app",         "ban"]
index       =    0      1      2        3              4
                       ↑                             ↑
                     start = 1                     end = 4

정답 = 4 - 1 = 3
```

`prefix = "az"`처럼 일치하는 단어가 없으면 두 경계가 같은 위치를 가리켜 `0`을 반환한다. 빈 배열도 두 경계가 모두 `0`이다. 빈 접두사라면 모든 `word[:0]`가 `""`이므로 전체 단어 개수를 반환한다.

### 왜 맞는가?

정렬된 배열에서 `word[:p]`는 `prefix`보다 작은 구간, 같은 구간, 큰 구간 순서로 나타난다. 첫 탐색은 작은 구간을 제외한 첫 위치를, 두 번째 탐색은 같은 구간까지 제외한 첫 위치를 찾는다. 따라서 두 위치 사이에는 `word[:p] == prefix`, 즉 `word.startswith(prefix)`인 단어만 있고, 중복도 빠짐없이 포함된다.

두 탐색 모두 탐색 구간을 `[left, right)`로 유지한다. `mid`가 조건보다 작으면 `left = mid + 1`, 경계 후보이면 `right = mid`로 줄여 나가며, `left == right`가 되면 해당 경계가 확정된다. 두 탐색의 차이는 비교 연산자 `<`와 `<=`이다.

### 복잡도

- **시간: O(p × log n)** (`n >= 2`). 이진 탐색을 두 번 하며, 매 단계의 문자열 슬라이싱과 비교는 최악 O(p)이다. 빈 접두사까지 포함한 표현은 O((p + 1) × log(n + 1))이다.
- **추가 공간: O(p)**. Python의 `words[mid][:p]`가 최대 `p`글자의 임시 문자열을 만든다. 모든 단어를 미리 잘라 별도 배열에 저장하지는 않는다.
- 이미 정렬된 입력을 활용하는 풀이이다. 정렬되지 않았다면 먼저 정렬하는 비용이 추가된다.

## 기억할 것 / 헷갈릴 수 있는 지점

- **접두사는 맨 앞에서 일치해야 한다.** `prefix in word`는 중간에 등장해도 참이므로 이 문제의 조건과 다르다.
- 중복 단어도 각각 세므로 `set(words)`로 바꾸지 않는다.
- 첫 번째로 일치하는 단어를 찾았다고 바로 반환하지 않는다. 끝까지 세어야 한다.
- 처음에 일치하지 않는 단어가 나와도 뒤에 일치하는 단어가 있을 수 있다. 예를 들어 `["ant", "apple"]`, `prefix = "app"`에서 `"ant"`를 보고 종료하면 안 된다.
- 빈 배열이나 일치하는 단어가 없는 경우에는 초기값 `0`이 그대로 반환된다.
- 정렬되어 있다는 조건은 이진 탐색에 활용할 수 있지만, 이 선형 탐색 풀이에는 정렬 여부가 영향을 주지 않는다.
- 이진 탐색에서는 **앞 `p`글자**를 비교한다. 단어 전체에 `<= prefix`를 적용하면 `"apple" > "app"`이므로 일치 구간의 끝을 잘못 찾는다.
- `startswith(prefix)`만으로는 전체 배열을 이진 탐색할 수 없다. 결과가 `False → True → False`일 수 있으므로, 사전순 비교로 경계의 어느 쪽인지 판단한다.
- **기억할 한 문장: 모든 단어를 한 번씩 확인하고, `startswith(prefix)`가 참일 때만 1을 더한다.**

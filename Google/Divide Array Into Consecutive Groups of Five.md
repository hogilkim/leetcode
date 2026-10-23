# Divide Array Into Consecutive Groups of Five

- **Topic:** #greedy #counter #sorting
- **Updated:** Oct 14, 2026
- 문제 번호와 입력 크기 제한은 제공되지 않았다.

## 문제

정수 배열 `nums`의 모든 원소를 **정확히 5개의 연속된 정수로 이루어진 그룹**으로 나눌 수 있으면 `True`, 없으면 `False`를 반환한다.

각 그룹은 정렬했을 때 `[x, x + 1, x + 2, x + 3, x + 4]` 형태여야 한다.

- 원래 배열의 순서는 상관없다. 그룹의 원소가 배열에서 붙어 있을 필요도 없다.
- 모든 원소를 정확히 한 번 사용해야 한다.
- 배열에 중복 값이 있어도 된다. 단, 같은 그룹 안에서는 값이 중복될 수 없으므로 각 복사본을 서로 다른 그룹에 배치해야 한다.

| 입력 | 결과 | 설명 |
| --- | --- | --- |
| `[1,2,3,4,5,2,3,4,5,6]` | `True` | `[1,2,3,4,5]`, `[2,3,4,5,6]` |
| `[5,1,4,2,3]` | `True` | 순서를 바꾸면 `[1,2,3,4,5]` |
| `[1,1,2,2,3,3,4,4,5,5]` | `True` | `[1,2,3,4,5]` 두 그룹 |
| `[1,1,2,2,3,3,4,4,5,6]` | `False` | 1로 시작하는 두 그룹에 필요한 5가 하나 부족하다 |
| `[1,2,3,4,5,6]` | `False` | 원소 수가 5의 배수가 아니다 |

## 풀이: 빈도표 + 가장 작은 값부터 Greedy

**남은 값 중 가장 작은 값은 반드시 새로운 그룹의 시작이어야 한다.** 그 값보다 작은 원소가 남아 있지 않으므로 그룹의 두 번째 이후 자리에 배치할 수 없다.

가장 작은 값 `start`가 `copies`개 남아 있다면, `start`로 시작하는 그룹을 정확히 `copies`개 만들어야 한다. 따라서 `start + 1`부터 `start + 4`까지도 각각 최소 `copies`개가 필요하다.

1. 배열 길이가 5의 배수가 아니면 `False`를 반환한다.
2. `Counter(nums)`로 각 값의 남은 개수를 저장한다.
3. 키를 오름차순으로 순회한다. 이미 모두 사용한 값은 건너뛴다.
4. 현재 값의 개수 `copies`를 저장하고, 연속된 다섯 값에서 각각 `copies`개를 차감한다.
5. 필요한 개수가 부족하면 `False`, 끝까지 처리하면 `True`를 반환한다.

## 정답 코드

```python
from collections import Counter
from typing import List


class Solution:
    def canDivideIntoGroups(self, nums: List[int]) -> bool:
        if len(nums) % 5 != 0:
            return False

        count = Counter(nums)

        for start in sorted(count):
            copies = count[start]

            if copies == 0:
                continue

            # start로 시작하는 그룹 copies개를 한꺼번에 만든다.
            for num in range(start, start + 5):
                if count[num] < copies:
                    return False

                count[num] -= copies

        return True
```

## 헷갈린 지점: `sorted(count)`는 무엇을 정렬하나?

`Counter`는 딕셔너리처럼 **순회하면 키가 나온다.** 따라서 `sorted(count)`는 빈도가 아니라 **원소 값인 키**를 오름차순으로 정렬한 리스트를 반환한다.

```python
count = Counter({3: 2, 1: 4, 2: 1})

sorted(count)         # [1, 2, 3]
sorted(count.keys())  # [1, 2, 3] — 위와 같다.
sorted(count.values())  # [1, 2, 4] — 빈도만 정렬한다.

for start in sorted(count):
    copies = count[start]
    # start: 1, 2, 3
    # copies: 각각 4, 1, 2
```

이 문제에서는 **가장 작은 원소부터 처리**해야 하므로 키를 정렬한다. 빈도가 작은 순서로 처리하는 것이 아니다. `sorted(count)`는 정렬된 키 리스트를 새로 만들며, `count` 자체를 정렬하거나 빈도를 바꾸지는 않는다.

## 중복 처리 예시

```text
nums = [1,1,2,2,3,3,4,4,5,5]
count = {1: 2, 2: 2, 3: 2, 4: 2, 5: 2}

start = 1, copies = 2
1, 2, 3, 4, 5에서 각각 2개 차감
count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

이후 start = 2, 3, 4, 5는 빈도가 0이므로 건너뛴다.
결과: True
```

`set(nums)`로 바꾸면 중복 개수를 잃는다. 각 값이 존재하는지만 확인해서는 부족하고, **필요한 개수만큼 남아 있는지** 확인해야 한다.

## 왜 올바른가?

남은 최솟값 `start`의 모든 복사본은 서로 다른 그룹의 첫 원소여야 한다. 따라서 각각의 다음 네 값도 `copies`개씩 사용하는 것은 필수다. 하나라도 부족하면 어떤 방식으로 나누어도 성공할 수 없다.

개수가 충분하면 필수 그룹들을 제거하고 같은 논리를 남은 원소에 적용한다. 차감 전에 개수를 확인하므로 원소를 초과 사용하지 않는다. 끝까지 성공하면 각 키의 남은 개수는 자신의 처리 시점에 0이 되며, 모든 원소가 정확히 한 번 사용된다.

## 복잡도

`n`은 원소 수, `u`는 서로 다른 값의 수다.

- 시간: `O(n + u log u)`. 빈도 집계 `O(n)`, 키 정렬 `O(u log u)`, 키마다 최대 다섯 값 확인 `O(5u)`.
- 공간: `O(u)`. 빈도표와 정렬된 키 리스트를 저장한다.

## 기억할 것

- 길이가 5의 배수인 것은 필요조건일 뿐, 충분조건이 아니다.
- `sorted(count)`는 **키 정렬**, `count[start]`는 **그 키의 남은 빈도**다.
- `copies = count[start]`를 차감 전에 저장한다. 첫 차감으로 `count[start]`가 0이 되어도 나머지 네 값에서는 같은 `copies`를 빼야 한다.
- 존재하지 않는 키는 `Counter`에서 0으로 읽히므로 부족한 값도 같은 조건으로 검사할 수 있다.
- **기억할 한 문장: 남은 최솟값의 빈도만큼 그룹을 시작하고, 연속된 다섯 값의 빈도를 함께 차감한다.**

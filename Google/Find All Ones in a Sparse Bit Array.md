# Find All Ones in a Sparse Bit Array

- **Topic:** #binary-search #bisect-left
- **Updated:** Oct 14, 2026

## 문제

크기 `M`인 비트 배열을 직접 읽을 수 없다. DB API `query(L, R)`는 양 끝을 포함하는 구간에 `1`이 하나라도 있으면 `1`, 없으면 `0`을 반환한다. 모든 `1`의 인덱스를 반환하라.

예: `01100000001` → `[1, 2, 10]` (0-based).

조건: 적은 쿼리, 추가 공간 `O(1)`, 재귀 / 큐 / 별도 helper 함수 없이 구현.

## 면접에서 기억할 한 문장

**남은 구간에 1이 있는지 확인 → 이진 탐색으로 첫 1을 찾기 → 그 다음 인덱스부터 반복.**

```python
def find_ones(M):
    result = []
    start = 0

    # query는 DB가 제공하는 API. 남은 구간에 1이 없으면 종료.
    while start < M and query(start, M - 1):
        left, right = start, M - 1

        while left < right:
            mid = (left + right) // 2

            if query(start, mid):
                right = mid
            else:
                left = mid + 1

        result.append(left)
        start = left + 1

    return result
```

## bisect_left가 되는 이유

배열 자체는 정렬되어 있지 않아도, **`query(start, i)`의 결과는 False → True로 한 번만 바뀐다.** 한 번 1을 포함하면 더 긴 구간에도 반드시 1이 있다. 내부 탐색 중 `start`는 고정한다.

```text
index i:       0      1     2     3    ...   10
A[i]:          0      1     1     0    ...    1
query(0, i): False  True  True  True   ...  True
                    ↑ 첫 True = 첫 1의 위치
```

- **True → `right = mid`:** `mid`가 첫 True일 수 있으므로 후보로 남긴다.
- **False → `left = mid + 1`:** `start`부터 `mid`까지 전부 0이므로 모두 제외한다.
- 항상 첫 1이 `[left, right]` 안에 남고, 매번 구간이 줄어든다.

| left | right | mid | query(0, mid) | 이동 |
| --- | --- | --- | --- | --- |
| 0 | 10 | 5 | True | right = 5 |
| 0 | 5 | 2 | True | right = 2 |
| 0 | 2 | 1 | True | right = 1 |
| 0 | 1 | 0 | False | left = 1 |

## 왜 append(left)인가?

종료 시 **`left == right`**이다. 첫 1을 포함하는 구간을 계속 유지했으므로, 마지막으로 남은 그 위치가 첫 1이다. `right`를 append해도 같다.

그 다음에는 `start = left + 1`로 이동해야 같은 1을 다시 찾지 않는다.

## 복잡도 / 경계 주의

- `k`가 1의 개수일 때 쿼리 수와 시간: `O(k log M + 1)` (`M >= 2`). 충분히 희소할 때 sublinear이다.
- 추가 공간: **`O(1)`**, 반환 배열은 `O(k)`로 별도 계산한다.
- 모든 비트가 1이면 출력만으로도 `Ω(M)` 시간이 필요하므로 모든 입력에서 sublinear를 보장할 수는 없다.
- 여기서는 먼저 1이 존재함을 확인하므로 `right = M - 1`로 시작한다. 답이 배열 안에 반드시 있다.
- 일반적인 `bisect_left` 삽입 위치 검색은 답이 배열 끝 다음일 수도 있으므로 `right = len(nums)`를 사용한다.
- `right = mid - 1`은 정답 후보인 `mid`를 버릴 수 있고, `left = mid`는 두 칸이 남았을 때 무한 루프가 될 수 있다.

## 면접 직전 확인

**첫 True 찾기: True면 mid 유지, False면 mid까지 버림. 끝나면 left == right == 정답.**

# Router Reachability

- **Topic:** #dfs #backtracking #geometry
- **Updated:** Oct 15, 2026
- 인터뷰 문제를 정리한 것으로, 별도 LeetCode 번호와 입력 크기 제한은 제공되지 않았다.

## 문제

2차원 평면 위의 라우터 좌표 배열 `routers`가 주어진다. `routers[i] = [xi, yi]`는 라우터 `i`의 위치다. 출발 라우터 인덱스 `source`, 도착 라우터 인덱스 `destination`, 최대 이동 거리 `threshold`도 주어진다.

모든 라우터는 처음에 활성 상태다. 현재 라우터에서 다음 규칙에 따라 이동할 때, 목적지에 도달할 수 있으면 `True`, 불가능하면 `False`를 반환한다.

1. 현재 라우터를 제외하고 **활성 상태인 라우터 중 가장 가까운 라우터**를 찾는다.
2. 그 최소 거리가 `threshold` 이하일 때만 이동할 수 있다.
3. 최소 거리가 같은 라우터가 여러 개라면 그중 하나를 선택할 수 있다.
4. 이동하면서 떠난 라우터는 영구적으로 비활성화되어 같은 경로에서 다시 방문할 수 없다.
5. `source == destination`이면 이동 없이 `True`다.

거리는 유클리드 거리다. `threshold`는 음수가 아니며, 출발점과 도착점은 유효한 라우터 인덱스라고 가정한다.

> 원문에서 확인할 조건: 이 노트는 **매번 현재 활성 라우터를 기준으로 최근접 라우터를 다시 계산**하며, **동률이면 자유롭게 선택**한다고 가정한다. 처음 정해진 최근접 관계를 계속 사용하는 문제라면 풀이가 달라진다.

### 예시 1: 도달 가능

```text
routers = [[0,0], [2,0], [5,0], [9,0]]
source = 0
destination = 3
threshold = 4

0 → 1 → 2 → 3
거리: 2, 3, 4
결과: True
```

매번 아직 방문하지 않은 라우터 중 가장 가까운 곳으로 이동하며, 모든 이동 거리가 임계값 이하다.

### 예시 2: 거리 제한으로 실패

```text
routers = [[0,0], [2,0], [5,0], [10,0]]
source = 0
destination = 3
threshold = 4

0 → 1 → 2
결과: False
```

라우터 `2`에서 목적지까지의 거리는 `5`이므로 더 이상 이동할 수 없다. 이미 떠난 라우터로 돌아갈 수도 없다.

## 풀이: DFS + 백트래킹

`visited`에는 **현재 경로에서 방문한 라우터**를 저장한다. 이전 라우터들은 비활성 상태이고, 현재 라우터는 자기 자신으로 이동할 수 없으므로 다음 후보에서 모두 제외한다.

`dfs(current)`는 현재 라우터와 현재 `visited` 상태에서 목적지에 도달할 수 있는지 반환한다.

1. 현재 라우터가 목적지라면 `True`를 반환한다.
2. 방문하지 않은 모든 라우터를 확인하여 최소 거리와 동률 후보들을 구한다.
3. 최소 거리가 임계값을 넘거나 후보가 없으면 `False`를 반환한다.
4. 후보 하나를 `visited.add(nxt)`로 방문 처리한 뒤 재귀 탐색한다.
5. 재귀가 끝나면 `visited.remove(nxt)`로 상태를 복원한다.
6. 성공한 후보가 하나라도 있으면 `True`, 모두 실패하면 `False`다.

가장 가까운 라우터가 항상 하나라면 경로가 정해져 있으므로 단순 시뮬레이션으로 충분하다. **동률일 때 여러 선택을 탐색하기 위해 백트래킹을 사용한다.**

## 코드

비트마스크나 `frozenset` 없이 일반 `set`의 `add()`와 `remove()`를 사용한다. 이 버전은 메모이제이션을 사용하지 않는다.

```python
class Solution:
    def canReach(self, routers, source, destination, threshold):
        visited = {source}
        limit_squared = threshold * threshold

        def dfs(current):
            if current == destination:
                return True

            x, y = routers[current]
            nearest_distance = float("inf")
            candidates = []

            for nxt, (nx, ny) in enumerate(routers):
                if nxt in visited:
                    continue

                distance = (x - nx) ** 2 + (y - ny) ** 2

                if distance < nearest_distance:
                    nearest_distance = distance
                    candidates = [nxt]
                elif distance == nearest_distance:
                    candidates.append(nxt)

            if nearest_distance > limit_squared:
                return False

            for nxt in candidates:
                visited.add(nxt)
                reachable = dfs(nxt)
                visited.remove(nxt)

                if reachable:
                    return True

            return False

        return dfs(source)
```

### 거리의 제곱을 비교하는 이유

```python
distance = (x - nx) ** 2 + (y - ny) ** 2
limit_squared = threshold * threshold
```

제곱근은 음수가 아닌 값의 대소 관계를 유지하므로, 실제 거리 대신 거리의 제곱을 비교해도 최근접 라우터와 임계값 통과 여부는 같다. `distance`와 `nearest_distance`는 코드에서 **거리의 제곱**을 뜻한다.

## `add()` / `remove()`는 무엇을 의미하는가?

```python
visited.add(nxt)       # 현재 경로에서 이 라우터를 선택한다.
reachable = dfs(nxt)   # 이 선택 이후에 목적지까지 갈 수 있는지 확인한다.
visited.remove(nxt)    # 다른 선택을 탐색하기 위해 이전 상태로 복원한다.
```

`remove()`는 실제 이동 중에 비활성 라우터를 다시 활성화하는 동작이 아니다. **한 경로의 탐색을 마친 뒤, 다른 가상의 경로를 확인하기 위해 탐색 상태를 되돌리는 것**이다. 하나의 경로 안에서는 이미 방문한 라우터가 계속 `visited`에 있으므로 재방문할 수 없다.

성공 여부를 `reachable`에 저장하고 방문 상태를 복원한 다음 반환하면, 성공하거나 실패한 경우 모두 재귀 호출 전후의 상태가 동일하게 유지된다.

## 동률 예시 추적

```text
routers = [S(0,0), A(-1,0), B(1,0), D(1,1)]
source = 0
destination = 3
threshold = 1.5
```

`S`에서 `A`와 `B`까지는 모두 거리 `1`이므로 둘 다 후보가 된다.

```text
visited = {S}

1. A를 선택: visited = {S, A}
   A에서 가장 가까운 미방문 라우터는 B지만 거리 2 > 1.5.
   실패하고 A를 remove: visited = {S}

2. B를 선택: visited = {S, B}
   B에서 가장 가까운 미방문 라우터는 D이고 거리 1.
   D를 선택: visited = {S, B, D}
   목적지이므로 True.
```

`S`에서 `D`까지의 거리도 `sqrt(2)`로 임계값 이하지만, `A`와 `B`가 더 가까우므로 처음부터 `D`로 이동하는 것은 허용되지 않는다.

## 왜 정답을 찾는가?

각 호출은 현재 방문 상태에서 최소 거리인 미방문 라우터만 후보로 만든다. 따라서 탐색하는 모든 이동은 규칙을 만족한다. 방문 처리는 같은 경로에서 이전 라우터를 재사용하지 못하게 한다.

반대로, 유효한 경로의 다음 라우터는 반드시 이 최소 거리 후보 중 하나여야 한다. DFS는 모든 동률 후보를 탐색하므로 유효한 경로가 존재하면 그 경로도 탐색한다. 각 이동마다 방문한 라우터가 하나 늘어나므로 재귀는 유한한 깊이에서 종료한다.

## 복잡도

`n = len(routers)`라고 하자. 집합의 조회·추가·삭제는 평균 `O(1)`로 본다.

- **동률이 있는 일반적인 경우:** 여러 방문 순서를 탐색하므로 팩토리얼 규모까지 탐색이 커질 수 있다. 모든 방문 순서를 고려하는 보수적인 시간 상한은 **`O(n · n!)`**이다. 각 재귀 호출에서 다음 후보를 찾기 위해 `O(n)`을 순회한다. 실제 탐색량은 좌표와 최근접 조건에 따라 줄어든다.
- **추가 공간: `O(n²)` 상한.** 방문 집합과 재귀 깊이는 각각 `O(n)`이지만, 재귀 호출마다 저장하는 `candidates` 목록이 최대 `O(n)`이고 부모 호출의 목록도 남아 있다.
- **최근접 라우터가 매번 유일한 경우:** 최대 `n`개 라우터를 차례로 방문하므로 시간 **`O(n²)`**, 추가 공간 **`O(n)`**이다.

입력 크기 제한이 주어지지 않았으므로, 큰 입력에서도 이 백트래킹이 충분히 빠르다고 단정할 수는 없다.

## 헷갈린 지점 / 기억할 것

- **임계값 이내의 모든 라우터로 갈 수 있는 문제가 아니다.** 가장 가까운 미방문 라우터만 허용된다.
- 현재 상태의 최소 거리 후보들을 먼저 확정한다. 그 후보가 실패했다고 같은 상태에서 더 먼 라우터를 새 후보로 선택하면 규칙을 위반한다.
- 일반적인 그래프 탐색의 전역 방문 집합과 다르게, 여기서는 **현재 경로의 방문 집합**을 관리하고 탐색 후 복원한다.
- 같은 `current`라도 방문한 라우터가 다르면 다음 후보가 달라질 수 있다. 메모이제이션을 추가한다면 `current`만 키로 쓰면 안 된다.
- `visited.add(nxt)` → 재귀 → `visited.remove(nxt)` 순서를 기억한다. 비트마스크나 집합 합집합 연산 없이 상태를 관리할 수 있다.
- `source == destination`이면 바로 성공한다. 남은 라우터가 없으면 최소 거리가 `inf`로 유지되어 실패한다.
- 거리 비교는 `<= threshold`다. 코드에서는 최소 거리가 임계값보다 **클 때만** 실패 처리하므로 경계값을 포함한다.

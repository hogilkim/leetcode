# Lexicographically Smallest Closed Walk

- **Topic:** #graph #dfs #backtracking #bfs #greedy
- **Updated:** Oct 14, 2026
- 문제 번호와 입력 크기 제한은 제공되지 않았다.

## 문제

`n × m` 격자 `grid`와 음이 아닌 정수 `k`가 주어진다. `'x'`에서 출발하여 **정확히 `k`번 이동한 뒤 같은 출발점으로 돌아오는 경로** 중 사전순으로 가장 작은 문자열을 반환한다.

- `'.'`: 이동 가능한 칸.
- `'x'`: 출발점. 이동 가능한 칸이며 하나만 존재한다.
- `'#'`: 장애물. 이동할 수 없다.
- 한 번에 상하좌우 인접한 칸으로 이동하며, 격자 밖으로 나갈 수 없다.
- 같은 칸과 간선을 여러 번 방문해도 된다.
- 이동 문자는 `D`(아래), `L`(왼쪽), `R`(오른쪽), `U`(위)이며, 사전순은 **`D < L < R < U`**다.
- 가능한 경로가 없으면 이 노트에서는 `"IMPOSSIBLE"`을 반환한다. `k == 0`이면 빈 문자열을 반환한다.

최단 경로를 구하는 문제가 아니다. 경로 길이가 반드시 `k`여야 한다.

### 예시

```text
grid = [
    "...",
    ".x.",
    "..."
]
k = 4
결과: "DLRU"
```

아래 → 왼쪽 → 오른쪽 → 위로 이동하면 정확히 4번 만에 출발점으로 돌아온다. 가능한 길이 4의 경로 중 사전순으로 가장 작다.

| 입력 | k | 결과 | 이유 |
| --- | --- | --- | --- |
| `["x."]` | 2 | `"RL"` | 오른쪽으로 갔다가 왼쪽으로 돌아온다 |
| `["x."]` | 3 | `"IMPOSSIBLE"` | 홀수 번 이동해서 출발점으로 돌아올 수 없다 |
| `["x"]` | 2 | `"IMPOSSIBLE"` | 출발점에서 움직일 수 없다 |
| `["x"]` | 0 | `""` | 이동 없이 이미 출발점에 있다 |

## 브루트포스: 사전순 DFS + 백트래킹

현재 위치에서 `D → L → R → U` 순서로 모든 가능한 이동을 탐색한다. 정확히 `k`번 이동했을 때 출발점에 있으면 성공이다. 처음 발견한 성공 경로를 반환한다.

**이 접근은 올바르다.** 같은 길이의 문자열을 사전순으로 탐색하므로, 첫 성공 경로가 사전순 최소다. 다만 길이 `k`에 도달한 것만으로는 성공이 아니다. 출발점에 돌아왔는지도 확인해야 한다.

```python
def smallest_closed_walk_brute_force(grid: list[str], k: int) -> str:
    n, m = len(grid), len(grid[0])

    sr, sc = next(
        (r, c)
        for r in range(n)
        for c in range(m)
        if grid[r][c] == "x"
    )

    directions = [
        ("D", 1, 0),
        ("L", 0, -1),
        ("R", 0, 1),
        ("U", -1, 0),
    ]
    path = []

    def dfs(r, c, remaining):
        if remaining == 0:
            return r == sr and c == sc

        for char, dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < n
                and 0 <= nc < m
                and grid[nr][nc] != "#"
            ):
                path.append(char)

                if dfs(nr, nc, remaining - 1):
                    return True

                path.pop()

        return False

    if dfs(sr, sc, k):
        return "".join(path)

    return "IMPOSSIBLE"
```

실패한 분기는 `path.pop()`으로 되돌린다. 성공하면 `pop()`하지 않고 그대로 반환하므로 완성된 경로가 남는다. 재방문이 허용되므로 경로 탐색에 `visited`를 사용하지 않는다.

### 복잡도

- 시간: **`O(n × m + 4^k)`**라는 최악의 상한. 출발점을 찾는 데 `O(n × m)`, DFS는 매 단계 최대 4개 분기를 탐색한다.
- 공간: 입력을 제외하고 **`O(k)`**. 재귀 스택과 경로를 저장한다.
- 큰 `k`에서는 탐색량뿐 아니라 Python의 재귀 깊이 제한도 문제가 된다.

## 최적화: BFS 거리 + Greedy

DFS의 문제는 정답의 순서가 아니라 **실패할 경로를 너무 많이 탐색한다는 것**이다. 거리 배열을 사용하면 다음 이동을 하기 전에 남은 횟수 안에 출발점으로 돌아올 수 있는지 판단할 수 있다.

### 1. BFS로 출발점까지의 최단 거리 계산

`dist[r][c]`는 해당 칸에서 출발점까지 돌아가는 데 필요한 최소 이동 수다. 이동이 양방향이므로 출발점에서 BFS를 한 번 실행하면 이 거리를 모두 구할 수 있다. 장애물이나 도달 불가능한 칸은 `-1`이다.

### 2. 다음 이동 후 완주 가능한지 확인

후보 칸으로 이동한 뒤 남은 이동 수를 `remaining`, 그 칸의 거리를 `distance`라고 하면 다음 조건을 확인한다.

```python
distance != -1
distance <= remaining
(remaining - distance) % 2 == 0
```

- `distance <= remaining`: 출발점까지 돌아갈 시간이 충분하다.
- 차이가 짝수: 최단 경로보다 남는 이동은 인접한 칸으로 갔다가 돌아오는 **2번 이동**으로 소비할 수 있다.

격자를 체스판처럼 색칠하면 매 이동마다 색이 바뀐다. 같은 칸으로 돌아오려면 총 이동 수가 짝수여야 하며, 현재 칸에서 출발점으로 가는 모든 경로의 길이는 같은 홀짝을 갖는다. 따라서 거리뿐 아니라 홀짝도 맞아야 한다.

왕복하려면 사용할 간선이 있어야 한다. 아래 코드는 후보 이동이 실제로 가능한지 먼저 확인하므로 방금 사용한 간선으로 왕복할 수 있다. 출발점이 고립되어 있고 `k > 0`이면 후보를 하나도 찾지 못해 실패한다.

### 3. 사전순으로 가능한 첫 이동 선택

매 단계 `D → L → R → U` 순서로 후보를 확인하고, 위 조건을 만족하는 첫 이동을 확정한다. 그 이동 뒤에 유효한 완성 경로가 존재하므로 백트래킹할 필요가 없다.

```python
from collections import deque


def smallest_closed_walk(grid: list[str], k: int) -> str:
    n, m = len(grid), len(grid[0])

    if k % 2:
        return "IMPOSSIBLE"

    sr, sc = next(
        (r, c)
        for r in range(n)
        for c in range(m)
        if grid[r][c] == "x"
    )

    directions = [
        ("D", 1, 0),
        ("L", 0, -1),
        ("R", 0, 1),
        ("U", -1, 0),
    ]

    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    queue = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()

        for _, dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < n
                and 0 <= nc < m
                and grid[nr][nc] != "#"
                and dist[nr][nc] == -1
            ):
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    r, c = sr, sc
    path = []

    for step in range(k):
        remaining = k - step - 1
        found = False

        for char, dr, dc in directions:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            distance = dist[nr][nc]

            if (
                distance != -1
                and distance <= remaining
                and (remaining - distance) % 2 == 0
            ):
                path.append(char)
                r, c = nr, nc
                found = True
                break

        if not found:
            return "IMPOSSIBLE"

    return "".join(path)
```

`for ... else`는 사용하지 않는다. `found`로 유효한 이동을 찾았는지 표시하고, 네 방향을 확인한 뒤 `if not found`로 실패를 처리한다.

### 왜 사전순 최소인가?

각 단계에서 완주 가능한 후보 중 가장 작은 문자를 고른다. 다른 유효한 경로와 처음 달라지는 위치에서 그 경로가 더 작은 문자를 선택할 수는 없다. 그런 후보가 있었다면 Greedy가 먼저 선택했을 것이기 때문이다.

마지막 이동 후에는 `remaining == 0`이므로 선택한 칸의 거리가 반드시 0이다. 즉, 정확히 `k`번 이동한 뒤 출발점에 도착한다.

### 복잡도

- 시간: **`O(n × m + k)`**. BFS는 각 칸을 최대 한 번 방문하고, 경로 생성은 `k`번 반복하며 매번 최대 네 방향을 확인한다.
- 공간: 출력 포함 **`O(n × m + k)`**. 거리 배열과 BFS 큐는 `O(n × m)`, 경로는 `O(k)`다.

## 헷갈린 지점 / 기억할 것

- **사전순 DFS로 첫 정답을 찾는 접근은 맞다.** 거리 배열은 정답 순서를 위한 것이 아니라 실패할 분기를 빠르게 제외하기 위한 것이다.
- 사전순으로 이동을 시도하는 것만으로 백트래킹 없이 선택해도 되는 것은 아니다. Greedy는 선택 후 완주 가능성을 확인해야 한다.
- `remaining = k - step - 1`: 후보 이동 한 번을 이미 사용한 뒤의 남은 횟수다.
- 홀수 `k`는 불가능하다. 짝수라고 무조건 가능한 것은 아니다. 고립된 출발점에서는 양수 `k`가 불가능하다.
- BFS에서는 중복 방문을 막지만, 실제 경로에서는 같은 칸을 여러 번 방문할 수 있다.
- **기억할 한 문장: DFS는 사전순으로 정답을 찾고, BFS 거리 + Greedy는 완주 가능한 최소 문자를 매 단계 바로 확정한다.**

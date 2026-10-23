# Nearest Favorite City

- **Topic:** #graph #shortestpath #dijkstra #heap
- **Updated:** Oct 15, 2026
- 인터뷰 문제를 LeetCode 스타일로 정리한 것으로, 별도 문제 번호와 입력 크기 제한은 제공되지 않았다.

## 문제 (LeetCode style)

You are given `n` cities labeled from `0` to `n - 1` and an array `roads`, where `roads[i] = [u, v, time]` represents a bidirectional road between cities `u` and `v` that takes `time` minutes to travel.

You are also given an array `favorites` containing your favorite cities and an integer `source` representing your starting city.

Return **the favorite city that can be reached from `source` in the minimum total travel time**. You may travel through other cities along the way.

If multiple favorite cities tie, return the one with the smallest label. If no favorite city is reachable, return `-1`.

> 정리할 때 추가한 가정: 도로는 양방향이고 이동 시간은 양수다. 동률이면 번호가 작은 도시를 반환하며, 도달할 수 없으면 `-1`을 반환한다. 원문에는 이 조건들이 명시되지 않았으므로 인터뷰에서는 확인한다. `source`가 favorite이면 이동 시간은 `0`이다.

### Example 1

```text
Input:
n = 5
roads = [[0,1,4], [0,2,1], [2,1,2], [1,3,1], [2,4,6]]
favorites = [3,4]
source = 0

Output: 3
```

- 도시 `3`: `0 → 2 → 1 → 3`, 총 시간 `1 + 2 + 1 = 4`.
- 도시 `4`: `0 → 2 → 4`, 총 시간 `1 + 6 = 7`.
- 최단 이동 시간이 더 작은 favorite 도시 `3`을 반환한다.

### Example 2

```text
Input:
n = 4
roads = [[0,1,3], [2,3,2]]
favorites = [2,3]
source = 0

Output: -1
```

도시 `0`에서 두 favorite 도시 모두 도달할 수 없다.

## 풀이: Dijkstra + 최소 힙

간선마다 시간이 다르므로, 이동한 도로 개수가 아니라 **누적 이동 시간**이 가장 작은 도시부터 탐색한다.

1. 양방향 인접 리스트를 만들고, favorite 목록은 조회가 빠른 `set`으로 바꾼다.
2. `dist[city]`는 현재까지 찾은 최소 이동 시간이다. 출발점만 `0`, 나머지는 무한대로 초기화한다.
3. 최소 힙에 `(누적 시간, 도시 번호)`를 넣고 가장 작은 항목부터 꺼낸다.
4. 꺼낸 시간이 `dist[city]`보다 크면 이미 더 좋은 경로가 발견된 오래된 항목이므로 건너뛴다.
5. 현재 도시가 favorite이면 즉시 반환한다.
6. 이웃으로 가는 시간이 기존 `dist`보다 작을 때만 갱신하고 힙에 넣는다.
7. 힙이 빌 때까지 favorite을 찾지 못하면 `-1`을 반환한다.

## 코드

```python
from typing import List
import heapq


class Solution:
    def nearestFavoriteCity(
        self,
        n: int,
        roads: List[List[int]],
        favorites: List[int],
        source: int,
    ) -> int:
        graph = [[] for _ in range(n)]

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        favorite_set = set(favorites)
        dist = [float("inf")] * n
        dist[source] = 0
        heap = [(0, source)]

        while heap:
            time, city = heapq.heappop(heap)

            if time > dist[city]:
                continue

            if city in favorite_set:
                return city

            for neighbor, travel_time in graph[city]:
                new_time = time + travel_time

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        return -1
```

## 왜 정답인가?

이동 시간이 양수이므로, 최소 힙에서 오래된 항목을 제외하고 꺼낸 도시의 최단 시간은 확정된다. 더 짧은 경로가 있다면 그 경로의 앞선 도시가 먼저 처리되어 이미 거리를 갱신했어야 하기 때문이다. 따라서 **처음 꺼낸 favorite이 최소 시간에 도달할 수 있는 favorite**이다.

같은 최단 시간을 갖는 도시들은 그보다 시간이 작은 이전 도시를 통해 이미 힙에 들어가 있다. Python의 튜플 비교는 시간이 같으면 도시 번호를 비교하므로 동률일 때 작은 번호가 먼저 나온다. 이 조기 반환의 동률 처리는 **양수 가중치** 가정에 의존한다.

예시 1의 유효한 pop 순서는 다음과 같다. 이는 탐색 순서이며, 하나의 이동 경로를 뜻하지 않는다.

```text
(0, 0) → (1, 2) → (3, 1) → (4, 3)
                                       ↑ favorite이므로 3 반환
```

## 복잡도

`N`은 도시 수, `M`은 도로 수다. favorite 목록에는 중복이 없다고 가정한다.

- **시간:** 일반적인 단순 그래프에서 `O((N + M) log N)`. 오래된 항목을 남기는 이 힙 구현은 평행 간선까지 허용하면 `O(N + M log(M + 1))`로 표현할 수 있다.
- **공간:** 인접 리스트, 거리 배열, favorite 집합, 힙을 포함해 `O(N + M)`.

## 기억할 것

- favorite을 **힙에 넣을 때** 반환하면 안 된다. 처음 발견한 경로보다 더 짧은 경로가 나중에 발견될 수 있다. 오래된 항목을 건너뛴 뒤 **pop할 때** 판단한다.
- 일반 BFS는 도로마다 시간이 같을 때 적합하다. 이 문제에서는 Dijkstra를 사용한다.
- `new_time < dist[neighbor]`일 때만 갱신하고, `time > dist[city]`인 항목은 건너뛴다.
- `source`가 favorite이면 `0`분이므로 출발 도시를 반환한다. favorite이 비었거나 모두 도달 불가능하면 `-1`이다.
- 이동 시간이 `0`인 도로까지 허용하면서 작은 번호 우선 규칙을 유지한다면, 첫 favorite에서 즉시 반환하는 동률 처리는 수정해야 한다. 최소 favorite 시간과 같은 거리의 후보를 모두 처리하고 번호를 비교한다.
- [743. Network Delay Time](../오답노트/743.%20Network%20Delay%20Time.md)은 모든 도시의 최단 시간 중 최댓값을 구한다. 여기서는 favorite 중 최솟값을 구하므로 조기에 종료할 수 있다.

# Oct 6, 2026 743
from collections import deque, defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        neighbors = [None] * (n + 1)

        distance_map = defaultdict(list)
        for time in times:
            source, dest, distance = time
            distance_map[source].append((dest, distance))

        dist_list = [float("inf")] * (n + 1)
        dist_list[k] = 0

        queue = deque([(k, 0)])

        while queue:
            source, currdis = queue.popleft()
            for nxt, nxtdis in distance_map[source]:
                if currdis + nxtdis < dist_list[nxt]:
                    queue.append((nxt, currdis + nxtdis))
                    dist_list[nxt] = currdis + nxtdis

        maxdis = 0
        for num in dist_list[1:]:
            if num == float("inf"):
                return -1
            maxdis = max(maxdis, num)

        return maxdis

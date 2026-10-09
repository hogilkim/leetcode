# Oct 9, 2026 1102
import heapq


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        minval = grid[0][0]

        max_heap = []
        heapq.heapify(max_heap)
        heapq.heappush(max_heap, (-grid[0][0], 0, 0))

        while max_heap:
            val, r, c = heapq.heappop(max_heap)
            minval = min(minval, -val)
            if r == ROW - 1 and c == COL - 1:
                break
            for rdir, cdir in DIR:
                nr, nc = r + rdir, c + cdir
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(max_heap, (-grid[nr][nc], nr, nc))
        return minval

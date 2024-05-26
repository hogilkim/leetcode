# LC HARD
# Solve again
import collections, heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        LEN = len(grid)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # build theif minimum distance matrix
        visited = set()
        min_dis_matrix = [[0] * LEN for _ in range(LEN)]
        bfs = collections.deque([])

        for r in range(LEN):
            for c in range(LEN):
                if grid[r][c] == 1:
                    bfs.append((r, c, 0))
                    visited.add((r, c))

        while bfs:
            r, c, dis = bfs.popleft()
            min_dis_matrix[r][c] = dis
            for rdir, cdir in dirs:
                nr, nc = r + rdir, c + cdir
                if 0 <= nr < LEN and 0 <= nc < LEN and (nr, nc) not in visited:
                    bfs.append((nr, nc, dis + 1))
                    visited.add((nr, nc))

        # find the path
        visited = set()
        max_heap = [(-min_dis_matrix[0][0], 0, 0)]
        visited.add((0, 0))
        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = -dist
            if (r, c) == (LEN - 1, LEN - 1): return dist

            for rd, cd in dirs:
                nr, nc = r + rd, c + cd
                if 0 <= nr < LEN and 0 <= nc < LEN and (nr, nc) not in visited:
                    heapq.heappush(max_heap, (-min(dist, min_dis_matrix[nr][nc]), nr, nc))
                    visited.add((nr, nc))

        return 0
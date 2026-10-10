# Oct 9, 2026 1254
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        ROW, COL = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):

            res = 0 < r < ROW - 1 and 0 < c < COL - 1

            for rdir, cdir in DIRS:
                nr, nc = r + rdir, c + cdir
                if (
                    0 <= nr < ROW
                    and 0 <= nc < COL
                    and grid[nr][nc] == 0
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    closed_result = dfs(nr, nc)
                    res = res and closed_result
            return res

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0 and (row, col) not in visited:
                    visited.add((row, col))
                    if dfs(row, col):
                        count += 1
        return count

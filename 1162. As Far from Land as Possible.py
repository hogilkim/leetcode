from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0), (0,-1)]
        dq = deque([(r,c) for c in range(COL) for r in range(ROW) if grid[r][c]])
        maxdis = 0

        while dq:
            r, c = dq.popleft()

            for rd, cd in directions:
                nr, nc = r+rd, c+cd
                if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc] == 0:
                    dq.append((nr,nc))
                    grid[nr][nc] = grid[r][c] + 1
            
                    maxdis = max(maxdis, grid[nr][nc])



        return maxdis - 1

        
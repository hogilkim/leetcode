class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        ROW, COL = len(grid), len(grid[0])
        
        def dfs(r, c):
            res = 0
            val = grid[r][c]
            grid[r][c] = 0
            for rd, cd in directions:
                nr, nc = r+rd, c+cd
                if 0<=nr<ROW and 0<=nc<COL and (nr,nc) not in path and grid[nr][nc]:
                    res = max(dfs(nr, nc), res)
                    
            grid[r][c] = val
            return res + val
        
        maxval = 0
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]: maxval = max(dfs(r,c),maxval)
        
        return maxval
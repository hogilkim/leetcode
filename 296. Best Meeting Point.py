class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        rows = [row for row in range(ROW) for col in range(COL) if grid[row][col]]
        cols = [col for col in range(COL) for row in range(ROW) if grid[row][col]]
        
        midr = rows[len(rows)//2]
        midc = cols[len(cols)//2]
        
        return sum(abs(r-midr) for r in rows) + sum(abs(c-midc) for c in cols)
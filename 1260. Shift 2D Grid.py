class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        ROW, COL = len(grid), len(grid[0])
        for _ in range(k):
            popped = grid[-1].pop()
            
            grid[0] = [popped] + grid[0]
            for i in range(ROW-1):
                pop = grid[i].pop()
                grid[i+1] = [pop] + grid[i+1]
        
        return grid
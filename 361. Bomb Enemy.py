class Solution:
    def left_to_right(self, grid, dp, fixed_row):
        ROW, COL = len(grid), len(grid[0])
        enemies = 0
        
        for col in range(COL):
            if grid[fixed_row][col] == "E": enemies += 1
            elif grid[fixed_row][col] == "W": enemies = 0
            else: dp[fixed_row][col] += enemies
        
    
    def right_to_left(self, grid, dp, fixed_row):
        ROW, COL = len(grid), len(grid[0])
        enemies = 0
        
        for col in range(COL-1,-1,-1):
            if grid[fixed_row][col] == "E": enemies += 1
            elif grid[fixed_row][col] == "W": enemies = 0
            else: dp[fixed_row][col] += enemies
    
    def bot_to_top(self, grid, dp, fixed_col):
        ROW, COL = len(grid), len(grid[0])
        enemies = 0
        
        for row in range(ROW):
            if grid[row][fixed_col] == "E": enemies += 1
            elif grid[row][fixed_col] == "W": enemies = 0
            else: dp[row][fixed_col] += enemies
    
    def top_to_bot(self, grid, dp, fixed_col): 
        enemies = 0
        ROW, COL = len(grid), len(grid[0])
        
        for row in range(ROW-1,-1,-1):
            if grid[row][fixed_col] == "E": enemies += 1
            elif grid[row][fixed_col] == "W": enemies = 0
            else: dp[row][fixed_col] += enemies
                
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        ROW, COL = len(grid), len(grid[0])
        dp = [[0]*COL for _ in range(ROW)]
        
        for r in range(ROW):
            self.left_to_right(grid, dp, r)
            self.right_to_left(grid, dp, r)
        for c in range(COL):
            self.top_to_bot(grid, dp, c)
            self.bot_to_top(grid, dp, c)
        return max( max(dp[i]) for i in range(ROW) )
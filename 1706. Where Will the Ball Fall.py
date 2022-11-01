class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        direction = {
            1:(1,1),-1:(1,-1)
        }
        
        ROW, COL = len(grid), len(grid[0])
        
        res = []
        
        for ball_col in range(COL):
            ball_c = ball_col
            ball_r = 0
            
            while ball_r < ROW:
                grid_dir = direction[grid[ball_r][ball_c]]
                
                side_grid_col = ball_c + grid_dir[1]
                # out of wall
                if side_grid_col < 0 or side_grid_col == COL: break
                # V shape
                if grid[ball_r][side_grid_col] == -grid_dir[1]: break
                
                ball_r += 1
                ball_c += grid_dir[1]
            
            if ball_r == ROW: res.append(ball_c)
            else: res.append(-1)
        
        return res
                    
                
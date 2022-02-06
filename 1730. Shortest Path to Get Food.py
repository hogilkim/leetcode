
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        start_row = start_col = 0
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "*":
                    start_row = row
                    start_col = col
                    break
                    
        
        directions = [(1,0), (0,1), (-1,0),(0,-1)]
        
        queue = [(start_row, start_col)]
        
        min_step = 0
        
        while queue:
            min_step += 1
            next_queue = []
            for row, col in queue:
                
                                
                for row_dir, col_dir in directions:
                    new_row, new_col = row+row_dir, col+col_dir
                    if 0<=new_row<ROW and 0<=new_col<COL:
                        
                        if grid[new_row][new_col]=="#": return min_step
                        
                        elif grid[new_row][new_col] == "O":
                            next_queue.append((new_row, new_col))
                            grid[new_row][new_col] = "X"
            queue = next_queue
            
        return -1
            
# dfs - time limit exceeded
#         min_step = float('inf')
#         visited = set()
#         ROW, COL = len(grid), len(grid[0])
        
#         directions = [[1,0], [0,1], [-1,0],[0,-1]]
        
#         def dfs(row, col, step):
#             if row >= ROW or row < 0  or col>= COL or col < 0 or grid[row][col] == "X" or (row,col)\
#             in visited:
#                 return
            
#             nonlocal min_step
            
#             if grid[row][col] == "#": min_step = min(min_step, step)
            
#             visited.add((row,col))
            
#             for row_dir, col_dir in directions:
#                 dfs(row+row_dir, col + col_dir, step+1)
            
#             visited.remove((row,col))
        
#         start_row = start_col = 0
        
#         for row in range(ROW):
#             for col in range(COL):
#                 if grid[row][col] == "*":
#                     start_row = row
#                     start_col = col
#                     break
        
#         dfs(start_row, start_col, 0)
        
        
#         return min_step if min_step < float('inf') else -1
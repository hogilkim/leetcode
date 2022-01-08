# Jan 8  second attempt - solve again 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      # Neetcode's method 
        ROW, COL = len(heights), len(heights[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        result = []
        pacific, atlantic = set(), set()
        
        def dfs(row,col,reachable, prev_height):
            if (row, col) in reachable or row < 0 or col < 0 or row >= ROW or col >= COL or prev_height > heights[row][col]:
                return
            
            reachable.add((row,col))
            
            for row_dir, col_dir in directions:
                dfs(row+row_dir, col+col_dir, reachable, heights[row][col])
                
                
        for row in range(ROW):
            # pacific
            dfs(row, 0, pacific, heights[row][0])
            # atlantic
            dfs(row, COL-1, atlantic, heights[row][COL-1])
        
        for col in range(COL):
            #pacific
            dfs(0 , col, pacific, heights[0][col] )
            #atlantic
            dfs(ROW-1, col, atlantic, heights[ROW-1][col] )
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in atlantic and (r,c) in pacific:
                    result.append([r,c])
        return result
    
        
        
        # maximum recursion depth exceeded in comparison
#         ROW, COL = len(heights), len(heights[0])
        
#         directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
#         result = []
        
#         #[pacific, atlantic]
        
#         def dfs(prev_height, row, col):
#             if prev_height < heights[row][col] :
#                 return [False, False]
#             # pacific
#             if row < 0 or col<0: 
#                 return [True, False]
#             # atlantic
#             elif row>=ROW or col>=COL:
#                 return [False, True]
            
#             result = [False,False]
            
#             for row_dir, col_dir in directions:
#                 return_val = dfs(heights[row][col], row+row_dir, col+col_dir)
#                 result = [ result[0] or return_val[0], result[1] or return_val[1] ]
            
#             return result
        
#         for row in range(ROW):
#             for col in range(COL):
#                 return_val = dfs(heights[row][col], row, col)
#                 if return_val[0] and return_val[1]:
#                     result.append([row,col])
        
#         return result

# -------------------------------------------------------------------------------------------
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pacific, atlantic = set(), set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r, c, reachable, prev_height):
            if (r,c) in reachable or r < 0 or c < 0 or c >= COLS or r >= ROWS or prev_height > heights[r][c]:
                return
            
            reachable.add((r,c))
            for r_dir, c_dir in directions:
                dfs(r+r_dir, c+c_dir, reachable, heights[r][c])
            
        
        for c in range(COLS):
            # pacific row
            dfs(0,c,pacific,heights[0][c])
            # atlantic row
            dfs(ROWS-1,c, atlantic, heights[ROWS-1][c])
            
        for r in range(ROWS):
            # pacific col
            dfs(r, 0, pacific, heights[r][0])
            # atlantic col
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
            
        
        result = []
        for c in range(COLS):
            for r in range(ROWS):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
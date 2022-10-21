# Third attempt - solved ! Oct 21, 2022 

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROW, COL = len(matrix), len(matrix[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        memo = {} # key: (r,c) value: max lip
        
        def dfs(r,c):
            if (r,c) in memo: return memo[(r,c)]
            
            max_lip = 0
        
            # for loop through the direction
            for rd, cd in directions:
                # not out of index and next one not in memo
                nr, nc = r+rd, c+cd
                if 0<=nr<ROW and 0<=nc<COL and matrix[r][c] < matrix[nr][nc]:
                    max_lip = max(dfs(nr,nc), max_lip)
                    
            
            # store (r,c) = max value of lip
            memo[(r,c)] = max_lip + 1
            
            # return max value of lip
            return max_lip+1
        
        
        max_lip_res = 0
        
        for r in range(ROW):
            for c in range(COL):
                max_lip_res = max(dfs(r,c), max_lip_res)
        
        return max_lip_res
        

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dynamic programming approach
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        dp = {}
        
        def dfs(x,y, prev):
            if ((x < 0) or (x >= len(matrix)) or (y < 0) or (y >= len(matrix[x])) 
            or (prev >= matrix[x][y])):
                return 0
            
            if (x,y) in dp:
                return dp[(x,y)]
            
            max_length = 1
            for dir_x, dir_y in directions:
                max_length = max(1+dfs(x+dir_x, y+dir_y, matrix[x][y]), max_length)
            
            dp[(x,y)] = max_length
            return max_length
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                dfs(x,y, -1)
                
        return max(dp.values())
        
        
        
        
        # timeout, but correct approach
#         path = set()
#         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
#         def dfs(x,y, prev, path_num):
#             if ((x < 0) or (x >= len(matrix)) or (y < 0) or (y >= len(matrix[x])) 
#             or (prev >= matrix[x][y]) or ((x,y) in path)):
#                 return path_num
            
#             max_length = path_num + 1
#             path.add((x,y))
#             for dir_x, dir_y in directions:
#                 max_length = max(dfs(x+dir_x, y+dir_y, matrix[x][y], path_num + 1), max_length)
            
#             path.remove((x,y))
#             return max_length
        
#         max_path = 0
#         for x in range(len(matrix)):
#             for y in range(len(matrix[0])):
#                 max_path = max(max_path, dfs(x,y, -1, 0))
#         return max_path
# Dec 17, 2023 79-3
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        path = set()

        # dfs
        def dfs(idx, row, col):
            if board[row][col] != word[idx]: return False
            if idx == len(word)-1: return True
            path.add((row, col))

            for rdir, cdir in dirs:
                nr, nc = row + rdir, col + cdir
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in path:
                    if dfs(idx+1, nr, nc): return True

            path.remove((row, col))

            return False
        

        for r in range(ROW):
            for c in range(COL):
                if dfs(0, r, c): return True
        
        return False

# Second time solved Dec 29, 2021
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()
        def dfs(row, col, i):
            
            if (row >= ROW or col >= COL or row < 0 or col < 0 or (row,col) in visited or word[i] != board[row][col]):
                return False
            visited.add((row,col))
            if i == len(word)-1:
                return True
            
            ret_val = dfs(row+1, col, i+1) or dfs(row, col+1, i+1) or dfs(row-1,col,i+1) or dfs(row, col-1, i+1)
            
            visited.remove((row,col))
            return ret_val
        
        for row in range(ROW):
            for col in range(COL):
                if dfs(row, col, 0): return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Better Solution
        
        ROW, COL = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, i):
            if i == len(word): return True
            if row >= ROW or col >= COL or row < 0 or col < 0 or (row, col) in visited or board[row][col]!=word[i]:
                return False
            
            visited.add((row, col))
            
            ans = dfs(row+1, col, i + 1) or dfs(row, col+1, i + 1) or dfs(row-1, col, i + 1) or dfs(row, col-1, i + 1)
            
            visited.remove((row, col))
        
            return ans
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): return True
        return False
    
        # My Solution
#         visited = set()
#         directions = [[1,0],[0,1],[-1,0],[0,-1]]
#         def dfs(row, col,sub_word):
#             if (row,col) in visited:
#                 return False
            
#             visited.add((row, col))
#             # print(visited)
#             if len(sub_word) == 0 or (len(sub_word) == 1 and sub_word[0] == board[row][col]):
#                 visited.remove((row,col))
#                 return True
#             if board[row][col] != sub_word[0]:
#                 visited.remove((row,col))
#                 return False
#             for row_dir, col_dir in directions:
#                 if row+row_dir <= len(board)-1 and col+col_dir <= len(board[0])-1 and row+row_dir >=0 and col+col_dir>=0:
#                     if dfs(row+row_dir, col+col_dir, sub_word[1:]):
#                         return True
            
#             visited.remove((row,col))
#             return False
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i,j,word): return True
#                 visited = set()
        
#         return False
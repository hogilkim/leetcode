import collections
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board: return []
        
        i, j = click[0], click[1]
        
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
    
        self.dfs(board, i, j)
        return board
    
    def dfs(self, board, r, c):
        if board[r][c] != "E": return
        
        ROW, COL = len(board), len(board[0])
        mines = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        for r_dir, c_dir in directions:
            row = r+r_dir
            col = c+c_dir
            if 0<=row<ROW and 0<=col<COL and board[row][col] == "M":
                mines += 1
        
        if mines:
            board[r][c] = str(mines)
            return
        else:
            board[r][c] = "B"
        
        
        for r_dir, c_dir in directions:
            row = r+r_dir
            col = c+c_dir
            if 0<=row<ROW and 0<=col<COL:
                self.dfs(board, row, col)        
        
    
#         bfs_queue = collections.deque([(click[0], click[1])])
        
#         if board[click[0]][click[1]] == "M":
#             board[click[0]][click[1]] = "X"
#             return board
        
#         directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
#         added = set()
#         added.add((click[0], click[1]))
        
#         while bfs_queue:
#             r, c = bfs_queue.popleft()
#             bombs = 0
#             for r_dir, c_dir in directions:
#                 if 0<= r+r_dir < len(board) and 0<=c+c_dir<len(board[0]) and board[r+r_dir][c+c_dir] == "M":
#                     bombs += 1
#                     # elif board[r+r_dir][c+c_dir] == "E" and (r+r_dir, c+c_dir) not in added:
#                     #     bfs_queue.append((r+r_dir, c+c_dir))
#                     #     added.add((r+r_dir, c+c_dir))

#             if bombs:
#                 board[r][c] = str(bombs)
#             else:
#                 board[r][c] = "B"
#                 for r_dir, c_dir in directions:
#                     if 0<= r+r_dir < len(board) and 0<=c+c_dir<len(board[0]) and board[r+r_dir][c+c_dir] == "E" and (r+r_dir, c+c_dir) not in added:
#                         bfs_queue.append((r+r_dir, c+c_dir))
#         return board
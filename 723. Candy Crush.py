# solve again
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(board), len(board[0])
        
        def drop():
            
            for col in range(COL):
                dropping_idx = ROW - 1
                for i in reversed(range(ROW)):
                    if board[i][col]: 
                        board[dropping_idx][col] = board[i][col]
                        dropping_idx -= 1
                for row in range(dropping_idx+1):
                    board[row][col] = 0
        
        
        while True:
            crush = set()
            for row in range(ROW):
                for col in range(COL):
                    if col > 1 and board[row][col] and board[row][col] == board[row][col-1] == board[row][col-2]:
                        crush.update({(row,col), (row, col-1), (row,col-2)})
                    if row > 1 and board[row][col] and board[row][col] == board[row-1][col] == board[row-2][col]:
                        crush.update({(row,col), (row-1, col), (row-2, col)})
                        
            if not crush: break
                
            for row, col in crush:
                board[row][col] = 0
                
            drop()
        
        return board
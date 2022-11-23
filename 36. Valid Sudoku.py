class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = len(board), len(board[0])
        
        # check each col
        for r in range(ROW):
            check = [0]*10
            for c in range(COL):
                if board[r][c].isdigit():
                    if check[int(board[r][c])]: return False
                    check[int(board[r][c])] += 1
        
        # check each row
        for c in range(COL):
            check = [0]*10
            for r in range(ROW):
                if board[r][c].isdigit():
                    if check[int(board[r][c])]: return False
                    check[int(board[r][c])] += 1
        
        
        for row in range(3):
            for col in range(3):
                start_r = row*3
                start_c = col*3
                
                check = [0]*10
                for r in range(start_r, start_r+3):
                    for c in range(start_c, start_c+3):
                        if board[r][c].isdigit():
                            if check[int(board[r][c])]: return False
                            check[int(board[r][c])] += 1
        
        return True
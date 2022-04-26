class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        
        nei_dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]
        
        def check(r,c):
            
            nei_num = 0
            for r_d, c_d in nei_dir:
                if (0<=r_d+r<ROW and 0<=c_d+c<COL) and abs(board[r_d+r][c_d+c])==1:
                    nei_num += 1
            if board[r][c] == 1: 
                # case 1
                if nei_num < 2 or nei_num>3:
                    board[r][c]= -1
            else:
                if nei_num ==3:
                    board[r][c]= 2
        
        for r in range(ROW):
            for c in range(COL):
                check(r,c)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c]==2: board[r][c]=1
                elif board[r][c]==-1: board[r][c]=0
        
        
        return board
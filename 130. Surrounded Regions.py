class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        
        visited = set()
        O = "O"
        X = "X"
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def dfs(r,c):
            
            
            not_on_border = 0<r<ROW-1 and 0<c<COL-1
            
            for rd, cd in directions:
                nr, nc = r+rd, c+cd
                
                if 0<=nr<ROW and 0<=nc<COL and board[nr][nc] == O and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    not_on_border = dfs(nr,nc) and not_on_border
                    
            
            region.add((r,c))
            return not_on_border
        
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == O and (row,col) not in visited:
                    region = set()
                    
                    if dfs(row,col):
                        for r,c in region:
                            board[r][c] = X
                    
            
            
            
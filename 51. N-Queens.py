class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [ ["."]*n for _ in range(n) ]
        
        def backtracking(r):
            if r == n:
                res.append( ["".join(row) for row in board ].copy() )
            
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                board[r][c] = 'Q'
                backtracking(r+1)
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
                board[r][c] = '.'
        backtracking(0)
        return res
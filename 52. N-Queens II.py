class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        
        pos_diag = set()
        neg_diag = set()
        cols = set()
        
        def backtracking(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                backtracking(r+1)
                
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
            
        backtracking(0)
        return res
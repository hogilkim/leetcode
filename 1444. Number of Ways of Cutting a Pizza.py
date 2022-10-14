class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        ROW, COL = len(pizza), len(pizza[0])
        MOD = 10**9+7
        
        # making preSum dp
        preSumdp = [[0]*(COL+1) for _ in range(ROW+1)]
        
        for i in range(ROW-1, -1, -1):
            for j in range(COL-1, -1, -1):
                preSumdp[i][j] = preSumdp[i][j+1] + preSumdp[i+1][j] - preSumdp[i+1][j+1] + int(pizza[i][j] == "A")
                
                
                #####
                
        # memo
        memo = {}
        def backtracking(r,c,k):
            if preSumdp[r][c] == 0: return 0
            if k == 0: return 1
            if (r,c,k) in memo: return memo[(r,c,k)]
                
                
            total_cutting = 0
            
            # for loop i  r+1 - end:
                # if preSum[r][c] - preSum[i][c] > 0 
                    # call backtracking(i, c, k-1)
            for row in range(r+1, ROW):
                if preSumdp[r][c] - preSumdp[row][c] > 0:
                    total_cutting = (total_cutting + backtracking(row, c, k-1))%MOD
                
            
            # for loop j  c+1 - end:
                # if preSum[r][c] - preSum[r][j] > 0 
                    # call backtracking(r, j, k-1)
            for col in range(c+1, COL):
                if preSumdp[r][c] - preSumdp[r][col] > 0:
                    total_cutting = (total_cutting + backtracking(r, col, k-1))%MOD
            
            memo[(r,c,k)] = total_cutting
            
            return total_cutting 
            
        
        return backtracking(0,0,k-1)

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        ROW, COL = len(pizza), len(pizza[0])
        MOD = 10**9+7
        preSum = [[0]*(COL+1) for _ in range(ROW+1)]
        
        for row in range(ROW-1, -1, -1):
            for col in range(COL-1, -1, -1):
                preSum[row][col] = preSum[row][col+1] + preSum[row+1][col]\
                + int(pizza[row][col] == 'A') - preSum[row+1][col+1]
        
        memo = {}
        def dp(k, r, c):
            if (k,r,c) in memo: return memo[(k,r,c)]
            if preSum[r][c] == 0: return 0
            if k == 0: return 1
            
            ans = 0
            for nr in range(r+1, ROW):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(k-1,nr,c))%MOD
            
            for nc in range(c+1, COL):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(k-1, r, nc))%MOD
            
            memo[(k,r,c)] = ans
            return memo[(k,r,c)]
        
        return dp(k-1, 0, 0)
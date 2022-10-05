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
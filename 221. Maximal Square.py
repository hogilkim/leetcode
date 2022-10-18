class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[0]*(COL+1) for _ in range(ROW + 1)]
        
        for row in range(ROW-1,-1,-1):
            for col in range(COL-1,-1,-1):
                dp[row][col] = dp[row+1][col] + dp[row][col+1] - dp[row+1][col+1] + int(matrix[row][col])
                
        max_sq_len = 0
        
        for row in range(ROW):
            for col in range(COL):
                for i in range(max_sq_len+1, min(ROW-row, COL-col)+1):
                    num_1s = dp[row][col] - dp[row+i][col] - dp[row][col+i] + dp[row+i][col+i]
                    if i**2 == num_1s:
                        max_sq_len = max(max_sq_len, i)
                    else: break
        
        return max_sq_len**2
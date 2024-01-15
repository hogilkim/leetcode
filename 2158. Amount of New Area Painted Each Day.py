# Solve again Jan 14, 2024 2158
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        dp = [0]*50001

        res = []
        
        for start, end in paint:
            idx = start
            res.append(0)

            while idx < end:

                if dp[idx] == 0:
                    dp[idx] = end
                    res[-1] += 1
                    idx += 1
                else:
                    nxt = dp[idx]
                    dp[idx] = max(dp[idx], end)
                    idx = nxt
        
        return res
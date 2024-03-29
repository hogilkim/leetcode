# Mar 23, 2024 Solve again
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        prev = [0]*(k+1)
        prev[0] = 1

        for N in range(1, n+1):
            total = 0
            curr = [0] * (k+1)
            for K in range(0, k+1):
                if K >= N:
                    total -= prev[K-N]
                total = (total + prev[K]) % MOD
                curr[K] = total

            
            prev = curr
        
        return curr[-1]


# so hard
class Solution:
    def numTilings(self, n: int) -> int:
        g = [0] * 1001
        u = [0] * 1001
        
        g[0], g[1], g[2] = 0, 1, 2
        u[0], u[1], u[2] = 0, 1, 2
        
        mod = 10**9+7
        
        for i in range(3, len(g)):
            u[i] = (u[i-1] + g[i-1]) % mod
            g[i] = (g[i-1] + g[i-2] + 2*u[i-2])% mod
        
        
        return g[n] % mod
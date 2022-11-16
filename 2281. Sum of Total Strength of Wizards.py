class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        N = len(strength)
        MOD = 10**9+7
        
        len_l = [0]*N
        len_r = [0]*N
        
        stack = []
        
        for i in range(N-1,-1,-1):
            while stack and strength[stack[-1]] >= strength[i]:
                j = stack.pop()
                len_l[j] = j - i
            stack.append(i)
        
        for idx in stack:
            len_l[idx] = idx + 1
        
        stack = []
        
        for i in range(N):
            while stack and strength[stack[-1]] > strength[i]:
                j = stack.pop()
                len_r[j] = i-j
                
            stack.append(i)
        
        for idx in stack:
            len_r[idx] = N - idx
            
        # prefix sum of prefix sum
        psps = list(accumulate(accumulate(strength)))+[0]
        ans = 0
        for i in range(N):
            L = len_l[i]
            R = len_r[i]
            total_R = (psps[i + R - 1] - psps[i - 1]) * L
            total_L = (psps[i - 1] - psps[max(-1, i - L - 1)]) * R
            ans = (ans + strength[i] * (total_R - total_L)) % MOD
        return ans
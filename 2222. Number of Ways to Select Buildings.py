class Solution:
    def numberOfWays(self, s: str) -> int:
        # O(n)
        
        one = zero = onezero = zeroone = total = 0
        
        for num in s:
            if num == "0":
                total+=zeroone
                onezero += one
                zero += 1
            else:
                total += onezero
                zeroone += zero
                one += 1
        
        return total
        
        
        # TLE
#         s = list(s)
#         res = 0
        
#         def dfs(insp, i):
#             nonlocal res
#             if len(insp) == 3:
#                 res += 1
#                 return
#             elif i > len(s)-1: return
            
#             for idx in range(i, len(s)):
#                 if not insp:
#                     dfs(s[idx],idx+1)
#                 elif s[idx] != insp[-1]:
#                     dfs(insp+s[idx], idx+1)
        
#         dfs("",0)
        
#         return res
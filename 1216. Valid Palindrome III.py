from collections import deque
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = {}
        
        def dfs(l, r, rmv):
            if (l,r,rmv) in dp: return dp[(l,r,rmv)]
            
            while l < r and s[l] == s[r]:
                l+=1
                r-=1
            if l>=r: return True
            if rmv >= k and s[l]!=s[r]: return False

            dp[(l,r,rmv)] = dfs(l+1,r,rmv+1) or dfs(l,r-1, rmv+1)
            
            return dp[(l,r,rmv)]
        
        return dfs(0,len(s)-1,0)
        
        
        # TLE
#         s = list(s)
#                         #l, r
#         queue = deque([(0,len(s)-1, 0)])
        
#         while queue:
#             l, r, rmv = queue.popleft()
            
#             if l >= r:
#                 return True
            
#             if s[l] == s[r]:
#                 queue.append((l+1, r-1, rmv))
#             elif rmv < k:
#                 queue.append((l+1,r,rmv+1))
#                 queue.append((l,r-1,rmv+1))
        
        
#         return False
            
            
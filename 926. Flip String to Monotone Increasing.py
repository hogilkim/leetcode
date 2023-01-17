class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count0 = s.count('0')
        count1 = 0
        res = min(count0, len(s)-count0)
        for char in s:
            if char == '0':
                count0 -= 1
            else:
                count1 += 1
                res = min(count0 + count1 - 1, res)
        
        return res

# solve again
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count0 = s.count('0')
        count1 = 0
        res = len(s) - count0
        
        for char in s:
            if char == '0':
                count0 -= 1
            else:
                res = min(res, count0 + count1)
                count1 += 1
        return res
    
    
    
        # simple, but not intuitive solution
#         min_flips = flips = s.count('0')
        
#         for char in s:
#             if char == '0':
#                 flips -= 1
#             else:
#                 flips += 1
#             min_flips = min(min_flips, flips)
#         return min_flips
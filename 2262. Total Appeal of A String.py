class Solution:
    def appealSum(self, s: str) -> int:
        seen = {}
        prev = res = 0
        
        
        
        for idx, char in enumerate(s):
            if char not in seen:
                curr = prev + idx + 1
            else:
                curr = prev + idx - seen[char]
            
            res += curr
            seen[char] = idx
            prev = curr
        
        return res
        
class Solution:
    def largestVariance(self, s: str) -> int:
        if len(set(s)) == 1: return 0
        res = 0
        
        for i in range(ord('a'), ord('z')+1):
            a = chr(i)
            for j in range(ord('a'), ord('z')+1):
                b = chr(j)
                
                if a == b: continue
                
                diff = 0
                b_diff = float('-inf')
                
                for char in s:
                    if char == a:
                        diff += 1
                        b_diff += 1
                    elif char == b:
                        diff -= 1
                        b_diff = diff
                        
                        if diff < 0:
                            diff = 0
                    else: continue
                    if b_diff >0:   
                        res = max(res, b_diff)
        
        return res
class Solution:
    def judgeSquareSum(self, c: int) -> bool:        
        l, r = 0, int(sqrt(c))

        while l <= r:
            curr = l*l + r*r
            if curr < c:
                l += 1
            elif curr > c:
                r -= 1
            else: return True
        
        return False
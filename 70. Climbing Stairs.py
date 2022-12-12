class Solution:
    def climbStairs(self, n: int) -> int:

        prev = 1
        curr = 2

        for i in range(2, n):
            curr, prev = curr + prev, curr
        
        return curr if n > 1 else 1
            
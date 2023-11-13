# Nov 12, 2023 70-2
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 2

        for num in range(3, n+1):
            prev, curr = curr, prev + curr
        
        return curr if n >= 2 else 1

class Solution:
    def climbStairs(self, n: int) -> int:

        prev = 1
        curr = 2

        for i in range(2, n):
            curr, prev = curr + prev, curr
        
        return curr if n > 1 else 1
            
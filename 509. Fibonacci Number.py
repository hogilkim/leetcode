class Solution:
    def fib(self, n: int) -> int:
        if not n: return 0
        prev_prev, prev = 0, 1
        
        num = 1
        
        while num < n:
            prev_prev, prev = prev, prev+prev_prev
            num += 1
        
        return prev
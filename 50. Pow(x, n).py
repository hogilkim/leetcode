class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod, index = 1, abs(n)
        
        while index:
            if index % 2: prod *= x
            
            x *= x
            index = index //2
            
        
        return prod if n >= 0 else 1/prod
            
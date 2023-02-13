class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        if high%2:
            res += 1
            high -= 1
        if low%2:
            res += 1
            low += 1

        return res + (high-low)//2 

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if not low%2: low += 1
        if not high%2: high -= 1
        
        return (high-low)//2 + 1
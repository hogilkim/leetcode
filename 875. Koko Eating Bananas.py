import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        def possible(speed):
            hours = 0
            
            for num in piles:
                hours += math.ceil(num/speed)
            
            return hours <= h
    
        low, high = 1, max(piles)
        
        while low < high:
            mid = (low+high)//2
            
            if possible(mid):
                high = mid
            else:
                low = mid + 1
            
        return low
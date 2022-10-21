class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # cannot change order 
        
        l, r = max(weights), sum(weights)
        
        while l<r:
            mid = (l+r)//2
            
            curr_weight=0
            daystook = 1
            # for loop
            for w in weights:
                if curr_weight + w > mid:
                    daystook += 1
                    curr_weight = 0

                curr_weight += w
            
            if daystook > days:
                l = mid+1
            
            else: r = mid
        
        return l
        
        

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid, need, cur = (left+right)//2, 1, 0
            
            for w in weights:
                if cur + w > mid:
                    cur = 0 
                    need += 1
                cur += w
            
            if need > days: left = mid + 1
            else: right = mid
        
        return left
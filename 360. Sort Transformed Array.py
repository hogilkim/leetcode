# Feb 2, 2024 360
import math
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0: 
            res = [self.calc(a,b,c,num) for num in nums]
            return res if b >= 0 else reversed(res)
        pivot = -b/(2*a)
        closest_pivot_idx = 0
        min_diff = float('inf')

        for idx, num in enumerate(nums):
            curr_diff = abs(num - pivot)

            if min_diff > curr_diff:
                closest_pivot_idx = idx
                min_diff = curr_diff

        
        l = closest_pivot_idx
        r = l + 1
        res = []
        while l >= 0 and r < len(nums):
            if abs(nums[l] - pivot) > abs(nums[r] - pivot):
                res.append(self.calc(a,b,c,nums[r]))
                r += 1
            else:
                res.append(self.calc(a,b,c,nums[l]))
                l -= 1
        
        while l >= 0:
            res.append(self.calc(a,b,c,nums[l]))
            l -= 1
        while r < len(nums):
            res.append(self.calc(a,b,c,nums[r]))
            r += 1
        
        return res if a >= 0 else reversed(res)
    
    def calc(self, a, b, c, x):
        return a*x*x + b*x + c
            

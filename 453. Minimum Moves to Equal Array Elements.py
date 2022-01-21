# solve again
# first attempt - Jan 20, 2022
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
       
        
        res = 0
        min_val = min(nums)
        for i in range(len(nums)):
            res += nums[i] - min_val
        
        return res
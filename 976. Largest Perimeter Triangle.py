class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        while len(nums)>=3 and nums[-1] >= nums[-2] + nums[-3]:
            nums.pop()
        
        return sum(nums[-3:]) if len(nums)>=3 else 0
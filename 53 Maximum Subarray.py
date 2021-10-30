class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0
            
        return max_sum
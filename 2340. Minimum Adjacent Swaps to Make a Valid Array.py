class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_num = 0
        max_idx = 0
        min_num = float('inf')
        min_idx = 0
        
        for idx, num in enumerate(nums):
            if num < min_num:
                min_num = num
                min_idx = idx
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i
            
        if min_idx > max_idx: return min_idx + len(nums) - 1 - max_idx - 1
        else: return min_idx + len(nums)-1-max_idx
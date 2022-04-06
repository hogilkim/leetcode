class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        
        for i in range(1, len(nums)):
            if nums[curr] < nums[i]:
                curr += 1
                nums[curr] = nums[i]
        
        return curr + 1
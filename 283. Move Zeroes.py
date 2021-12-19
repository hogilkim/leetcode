class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # better solution
        left = 0
        
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
    
        
        # my solution
        
        # i = 0
        # count = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         del nums[i]
        #         count += 1
        #     else:
        #         i += 1
        # for j in range(count):
        #     nums.append(0)
        # return nums    
    
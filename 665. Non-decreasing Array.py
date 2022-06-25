class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        modified = False
        
        nums = [-10e5] + nums + [10e5]
        for i in range(len(nums[1:])):
            if nums[i] <= nums[i+1]: continue
            if modified: return False

            if nums[i-1]<=nums[i+1]: nums[i] = nums[i+1]
            else: nums[i+1] = nums[i]
            modified = True
         
        return True
            
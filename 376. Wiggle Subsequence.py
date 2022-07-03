class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        count = 1
        increasing=None
        
        for i in range(1,len(nums)):
            
            if nums[i-1] > nums[i] and increasing != False:
                increasing = False
                count += 1
            elif nums[i-1] < nums[i] and increasing != True:
                increasing = True
                count += 1
            
        return count
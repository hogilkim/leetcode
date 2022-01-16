# solve again
# first attempt - Jan 16, 2022
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2: return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        
        for i in range(len(nums)):
            nextDP = set()
            
            for val in dp:
                if val+nums[i] == target: return True
                nextDP.add(val+nums[i])
                nextDP.add(val)
            
            dp = nextDP
        
        return True if target in dp else False
        
        
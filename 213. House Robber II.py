# second try - solved! but previous one better

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]     
            
        
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums)-1]))
        
    
    
    def helper(self, nums):
        if len(nums) < 2: return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])] 
        
        def helper2(i):
            if i >= len(nums): return
            dp.append( max( dp[i-1], dp[i-2] + nums[i] ) )
        
        
        for i in range(2, len(nums)):
            helper2(i)
        
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums_sublist):
            print(nums_sublist)
            bigger_val = 0
            smaller_val = 0
            for num in nums_sublist:
                temp = max(smaller_val + num, bigger_val)
                smaller_val = bigger_val
                bigger_val = temp
            return bigger_val

        
        max1 = helper(nums[1:])
        max2 = helper(nums[:-1])
        
        return max(nums[0], max1, max2)
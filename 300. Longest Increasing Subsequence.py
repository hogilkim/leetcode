# second attempt - Jan 10, 2022 - solved!
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            max_lis = 0
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    max_lis = max(max_lis, dp[j])
                
            dp[i] = max_lis + 1
    
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        nums = list(reversed(nums))
        result = [1]
        
        for i in range(1, len(nums)):
            max_subsequence = 1
            for j in range(i):
                if nums[j] > nums[i]:
                    max_subsequence = max(max_subsequence, result[j] + 1)
            result.append(max_subsequence)
            
            
        return max(result)
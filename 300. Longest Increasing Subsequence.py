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
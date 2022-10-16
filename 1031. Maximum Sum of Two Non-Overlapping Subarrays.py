class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(len(nums)-1):
            nums[i+1] += nums[i]
            
        nums = [0] + nums
        
        def maxTwoArraySum(f,s):
            maxF = 0
            ans = 0
            
            for i in range(f+s, len(nums)):
                maxF = max(maxF, nums[i-s]-nums[i-f-s])
                ans = max(ans, maxF + nums[i] - nums[i-s])
            
            return ans
        
        
        return max(maxTwoArraySum(firstLen, secondLen), maxTwoArraySum(secondLen, firstLen))
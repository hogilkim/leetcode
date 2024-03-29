# Third - Aug 5, 2022
# Solve again
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0]=1
        for i in range(target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i]+=dp[i-num]
        
        return dp[-1]
        
# solve again
# second attempt - Jan 17, 2022
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        dp = [0]*(target+1)
        
        dp[0] = 1
        
        
        for i in range(target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        
        return dp[-1]

# try again
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0]=1
        for i in range(1,len(dp)):
            for num in nums:
                if i-num >=0:
                    dp[i]+= dp[i-num]
        return dp[-1]
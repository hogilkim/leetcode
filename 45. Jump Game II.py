class Solution:
    def jump(self, nums: List[int]) -> int:

        steps = 0
        curr_end = 0
        curr_furthest = 0
        for i in range(len(nums)-1):
            curr_furthest = max(curr_furthest, nums[i] + i)

            if curr_furthest >= len(nums)-1:
                steps += 1
                break

            if i == curr_end:
                steps += 1
                curr_end = curr_furthest

        return steps                


        # dp solution w/ time O(n) - O(n^2)

        # dp = [float('inf')]*len(nums)
        # dp[0] = 0

        # for i in range(len(nums)):

        #     for j in range(i, min(i+nums[i]+1, len(nums))):
        #         dp[j] = min(dp[j],dp[i] + 1)
        
        # return dp[-1]
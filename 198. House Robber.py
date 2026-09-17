# Sep 16, 2026 198
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]

        return max(dp[-1], dp[-2])


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0, 0] + nums
        dp = [0] * len(nums)

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


# second try - solved! but previous one better


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        def helper(i):
            if i >= len(nums):
                return

            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))

        for i in range(2, len(nums)):
            helper(i)
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:

        bigger_val = 0
        smaller_val = 0

        for num in nums:
            temp = max(bigger_val, num + smaller_val)
            smaller_val = bigger_val
            bigger_val = temp

        return bigger_val

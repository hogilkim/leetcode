# Sep 10, 2026 53-4
# solve again
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = float("-inf")
        currsum = 0

        for num in nums:
            currsum += num
            max_val = max(max_val, currsum)
            if currsum < 0:
                currsum = 0

        return max_val


# Nov 17, 2023 53-3
# solve again
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = float("-inf")

        for num in nums:
            currsum += num
            maxsum = max(maxsum, currsum)
            if currsum < 0:
                currsum = 0

        return maxsum


# Second Attempt, looked at the answer.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum

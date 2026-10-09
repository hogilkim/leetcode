# solve again.
# Oct 9, 2026 962
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = []

        for idx, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(idx)

        maxwidth = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                maxwidth = max(maxwidth, j - stack.pop())

        return maxwidth

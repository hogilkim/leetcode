# Solve again Jan 23, 2024 2863
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        stack = []
        max_len = 0

        for i in range(len(nums)-1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for idx, num in enumerate(nums):
            while stack and idx >= stack[-1]: stack.pop()

            while stack and num > nums[stack[-1]]:
                max_len = max(max_len, stack[-1] - idx + 1)
                stack.pop()
        
        return max_len
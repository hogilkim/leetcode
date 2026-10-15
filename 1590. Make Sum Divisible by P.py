# solve again
# Oct 14, 2026 1590
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0

        prefix_sums = {0: -1}
        minlen = len(nums)
        prefix = 0

        for idx, num in enumerate(nums):
            prefix = (prefix + num) % p
            needed = (prefix - target) % p

            if needed in prefix_sums:
                minlen = min(minlen, idx - prefix_sums[needed])

            prefix_sums[prefix] = idx
        return minlen if minlen < len(nums) else -1

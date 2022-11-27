from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0
        
        for e in range(1, len(nums)):
            for s in range(e):
                diff = nums[e] - nums[s]
                res += dp[(s, diff)]
                dp[(e, diff)] += dp[(s,diff)] + 1
        
        return res
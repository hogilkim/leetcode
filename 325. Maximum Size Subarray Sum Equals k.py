import collections
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        acc_to_idx = {0:-1}
        acc = 0
        res = 0
        for idx, num in enumerate(nums):
            acc += num
            if acc not in acc_to_idx: acc_to_idx[acc] = idx
            if acc - k in acc_to_idx:
                res = max(res, idx - acc_to_idx[acc-k])
        
        return res
        
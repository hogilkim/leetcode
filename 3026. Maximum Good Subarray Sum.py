from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        LEN = len(nums)
        prefix_sum = [0]*LEN
        prefix_sum[0] = nums[0]
        hash_map = {}
        res = float('-inf')

        for i in range(1, LEN):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        for idx, num in enumerate(nums):
            if num - k in hash_map:
                before_idx = hash_map[num-k]
                res = max(res, prefix_sum[idx] - prefix_sum[before_idx] + nums[before_idx])
            
            if k + num in hash_map:
                before_idx = hash_map[k+num]
                res = max(res, prefix_sum[idx] - prefix_sum[before_idx] + nums[before_idx])
            
            if num in hash_map:
                curr = hash_map[num]

                if prefix_sum[curr] > prefix_sum[idx]:
                    hash_map[num] = idx
            
            else:
                hash_map[num] = idx
        
        return res if res > float('-inf') else 0
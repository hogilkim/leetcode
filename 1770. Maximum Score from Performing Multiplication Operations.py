class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def fn(lo, hi, k):
            if k == len(multipliers): return 0
            return max(nums[lo] * multipliers[k] + fn(lo+1, hi, k+1), nums[hi] * multipliers[k] + fn(lo, hi-1, k+1))
        
        return fn(0, len(nums)-1, 0)
        
        # =================================================================================================================================================
        
#         dp = [[0 for _ in range(len(multipliers))] for _ in range(len(multipliers))]
        
#         def backtracking(num_l, mult_idx):
#             if mult_idx == len(multipliers):
#                 return 0
#             if dp[num_l][mult_idx]: return dp[num_l][mult_idx]

#             num_r = len(nums) - 1 - (mult_idx - num_l)
#             dp[num_l][mult_idx] = max(nums[num_l] * multipliers[mult_idx] + backtracking(num_l+1, mult_idx+1), nums[num_r]*multipliers[mult_idx]+backtracking(num_l, mult_idx+1))
            
#             return dp[num_l][mult_idx]
#         return backtracking(0,0)
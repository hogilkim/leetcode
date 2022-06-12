import collections
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        arr_sum = sum(nums)
        if arr_sum == x: return len(nums)
        target = arr_sum - x
        
        curr_sum = 0
        l = 0
        max_len = 0
        
        for idx, num in enumerate(nums):
            curr_sum += num
            
            while curr_sum > target and l <= idx:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                max_len = max(max_len, idx - l + 1)
        
        return len(nums) - max_len if max_len > 0 else -1
        
        
        
#=====================MEMORY LIIMT EXCEEDED==================================
#         memo = {}
        
#         def backtracking(start, end, target, count):
#             if (start, end) in memo: return memo[(start,end)]
#             if start > end: return float('inf')
#             if nums[start] > target and nums[end] > target:
#                 memo[(start,end)] = float('inf')
#                 return float('inf')
            
#             if nums[start] == target or nums[end]==target:
#                 memo[(start,end)] = count + 1
#                 return count + 1
            
#             res1 = backtracking(start+1, end, target - nums[start], count + 1)
#             res2 = backtracking(start, end-1, target - nums[end], count + 1)
#             memo[(start, end)] = min(res1, res2)
            
#             return memo[(start, end)]
        
#         res = backtracking(0,len(nums)-1, x, 0)
#         return res if res<=10e5 else -1
            
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # solve again for this solution. O(n)
        sub_sum = 0
        
        min_len = len(nums) + 1
        slow = 0
        
        for fast in range(len(nums)):
            sub_sum += nums[fast]
            
            while sub_sum >= target and slow <= fast:
                sub_sum -= nums[slow]
                min_len = min(min_len, fast - slow + 1)
                
                slow += 1
        
        return min_len if min_len < len(nums) + 1 else 0
        
        
        # solved. High time complexity O(n)~O(n^2)
        
#         sub_sum = nums[0]
        
#         slow = fast = 0
#         if sub_sum < target:
#             min_len = len(nums)
#         else:
#             return 1
        
#         while slow < len(nums) and fast < len(nums):
#             #sub_sum = sum(nums[slow:fast+1])
            
#             if sub_sum >= target:
#                 min_len = min(min_len, fast - slow + 1)
#             if sub_sum < target:
#                 fast += 1
#             else:
#                 slow += 1
                
            
            
            
#         if slow == 0 and sub_sum < target:
#             return 0
#         else:
#             return min_len
        
        
            
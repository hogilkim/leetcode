# NICE JOB!!!!
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        left = right = 0
        num_odds = 0
        odd_stack = []
        
        total_subarrays = 0
        
        for i, num in enumerate(nums):
            if num%2 == 1:
                odd_stack.append(i)
            
            if len(odd_stack) == k:
                # find right
                right = i
                while right+1 < len(nums) and nums[right+1]%2 == 0:
                    right += 1
                
                total_subarrays += (odd_stack[0] - left + 1) * \
                                    (right - odd_stack[-1] + 1)
                
                left = odd_stack[0] + 1
                odd_stack = odd_stack[1:]
                
        
        return total_subarrays
                
                
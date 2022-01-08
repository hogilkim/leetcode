# second attempt - solve again
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = max(nums)
        cur_min = cur_max = 1
        for num in nums:
            temp = cur_max * num
            cur_max = max(temp, cur_min*num, num)
            cur_min = min(temp, cur_min*num, num)
            result = max(result, cur_max)
        return result

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        min_val, max_val = 1,1
        
        for num in nums:
            temp = num*max_val
            max_val = max(temp, num*min_val, num)
            min_val = min(num*min_val, temp, num)
            print(max_val)
            result = max(result, max_val)
        return result
        
#         curr = 1
#         max_val = nums[0]
#         sub_max_val = nums[0]
#         for i in range(len(nums)):
#             curr *= nums[i]
#             sub_max_val=max(sub_max_val, curr)
#             if curr < 0:
#                 max_val = max(sub_max_val, max_val)
#                 if i + 1 <len(nums):
#                     sub_max_val = nums[i+1]
                
                
#             if curr == 0:
#                 max_val = max(max_val, 0)
#                 curr = 1
                
                
#         return max(max_val, sub_max_val)
                
                
                
                
#         return max_val
            
#         neg_val = 1
#         max_prod = 1
#         buffer  = 1
#         zero = False
#         for i in range(len(nums)):
#             if nums[i] < 0 :
#                 max_prod *= buffer
#                 buffer = 1
#                 neg_val *= nums[i]
#                 if neg_val > 0:
#                     max_prod *= neg_val
#                     neg_val = 1
#             elif nums[i] == 0:
#                 zero = True
#             else: 
#                 buffer *= nums[i]
                
#         if max_prod == 1 and buffer == 1:
#             max_prod *= neg_val
#             if zero == True:
#                 return 0
#         elif max_prod == 1:
#             max_prod *= buffer
#         return max_prod
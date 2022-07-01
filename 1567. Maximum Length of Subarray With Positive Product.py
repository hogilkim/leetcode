class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # Solution #2 from discussion
        
        neg = 1 if nums[0] < 0 else 0
        pos = 1 if nums[0] > 0 else 0
        
        max_sublen = pos
        
        for num in nums[1:]:
            if num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif num < 0:
                pos,neg = neg + 1 if neg > 0 else 0, pos+1
            else:
                pos=neg=0
                
            max_sublen = max(max_sublen, pos)
            
        return max_sublen
        
        
        # Solution #1
#         prod = 1
#         neg_idx = -1
#         beg_idx = 0
#         max_sublen = 0
        
#         for idx, num in enumerate(nums):
#             if num == 0:
#                 prod = 1
#                 neg_idx = -1
#                 beg_idx = idx + 1
#                 continue
#             if num < 0 and neg_idx < 0:
#                 neg_idx = idx
                
#             prod *= num
#             if prod > 0:
#                 max_sublen = max(max_sublen, idx - beg_idx + 1)
#             else:
#                 max_sublen = max(max_sublen, idx - neg_idx)
                
        
#         return max_sublen
# Oct 30, 2023
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        return sum(list(set(nums)))*2 - sum(nums)
#         seen = set()
        
#         for num in nums:
#             if num not in seen:
#                 seen.add(num)
#             elif num in seen:
#                 seen.remove(num)
            
        
#         return list(seen).pop()
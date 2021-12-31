class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # second time - could not solve. solve again
        
        res = []
        
        nums.sort()
        for i, first_val in enumerate(nums):
            if i > 0 and nums[i-1] == first_val:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = first_val + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([first_val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                
        return res


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = []
#         a_history = []
#         for i in range(len(nums)-2):
#             if nums[i] in a_history:
#                 continue
#             a = nums[i]
#             a_history.append(a)
            
#             target = (-1)*a
#             left = i + 1
#             right = len(nums)-1
#             print(a)
#             while left < right:
#                 if nums[left] + nums[right] < target:
#                     left += 1
#                 elif nums[left] + nums[right] > target:
#                     right -= 1
#                 elif nums[left] + nums[right] == target:
#                     result.append([a, nums[left], nums[right]])
#                     left += 1
#                     while left < right and nums[left] == nums[left-1]:
#                         left += 1
                    
                    
#         return result
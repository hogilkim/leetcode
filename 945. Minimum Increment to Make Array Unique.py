from collections import deque
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        total_moves = 0
        for i in range(1,len(nums)):
            if nums[i] <=nums[i-1]:
                addup = nums[i-1] - nums[i] + 1
                nums[i] += addup
                total_moves += addup
        
        return total_moves
        
        
#         nums = sorted(nums)
#         counter = nums[0] + 1
#         dup_list = deque([])
#         total_moves = 0
        
#         # print(nums)
#         # for num in nums:
#         for i in range(1, len(nums)):
#             # if prev is same as curr num:
#             # print(nums[i])
#             if nums[i-1] == nums[i]:
#                 # add duplist
#                 dup_list.append(nums[i])
                
#             # if counter == num: num+1
#             if counter == nums[i]: counter + 1
            
#             # while counter < num:
#                 # if there is duplicate
#                     # calculate the diff and record the total moves we made
#             while counter < nums[i]:
#                 if dup_list:
#                     total_moves += counter - dup_list.popleft()
#                 counter += 1
#             if counter == nums[i]:
#                 counter += 1
        
#         while dup_list:
#             total_moves += counter - dup_list.popleft()
#             counter += 1
        
#         return total_moves
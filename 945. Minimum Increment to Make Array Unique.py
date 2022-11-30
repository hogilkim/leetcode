# second - Nov 30, 2022
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        # sort
        nums = sorted(nums)
        
        res = 0
        
        # for loop starting from index 1
        for i in range(1, len(nums)):
            # compare to prev. 
            # if curr <= prev
            if nums[i-1] >= nums[i]:
                # make curr = prev+1
                res += abs(nums[i] - nums[i-1]) + 1
                nums[i] = nums[i-1] + 1
        
        return res


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
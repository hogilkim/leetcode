# solve again
# third attempt - Dec 26, 2022
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False


# solve again
# second attempt - Jan 18, 2022
import collections
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums)-1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal==0 else False
        
        
        
        # not working solution
#         visited = set()
        
#         will_visit = collections.deque([0])
        
        
#         while will_visit:
#             curr = will_visit.popleft()
#             visited.add(curr)
#             for i in range(1, nums[curr]+1):
#                 if (curr + i < len(nums)) and (curr + i not in visited):
#                     will_visit.append(curr + i)
#                     visited.add(curr+i)
#                 if (curr - i > 0) and (curr - i not in visited):
#                     will_visit.append(curr - i)
#                     visited.add(curr-i)
#             if curr == len(nums)-1:
#                 return True
#         return False
        
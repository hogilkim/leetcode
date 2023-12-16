# Dec 15, 2023 78-2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(i, part):
            if i >= len(nums): 
                res.append(part.copy())
                return

            # X include i
            backtracking(i+1, part.copy())

            # include i
            part.append(nums[i])
            backtracking(i+1, part.copy())

        
        backtracking(0, [])

        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Another Solution & better, clean
        res = []
        subset = []
        
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i+1)
            # decision not to include nums[i]
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return res
        
        # my solution: worked
        
#         res = [[]]
        
#         def backtrack(part, i):
#             if i >= len(nums) - 1:
#                 return
#             for j in range(i+1, len(nums)):
#                 res.append(part + [nums[j]])
#                 backtrack(part + [nums[j]], j)
        
#         backtrack([], -1)
        
#         return res
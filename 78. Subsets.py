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
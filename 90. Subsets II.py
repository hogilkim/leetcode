# solve again
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(part, i):

            if i >= len(nums):
                res.append(part.copy())
                return
            
            part.append(nums[i])
            backtrack(part, i + 1)
            part.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(part,i+1)
        
        backtrack([],0)
        return res
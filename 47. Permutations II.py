# first attempt - Jan 11
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        indices = set()
        def backtrack(part):
            if len(part) == len(nums): result.append(part.copy())
            prev = -100
            for i in range(len(nums)):
                if nums[i] == prev:
                    continue
                if i not in indices:
                    part.append(nums[i])
                    indices.add(i)
                    backtrack(part)
                    prev = part.pop()
                    indices.remove(i)
        backtrack([])
        return result
            
            
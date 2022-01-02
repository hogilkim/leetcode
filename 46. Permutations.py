class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(part):
            if len(part) == len(nums):
                res.append(part)
                return
            rest = [item for item in nums if item not in part]
            for r in rest:
                dfs(part + [r])
        
        dfs([])
        return res
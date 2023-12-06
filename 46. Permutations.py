# Dec 6, 2023 46-2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = set()
        res = []

        def backtracking(curr_list):
            if len(curr_list) == len(nums):
                res.append(curr_list.copy())
                return
            
            for i in range(len(nums)):
                if i not in path:
                    path.add(i)
                    curr_list.append(nums[i])
                    backtracking(curr_list.copy())
                    path.remove(i)
                    curr_list.pop()
        
        backtracking([])

        return res

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
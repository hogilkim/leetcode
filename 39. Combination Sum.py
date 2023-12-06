# Dec 6, 2023 39-2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr_list):
            if idx == len(candidates): return

            if sum(curr_list) == target: 
                res.append(curr_list.copy())
                return
            elif sum(curr_list) > target: return

            # include curr idx
            curr_list.append(candidates[idx])
            backtrack(idx, curr_list.copy())
            # X include curr idx
            curr_list.pop()
            backtrack(idx+1, curr_list.copy())

        if candidates: backtrack(0, [])
        
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(part, i):
            if sum(part) > target or i >= len(candidates): return
            if sum(part) == target:
                res.append(part.copy())
                return
            
            #decide to include i
            part.append(candidates[i])
            backtrack(part, i)
            
            #decide not to include i
            part.pop()
            backtrack(part, i+1)
        
        if candidates: backtrack([],0)
        return res
            
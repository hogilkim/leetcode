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
            
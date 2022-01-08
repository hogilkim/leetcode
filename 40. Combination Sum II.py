class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        
        def backtrack(part, index):
            part_sum = sum(part)
            if part_sum == target: 
                res.append(part.copy())
                return
            if part_sum > target or index >= len(candidates): return
            
            #include candidates[index]
            part.append(candidates[index])
            backtrack(part, index + 1)
            
            # X include candidates[index]
            skip = part.pop()
            while index < len(candidates) and candidates[index] == skip:
                index += 1
            backtrack(part, index)
        
        
        backtrack([],0)
        return res
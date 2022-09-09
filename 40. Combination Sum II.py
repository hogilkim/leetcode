class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        
        print(candidates)
        
        # def backtracking(i, part_sum):
        def backtracking(i, part_sum):
            # if partsum == target: append
            if sum(part_sum) == target: 
                res.append(part_sum.copy())
                return
            # part_sum > target: return
            if sum(part_sum) > target or i >= len(candidates): return
            
            # case 1. include curr i -> backtracking(i+1, part_sum)
            part_sum.append(candidates[i])
            backtracking(i+1, part_sum)
            
            
            # case 2. X include curr i
            # skip = curr[i]
            # while curr[i] == skip: i+= 1
            skip = part_sum.pop()
            while i < len(candidates) and skip == candidates[i]:
                i += 1

            backtracking(i, part_sum)
            
            
        backtracking(0, [])
        return res
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
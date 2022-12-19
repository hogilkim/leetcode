import sys
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def calc(w, b):
            return abs(w[0]-b[0]) + abs(w[1]-b[1])
        
        memo = {}
        used_bike = [0]*len(bikes)
        
        def backtracking(i, bikememo):
            if i == len(workers): return 0
            if (i, tuple(bikememo)) in memo: return memo[(i,tuple(bikememo))]
            res = float('inf')
            for j in range(len(bikes)):
                if bikememo[j]: continue
                newdis = calc(workers[i], bikes[j])
                bikememo[j] = 1
                res = min(res, backtracking(i+1, bikememo) + newdis)
                bikememo[j] = 0
            
            memo[(i, tuple(used_bike))] = res
            return res

        return backtracking(0, used_bike)
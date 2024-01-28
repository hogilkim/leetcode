#Jan 28, 2024 403-2
class Solution:
    def canCross(self, stones: List[int], prev = 0) -> bool:
        
        memo = {}
        def dfs(idx, prev):
            if idx == len(stones)-1: return True
            if (idx, prev) in memo: return memo[(idx, prev)]

            memo[(idx, prev)] = False

            for i in range(idx+1, len(stones)):
                if prev-1 <= stones[i] - stones[idx]<= prev+1:
                    if dfs(i, stones[i] - stones[idx]):
                        memo[(idx, prev)] = True
                        return True
                
            return False
        return dfs(0, 0)

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        memo = {}
        def dfs(idx, last_unit):
            if (idx, last_unit) in memo: return memo[(idx, last_unit)]
            
            if idx == len(stones)-1: return True

            i = idx + 1
            res = False
            while i < len(stones) and stones[i] - stones[idx] <= last_unit + 1:
                if last_unit - 1 <= stones[i] - stones[idx]:
                    res = res or dfs(i, stones[i] - stones[idx])
                i += 1
            

            memo[(idx, last_unit)] = res
            return res
        
        return dfs(0, 0)
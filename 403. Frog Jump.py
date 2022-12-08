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
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        
        # k: # of numbers
        # n : 1~n
        
        res = []
        def dfs(part):
            if len(part) == k:
                res.append(part)
                return
            
            for num in range(part[-1]+1 if part else 1,n+1):
                if num not in part:
                    dfs(part + [num])
            
            
        dfs([])
        return res
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # path
        bank = set(bank)

        def onediff(a,b):
            return sum(c1!=c2 for c1,c2 in zip(a,b)) == 1
        
        
        res = float('inf')
        
        def dfs(curr,depth):
            nonlocal res
            if depth > res: return
            
            if curr == end:
                res = min(res, depth)
                return
            
            bank.remove(curr)
            
            for string in bank:
                if onediff(curr,string):
                    dfs(string, depth+1)
            
            bank.add(curr)
            
        
        bank.add(start)
        dfs(start, 0)
        return -1 if res == float('inf') else res
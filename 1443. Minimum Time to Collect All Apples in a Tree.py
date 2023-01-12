from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        need_visit = set()

        def dfs(prev, curr):
            res = False
            for nxt in graph[curr]:
                
                if nxt == prev: continue
                temp = dfs(curr, nxt)
                res = res or temp
            
            res = res or hasApple[curr]
            if res: need_visit.add(curr)
            return res
        
        dfs(-1,0)
        return max(2*len(need_visit) - 2,0)

        

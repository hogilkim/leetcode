from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        NOT_EQUAL = "!"
        EQUAL = "="
        graph = collections.defaultdict(list)
        neq = []
        
        for eq in equations:
            u = eq[0]
            v = eq[3]
            
            if eq[1] == EQUAL:
                graph[u].append(v)
                graph[v].append(u)
            else:
                neq.append((u,v))
                
        visited = set()
        
        def dfs(curr, target):
            if curr == target: return True
            visited.add(curr)
            res = False
            for element in graph[curr]:
                if element in visited: continue
                if dfs(element, target):
                    res = True
                    break
            
            visited.remove(curr)
            
            return res
        
        
        for a, b in neq:
            if dfs(a, b): return False
        
        return True
            
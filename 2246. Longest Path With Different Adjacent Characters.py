from collections import defaultdict
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for idx, p in enumerate(parent):
            if p == -1: continue
            # graph[idx].append(p)
            graph[p].append(idx)
        

        pathlen = 0

        def dfs(curr):
            nonlocal pathlen
            max1 = max2 = 0
            for nxt in graph[curr]:
                # if nxt == prev: continue
                
                childlen = dfs(nxt)
                if s[nxt] != s[curr]:
                    if childlen > max1:
                        max1, max2 = childlen, max1
                    elif childlen > max2:
                        max2 = childlen
                
            
            pathlen = max(pathlen, max1+max2+1)
            return max1+1

        dfs(0)
        return pathlen
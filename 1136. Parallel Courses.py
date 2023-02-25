from collections import defaultdict
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        prereqs = defaultdict(list)

        for prev, nxt in relations:
            prereqs[nxt].append(prev)


        depth = {}
        path = set()
        def dfs(node):
            depth[node] = 1
            path.add(node)
            
            for nxt in prereqs[node]:
                
                if nxt in path: 
                    return -1

                if nxt not in depth:
                    nxtdepth = dfs(nxt)

                    if nxtdepth == -1: 
                        return -1

                    else:
                        depth[node] = max(depth[node], nxtdepth+1)

                else:
                    depth[node] = max(depth[nxt] + 1, depth[node])

            path.remove(node)

            return depth[node]

        
        for node in range(1, n+1):
            if node not in depth:
                if dfs(node) == -1: 
                    return -1
        
        return max(depth.values())

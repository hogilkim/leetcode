from collections import Counter, defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        res = [0]*n
        
        def dfs(prev, curr):
            
            counter = Counter()
            for nxt in graph[curr]:
                if nxt == prev: continue
                counter = counter + dfs(curr, nxt)
            counter[labels[curr]] += 1
            res[curr] = counter[labels[curr]]

            return counter
        
        dfs(-1, 0)
        return res
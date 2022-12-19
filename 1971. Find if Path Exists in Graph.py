from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def dfs(node):
            visited.add(node)
            if node == destination:
                return True
            
            res = False
            for nxt in graph[node]:
                if nxt not in visited:
                    res = res or dfs(nxt)
            return res
        return dfs(source)
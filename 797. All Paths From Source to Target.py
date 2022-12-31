class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        N = len(graph)-1

        path = [0]
        def dfs(curr):
            if curr == N:
                res.append(path.copy())
                return

            for nxt in graph[curr]:
                path.append(nxt)
                dfs(nxt)
                path.pop()
        
        dfs(0)
        return res

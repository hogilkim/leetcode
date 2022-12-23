from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        N = n
        res = [0]*N
        count = [1]*N
        
        def dfs(subroot, prev):
            for child in graph[subroot]:
                if child == prev: continue
                dfs(child, subroot)
                count[subroot] += count[child]
                res[subroot] += res[child] + count[child]
        
        def dfs2(subroot, prev):
            for child in graph[subroot]:
                if child == prev: continue
                res[child] = res[subroot] - count[child] + N - count[child]
                dfs2(child, subroot)
        

        dfs(0, -1)
        dfs2(0, -1)

        return res

# Solve again Jan 17, 2024 2421
class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
    def find(self, n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)

        if aRoot == bRoot:
            return False
        
        if self.rank[aRoot] < self.rank[bRoot]:
            self.par[aRoot] = bRoot
            self.rank[bRoot] += self.rank[aRoot]
        else:
            self.par[bRoot] = aRoot
            self.rank[aRoot] += self.rank[bRoot]

from collections import defaultdict
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        valToNode = defaultdict(list)
        for node, val in enumerate(vals):
            valToNode[val].append(node)
        
        res = 0
        uf = UnionFind(len(vals))

        for val in sorted(valToNode.keys()):
            for samevalnode in valToNode[val]:
                for nei in graph[samevalnode]:
                    if vals[nei] <= vals[samevalnode]:
                        uf.union(nei, samevalnode)
            
            count = defaultdict(int)
            for samevalnode in valToNode[val]:
                count[uf.find(samevalnode)] += 1
                res += count[uf.find(samevalnode)]
        
        return res
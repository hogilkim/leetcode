# solve again
# Dec 17, 2023 310-2
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        graph = defaultdict(list)

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        degrees = []    
        leaves = []; new_leaves = []
        
        for node in range(n):
            if len(graph[node]) == 1: leaves.append(node)
            degrees.append(len(graph[node]))
        
        while n > 2:
            for leaf in leaves:
                degrees[leaf] -= 1
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        new_leaves.append(neighbor)

            n -= len(leaves)

            leaves = new_leaves.copy()
            new_leaves = []
        
        return leaves

# solve again
# first attempt - Jan 12, 2022 
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]
        graph = {i:[] for i in range(n)}
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        leaves, new_leaves, in_degree = [], [], []
        
        for node in range(n):
            if len(graph[node]) == 1:
                leaves.append(node)
            in_degree.append(len(graph[node]))
            
        while n > 2:
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        new_leaves.append(neighbor)
            
            n -= len(leaves)
            leaves = new_leaves.copy()
            new_leaves.clear()
        
        return leaves
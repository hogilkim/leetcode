class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph_map = {i:[] for i in range(n)}
        
        visited = set()
        
        for edge in edges:
            graph_map[edge[0]].append(edge[1])
            graph_map[edge[1]].append(edge[0])
        
        def dfs(node):
            visited.add(node)
            for next_node in graph_map[node]:
                if next_node not in visited:
                    dfs(next_node)
            
        count = 0
        for num in range(n):
            if num not in visited:
                dfs(num)
                count += 1
        return count
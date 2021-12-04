class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # THIS IS DIFFERENT PROBLEM FROM COURSE SCHEDULE
        tree_map = {i:[] for i in range(n)}

        for edge in edges:
            tree_map[edge[0]].append(edge[1])
            tree_map[edge[1]].append(edge[0])
            
        visited = set()
        def dfs(node, prev):
            if node in visited: return False
            visited.add(node)
            for next_node in tree_map[node]:
                if prev != next_node:
                    if not dfs(next_node, node): return False
            
            visited.add(node)
            return True
                
                
            
        

        return dfs(0, -1) and n == len(visited)
        
        
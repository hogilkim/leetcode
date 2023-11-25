# Nov 25, 2023 133-3 solve again
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        og_to_clone = {}

        def dfs(n):
            if n in og_to_clone:
                return og_to_clone[n]

            copy = Node(n.val)
            og_to_clone[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(node) if node else None

# second try, couldn't solve
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        og_to_clone = {}
        
        def dfs(node):
            if node in og_to_clone:
                return og_to_clone[node]
            copy = Node(node.val)
            og_to_clone[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        return dfs(node) if node else None

# Solve again

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        og_to_copy={}

        def dfs(node):
            if node in og_to_copy:
                return og_to_copy[node]
            copy_node = Node(node.val)
            og_to_copy[node]=copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return copy_node
        
        return dfs(node) if node else None
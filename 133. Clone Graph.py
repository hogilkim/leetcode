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
# solve again
# first attempt - Jan 18, 2022

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {root : []}
        
        def dfs_build_graph(node):
            if node.left:
                graph[node.left] = [node]
                graph[node].append(node.left)
                dfs_build_graph(node.left)
            if node.right:
                graph[node.right] = [node]
                graph[node].append(node.right)
                dfs_build_graph(node.right)
            
        dfs_build_graph(root)
        
        result = []
        visited = set()
        
        def dfs(node, d):
            if d == k:
                result.append(node.val)
                return

            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj, d+1)
        
        dfs(target, 0)
        
        return result
        
        
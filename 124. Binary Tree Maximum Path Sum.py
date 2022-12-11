class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def dfs(node):
            if not node: return 0
            nonlocal max_path

            left = dfs(node.left)
            right = dfs(node.right)

            max_path = max(max_path, node.val+right + left, node.val+left, node.val+right, node.val)

            return max(node.val + right, node.val + left, node.val)
        
        dfs(root)
        return max_path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_route = root.val
        
        def dfs(node):
            
            max_val = node.val
            left = right = float('-inf')
            if node.left:
                left = dfs(node.left)
                max_val = max(max_val, left+node.val)
            if node.right:
                right = dfs(node.right)
                max_val = max(max_val, right + node.val)
            
            nonlocal max_route
            max_route = max(max_route, max_val, left, right, left+right+node.val)
            
            return max_val
        
        dfs(root)
        
        return max_route
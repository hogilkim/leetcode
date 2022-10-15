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
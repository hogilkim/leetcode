# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def dfs(node, num_build):
            if not node.left and not node.right:
                nonlocal total_sum
                total_sum += num_build*10 + node.val
            
            if node.left:
                dfs(node.left, num_build*10 + node.val)
            if node.right:
                dfs(node.right, num_build*10 + node.val)
        
        dfs(root, 0)

        return total_sum
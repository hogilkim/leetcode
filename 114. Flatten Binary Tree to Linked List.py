# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        if not root.left and not root.right: return root
        
        
        if root.left:
            left_leaf = self.flatten(root.left)
            right_tmp = root.right
            root.right = root.left
            root.left = None
            left_leaf.right= right_tmp
        
        if root.right: 
            return self.flatten(root.right)
        
        return left_leaf
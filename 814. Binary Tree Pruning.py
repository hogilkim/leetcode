class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        
        if not root: return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and not root.val: return None
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        root.left = self.pruneTree(root.left) if root.left else None
        root.right = self.pruneTree(root.right) if root.right else None
        
        if root.left or root.right or root.val:
            return root
        else: return None
        
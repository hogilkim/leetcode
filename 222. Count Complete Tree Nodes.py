# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        l_depth = self.count_depth(root.left)
        r_depth = self.count_depth(root.right)
    
        if l_depth == r_depth:
            return pow(2, l_depth) + self.countNodes(root.right)
        else:
            return pow(2, r_depth) + self.countNodes(root.left)
    
    
    def count_depth(self, node):
        if not node: return 0
        return 1 + self.count_depth(node.left)
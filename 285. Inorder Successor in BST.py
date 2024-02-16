# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solve again
# Feb 16, 2024 285
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root: return None


        prev = None
        if p.right:
            curr = p.right
            
            while curr:
                prev = curr
                curr = curr.left
            return prev
        
        curr = root
        while curr and curr.val != p.val:
            if curr.val > p.val:
                prev = curr
                curr = curr.left
            else:
                curr = curr.right
        
        return prev
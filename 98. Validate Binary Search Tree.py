# solve again
# Second attempt - Aug 10, 2022
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor = float('-inf'), ceiling=float('inf')) -> bool:
        
        return not root or (floor<root.val<ceiling and \
                           self.isValidBST(root.left, floor, root.val) and \
                           self.isValidBST(root.right, root.val, ceiling))

# solve again
# First attempt - Jan 18, 2022
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor = float('-inf'), ceiling=float('inf')) -> bool:
        return not root or (floor < root.val < ceiling and self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling))
        
        
        
        
#         if not root: return True
        
#         if root.left:
#             if root.left.val >= root.val:
#                 return False
            
#         if root.right:
#             if root.right.val <= root.val:
#                 return False
            
#         return self.isValidBST(root.left) and self.isValidBST(root.right)
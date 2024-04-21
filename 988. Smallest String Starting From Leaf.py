# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def helper(node, curr):
            # if not node: return None
            curr = chr(node.val+97) + curr
            
            if node.left and node.right:
                return min(helper(node.left, curr), helper(node.right, curr))
            
            if node.left:
                return helper(node.left, curr)
            
            if node.right:
                return helper(node.right, curr)
            
            return curr
        
        return helper(root, "")
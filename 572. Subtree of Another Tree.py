# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot)
        
        
    def helper(self, node, subNode):
        result = self.check_subtree(node, subNode)
        if result:
            return result
        
        left_result, right_result = False, False
        if node.left:
            left_result = self.helper(node.left, subNode)
        if node.right:
            right_result = self.helper(node.right, subNode)
        return left_result or right_result
        
    def check_subtree(self, node, subNode):
        if not node and not subNode:
            return True
        elif not node:
            return False
        elif not subNode:
            return False
        elif node.val == subNode.val:
            return self.check_subtree(node.left, subNode.left) and self.check_subtree(node.right, subNode.right)
        else: #value not same
            return False
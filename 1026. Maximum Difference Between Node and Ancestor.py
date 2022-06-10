# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, minval, maxval):
            if not node: return 0
            
            
            temp = max(abs(node.val - minval), abs(node.val-maxval)) if minval < 10e5 else 0
            minval = min(minval, node.val)
            maxval = max(maxval, node.val)
            
            temp2 = max(dfs(node.left, minval, maxval),dfs(node.right,minval,maxval))
            
            return max(temp, temp2)

        return dfs(root, 10e5, -10e5)
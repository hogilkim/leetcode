# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        
        x_y = []
        
        def dfs(node, parent, depth):
            if not node: return
            if len(x_y)>=2: return
            
            if node.val == x or node.val == y:
                x_y.append((depth, parent))
            
            dfs(node.left,node.val,depth+1)
            dfs(node.right, node.val, depth+1)
        
        dfs(root,0,0)
        return x_y[0][0] == x_y[1][0] and x_y[0][1] != x_y[1][1]
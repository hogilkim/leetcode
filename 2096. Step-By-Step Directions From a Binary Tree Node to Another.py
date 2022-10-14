# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # startpath, destpath
        startpath = []
        destpath = []
        
        def dfs(node, path, val):
            if not node: return False
            
            if node.val == val:
                return True
            
            if dfs(node.left, path, val):
                path.append("L")
            elif dfs(node.right, path, val):
                path.append("R")
        
            return len(path)>0
        
        
        dfs(root, startpath, startValue)
        dfs(root, destpath, destValue)
        
        while startpath and destpath and startpath[-1] == destpath[-1]:
            startpath.pop()
            destpath.pop()
        
        return "U"*len(startpath) + "".join(reversed(destpath))
        
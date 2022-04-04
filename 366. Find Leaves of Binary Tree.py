# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(node):
            if not node: return -1
            height = max(dfs(node.left), dfs(node.right)) + 1
            if height >= len(res): res.append([])
            
            res[height].append(node.val)
            
            return height
        
        dfs(root)
        return res
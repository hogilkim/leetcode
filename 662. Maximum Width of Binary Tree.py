# solve again
# first attempt - Jan 16, 2022

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = [(root, 0, 0)]
        curr_depth = 0
        
        max_len,left = 0, 0
        
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2+1))
                
                if curr_depth < depth:
                    curr_depth = depth
                    left = pos
                
                max_len = max(max_len, pos-left+1)
        
        return max_len
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque = collections.deque([])
        
        if root: deque.append(root)
        res = []
        
        while deque:
            nodes_in_level = []
            for i in range(len(deque)):
                node = deque.popleft()
                nodes_in_level.append(node.val)
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(nodes_in_level)
        
        return res
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        res = []
        
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(curr_level)
        return res
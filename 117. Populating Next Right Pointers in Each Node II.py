# solved
# first attempt - Jan 15, 2022
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        deque = collections.deque([])
        if root: deque.append(root)
            
        while deque:
            node_num = len(deque)
            
            for i in range(node_num):
                curr = deque.popleft()
                if i < node_num-1:
                    curr.next = deque[0]
                else:
                    curr.next = None
                if curr.left: deque.append(curr.left)
                if curr.right: deque.append(curr.right)

        
        return root
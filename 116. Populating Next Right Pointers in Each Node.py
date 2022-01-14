# solved
# Jan 13, 2022 
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        deque = collections.deque([])
        if root:
            deque.append(root)
        
        while deque:
            node_num = 0
            # append children in deque
            for i in range(len(deque)):
                if deque[i].left: deque.append(deque[i].left)
                if deque[i].right: deque.append(deque[i].right)
                node_num += 1
            
            # make next poninters
            for j in range(node_num):
                curr = deque.popleft()
                if j == node_num - 1:
                    curr.next = None
                else:
                    curr.next = deque[0]
        
        return root
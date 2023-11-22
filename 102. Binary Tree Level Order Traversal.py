# Nov 22, 2023 102-3
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([])
        if root: queue.append(root)
        res = []

        while queue:
            curr_level = []
            for _ in range(len(queue)):
                
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)


                curr_level.append(node.val)
            res.append(curr_level)
        return res

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
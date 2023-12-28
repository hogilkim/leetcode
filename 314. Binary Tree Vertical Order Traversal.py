# Dec 28, 2023 314-2
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vdict = defaultdict(list)

        queue = deque([(root, 0)]) if root else deque([])

        while queue:
            node, pos = queue.popleft()
            vdict[pos].append(node.val)
            if node.left:
                queue.append((node.left, pos-1))
            if node.right:
                queue.append((node.right, pos+1))
        
        return [vdict[key] for key in sorted(vdict.keys())]

import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        vertical = defaultdict(list)
        
        deque = collections.deque([(root, 0)])
        
        while deque:
            for i in range(len(deque)):
                node, key = deque.popleft()
                if node:
                    vertical[key].append(node.val)
                    deque.append((node.left, key-1))
                    deque.append((node.right, key+1))
        
        result = []
        
        for key in sorted(vertical.keys()):
            result.append(vertical[key])
        
        return result
            
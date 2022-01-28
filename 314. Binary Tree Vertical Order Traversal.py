# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            
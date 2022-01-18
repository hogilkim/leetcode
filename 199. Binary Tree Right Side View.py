# solved
# first attempt - Jan 17, 2022
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        deque = collections.deque([])
        if root: deque.append(root)
            
        result = []
        while deque:
            result.append(deque[-1].val)
            for i in range(len(deque)):
                curr = deque.popleft()
                if curr.left: deque.append(curr.left)
                if curr.right: deque.append(curr.right)
        
        return result
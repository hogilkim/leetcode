# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dq = collections.deque([])
        if root: dq.append(root)
        direction = 1
        result = []
        while dq:
            curr_level = []

            for i in range(len(dq)):
                node = dq.popleft()
                curr_level.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            
            result.append(curr_level[::direction])
            
            direction *= -1
        
        return result


import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        deque = collections.deque([])
        if root: deque.append(root)
        direction = 1
        result = []
        while deque:
            level_vals = []
            
            for i in range(len(deque)):
                curr = deque.popleft()
                level_vals.append(curr.val)
                if curr.left: deque.append(curr.left)
                if curr.right: deque.append(curr.right)
            
            result.append(level_vals[::direction])
            direction *= -1
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        
        # bfs
#         if not root: return 0
#         queue = deque([root])
#         depth = 1
#         while queue:
            
#             for i in range(len(queue)):
#                 node = queue.popleft()
#                 if not node.left and not node.right:
#                     return depth
#                 if node.left: queue.append(node.left)
#                 if node.right: queue.append(node.right)
#             depth += 1
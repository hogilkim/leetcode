# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7

        queue = deque([root])
        allsum = 0
        while queue:
            node = queue.popleft()
            allsum += node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        max_mult = 0

        def dfs(node):
            if not node: return 0
            nonlocal max_mult
            left = dfs(node.left)
            right = dfs(node.right)
            sub_tree_sum = left+right+node.val
            max_mult = max(max_mult, (allsum - sub_tree_sum)*sub_tree_sum)

            return sub_tree_sum
        
        dfs(root)

        return max_mult%MOD



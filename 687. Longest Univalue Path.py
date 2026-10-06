# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Oct 5, 2026 687
class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        max_seq = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal max_seq

            leftres = dfs(node.left)
            rightres = dfs(node.right)

            left = right = 0
            if node.left and node.left.val == node.val:
                left = leftres
            if node.right and node.right.val == node.val:
                right = rightres
            max_seq = max(max_seq, left + right + 1)
            return max(left, right) + 1

        dfs(root)
        return max_seq - 1

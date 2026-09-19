# Sep 19, 2026 543
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_r = 0

        def dfs(node):
            if not node:
                return 0
            nonlocal max_r

            left = dfs(node.left)
            right = dfs(node.right)
            max_r = max(max_r, 1 + left + right)

            return 1 + max(left, right)

        dfs(root)

        return max_r - 1


# Nov 16, 2023
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxlen = 0

        def dfs(node):
            if not node:
                return 0

            nonlocal maxlen

            left = dfs(node.left)
            right = dfs(node.right)

            maxlen = max(maxlen, left + right)

            return max(left, right) + 1

        dfs(root)
        return maxlen


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # solve again
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.diameter

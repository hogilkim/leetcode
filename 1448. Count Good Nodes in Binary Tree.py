# Sep 25, 2026 1448
class Solution:
    def goodNodes(self, root: TreeNode, maxval=float("-inf")) -> int:
        count = 0
        new_max = maxval
        if not root:
            return 0
        if root.val >= maxval:
            count += 1
            new_max = root.val

        count += self.goodNodes(root.left, new_max) + self.goodNodes(
            root.right, new_max
        )

        return count


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_val=-1 * 10000) -> int:
        if not root:
            return 0

        ret_val = 1 if root.val >= max_val else 0

        return (
            self.goodNodes(root.left, max(root.val, max_val))
            + self.goodNodes(root.right, max(root.val, max_val))
            + ret_val
        )

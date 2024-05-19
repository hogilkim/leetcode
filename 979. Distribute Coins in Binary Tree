# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solve again
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        total_moves = 0

        def dfs(node):
            nonlocal total_moves
            left = [0, 0]
            if node.left:  left = dfs(node.left)
            right = [0, 0]
            if node.right: right = dfs(node.right)
            curr_stat = [left[0] + right[0] + node.val, left[1] + right[1] + 1]
            total_moves += abs(curr_stat[0] - curr_stat[1])
            return curr_stat
        dfs(root)
        return total_moves
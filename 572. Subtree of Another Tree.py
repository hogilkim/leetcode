# Sep 21, 2026 572-2


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def check_subtree(node, subRoot):
            if not node and not subRoot:
                return True
            if (not node and subRoot) or (node and not subRoot):
                return False
            curr_res = node.val == subRoot.val
            if not curr_res:
                return False
            left = check_subtree(node.left, subRoot.left)
            right = check_subtree(node.right, subRoot.right)

            return curr_res and left and right

        def dfs(node, subRoot):
            if not node:
                return False
            res = check_subtree(node, subRoot)
            if res:
                return res

            left = dfs(node.left, subRoot)
            right = dfs(node.right, subRoot)
            return left or right

        return dfs(root, subRoot)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.helper(root, subRoot)

    def helper(self, node, subNode):
        result = self.check_subtree(node, subNode)
        if result:
            return result

        left_result, right_result = False, False
        if node.left:
            left_result = self.helper(node.left, subNode)
        if node.right:
            right_result = self.helper(node.right, subNode)
        return left_result or right_result

    def check_subtree(self, node, subNode):
        if not node and not subNode:
            return True
        elif not node:
            return False
        elif not subNode:
            return False
        elif node.val == subNode.val:
            return self.check_subtree(node.left, subNode.left) and self.check_subtree(
                node.right, subNode.right
            )
        else:  # value not same
            return False

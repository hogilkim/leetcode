# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Oct 6, 2026 1110-2
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        subtrees = []
        to_delete = set(to_delete)

        def dfs(node, prev, new_root_bool, left, right):
            if not node:
                return

            if node.val in to_delete:
                if prev and left:
                    prev.left = None
                if prev and right:
                    prev.right = None

                dfs(node.left, node, True, True, False)
                dfs(node.right, node, True, False, True)
                return
            if new_root_bool:
                subtrees.append(node)
            dfs(node.left, node, False, True, False)
            dfs(node.right, node, False, False, True)

        dfs(root, None, True, False, False)
        return subtrees


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def dfs(node, prev, new_root_bool, left, right):
            if not node:
                return

            if node.val in to_delete:
                if prev and left:
                    prev.left = None
                if prev and right:
                    prev.right = None

                dfs(node.left, None, True, True, False)
                dfs(node.right, None, True, False, True)

                return

            elif new_root_bool:
                res.append(node)

            dfs(node.left, node, False, True, False)
            dfs(node.right, node, False, False, True)

        dfs(root, None, True, False, False)
        return res

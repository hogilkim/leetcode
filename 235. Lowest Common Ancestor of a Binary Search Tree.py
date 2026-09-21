# Sep 21, 2026 235-4
# solve again.
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if p.val > q.val:
            p, q = q, p

        while root:
            if root.val < p.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
            else:
                return root

        return root

        # lca = None

        # def dfs(node, p, q):
        #     if not node: return False
        #     nonlocal lca
        #     left = dfs(node.left, p, q)
        #     right = dfs(node.right, p, q)

        #     found = node==p or node==q
        #     is_lca = (left and right) or (left and found) or (right and found)
        #     if is_lca:
        #         lca = node
        #     # print(node.val, found or left or right)
        #     return found or left or right

        # dfs(root,p,q)

        # return lca


# Nov 9, 2023 solve again. third trial
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val < q.val:
            p, q = q, p
        while root:
            if root.val > p.val:
                root = root.left
            elif root.val < q.val:
                root = root.right
            else:
                return root

        # if not root: return None
        # if root == p or root == q: return root
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right: return root
        # if left: return left
        # if right: return right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None:
            return root

        if left != None:
            return left
        if right != None:
            return right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

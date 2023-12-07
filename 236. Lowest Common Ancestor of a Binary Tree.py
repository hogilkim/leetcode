# Third Dec 7, 2023 236-3

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: return root
        return left or right
        
        # res = None
        # def dfs(node):
        #     nonlocal res
        #     if not node: return False

        #     left = dfs(node.left)
        #     right = dfs(node.right)

        #     if left and right: res = node
        #     if (left or right) and (node == p or node == q): res = node

        #     return left or right or node == p or node == q
        
        # dfs(root)

        # return res

# Second: July 25, 2022
# Solve again

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if root == p or root==q: return root
        
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: return root
        
        return left or right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# first attempt: Jan 11, 2022
# solve again 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        
        left = right = None
        
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
            
        
        if left and right:
            return root
        
        else:
            return left or right
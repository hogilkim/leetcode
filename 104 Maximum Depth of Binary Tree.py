# Nov 16, 2023 104-3
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ** Solved Again Dec 25
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def maxDepth(self, root):
#         depth = traverse(root, 0)
#         return depth

        
# def traverse (object, depth):
#     if object == None:
#         return depth
#     left_node = object.left
#     right_node = object.right
#     return max(traverse(left_node, depth+1), traverse(right_node, depth+1))
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right: return [root.val]
        def boundary(node, arr, is_right):
            if not node or (not node.left and not node.right): return
            # if not node.left and not node.right: 
            #     return
            arr.append(node.val)
            
            if not is_right:
                if node.left:
                    boundary(node.left, arr, is_right)
                else:
                    boundary(node.right, arr, is_right)
            
            elif is_right:
                if node.right:
                    boundary(node.right, arr, is_right)
                else:
                    boundary(node.left, arr, is_right)
            
            
        
        def findleaves(node, arr):
            if not node.left and not node.right:
                arr.append(node.val)
                return
            
            if node.left: findleaves(node.left, arr)
            if node.right: findleaves(node.right, arr)
        
        
        
        left_boundary = []
        boundary(root.left, left_boundary, 0)
        right_boundary = []
        boundary(root.right, right_boundary, 1)
        leaves = []
        findleaves(root, leaves)
        
        return [root.val] + left_boundary + leaves + list(reversed(right_boundary))
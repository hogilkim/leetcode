# solve again
# second attempt - Jan 15, 2022
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder: return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        pivot = inorder.index(root_val)
        
        root.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])
        
        
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # INORDER & PREORDER are not bfs and dfs! 
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
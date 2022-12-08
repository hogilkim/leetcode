# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leaves = [[],[]]

        def dfs(node, rootnum):
            if not node: return
            if not node.left and not node.right: 
                leaves[rootnum].append(node.val)

            dfs(node.left, rootnum)
            dfs(node.right, rootnum)

        
        dfs(root1, 0)
        dfs(root2, 1)

        return leaves[0]==leaves[1]
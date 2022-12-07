#2
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        if root.val > high: return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        if root.val > high: return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)
        
        
#         def dfs(node):
#             if not node:
#                 return 0
            
#             total_sum = 0
            
#             if low<=node.val<=high:
#                 total_sum += node.val
            
#             total_sum += dfs(node.left) + dfs(node.right)
            
#             return total_sum
        
#         return dfs(root)
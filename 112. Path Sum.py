# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curr_node, total_sum):
            if not curr_node:
                return False
            total_sum += curr_node.val
            print(total_sum)
            if total_sum == targetSum:
                if not curr_node.left and not curr_node.right:
                    return True
            return dfs(curr_node.left, total_sum) or dfs(curr_node.right, total_sum)
            
        return dfs(root, 0)
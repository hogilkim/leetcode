# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            # return: max_bst_size_from_left_or_right_or_sum, sum_up, min_val, max_val
            if not node: return 0, 0, float('inf'), float('-inf')
            
            N1, n1, min_val1, max_val1 = dfs(node.left)
            N2, n2, min_val2, max_val2 = dfs(node.right)
            
            n = n1+n2+1 if max_val1 < node.val < min_val2 else float('-inf')
            
            return max(N1,N2,n), n, min(node.val, min_val1), max(node.val, max_val2)
        
        
        return dfs(root)[0]
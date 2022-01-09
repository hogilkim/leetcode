#solve again 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = {}
        self.counter = 0
        
        def dfs(curr_sum, node):
            if not node: return
            curr_sum += node.val
            if curr_sum == targetSum: self.counter += 1
            
            want_to_exclude = curr_sum - targetSum
            self.counter += cache.get(want_to_exclude, 0)
            
            cache[curr_sum] = cache.get(curr_sum, 0) + 1
            dfs(curr_sum, node.left)
            dfs(curr_sum, node.right)
            
            cache[curr_sum] -= 1
        
        dfs(0, root)
        return self.counter
        
        # wrong answer. 
#         self.paths = 0
        
#         def dfs(part_sum, node):
#             if not node: return
            
#             if part_sum == targetSum:
#                 self.paths+= 1
            
#             if node.left: 
#                 dfs(part_sum +node.left.val, node.left)
#                 dfs(node.left.val, node.left)
#             if node.right:
#                 dfs(part_sum + node.right.val, node.right)
#                 dfs(node.right.val, node.right)
            
            
        
#         dfs(root.val, root)
#         return self.paths
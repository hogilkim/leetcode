# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(part, curr):
            if not curr: return
            
            part.append(curr.val)
            path_sum = sum(part)
            
            if (not curr.left) and (not curr.right) and (path_sum == targetSum):
                res.append(part.copy())
            else:            
                dfs(part, curr.left)
                dfs(part, curr.right)
            part.pop()
        
        dfs([],root)
        
        return res
            
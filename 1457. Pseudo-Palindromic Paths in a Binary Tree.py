# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # set elements == 0: all even 
        # set elements == 1: all even except one
        # set elements >=2 : cannot be palindrome
        
        elements = set()
        
        def dfs(node):
            if not node: return 0
            
            # modify set
            if node.val not in elements: elements.add(node.val)
            else: elements.remove(node.val)
                
            if not node.left and not node.right:
                return_val = 1 if len(elements)<=1 else 0
            else:
                return_val = dfs(node.left) + dfs(node.right)
            
            # UNDO the modification from the above for other dfs
            if node.val not in elements: elements.add(node.val)
            else: elements.remove(node.val)
            
            return return_val
            
        
        return dfs(root)
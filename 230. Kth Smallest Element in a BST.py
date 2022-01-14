# solve again
# second attempt - Jan 13, 2022

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        n = 0 
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
        



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        return sorted(self.helper(root, []))[k-1]
    
    def helper(self, node, num_list):
        if node:
            num_list.append(node.val)
            if node.left:
                num_list += self.helper(node.left, [])
            if node.right:
                num_list += self.helper(node.right, [])
        return num_list
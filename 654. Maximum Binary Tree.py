# solved
# first attempt - Jan 15, 2022
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums: return None
        
        max_num = max(nums)
        pivot = nums.index(max_num)
        
        
        root = TreeNode(max_num)
        
        root.left = self.constructMaximumBinaryTree(nums[:pivot])
        root.right = self.constructMaximumBinaryTree(nums[pivot+1:])
        
        return root
# solve again

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        
        def dfs(node):
            if not node: return collections.Counter()
            if not node.left and not node.right: return collections.Counter([0])
            
            left_count = dfs(node.left)
            right_count = dfs(node.right)
            
            for left_distance, left_leaves in left_count.items():
                for right_distance, right_leaves in right_count.items():
                    if left_distance + right_distance + 2 <= distance: self.count += left_leaves*\
                        right_leaves
            
            return Counter({k+1:v for k,v in (left_count + right_count).items()})
        
        dfs(root)
        
        return self.count
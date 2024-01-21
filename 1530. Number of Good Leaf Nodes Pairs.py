# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    # Solve again Jan 20, 2024 1530-2
    def countPairs(self, root: TreeNode, distance: int) -> int:
        good_pairs = 0
        # key: distance val: # of leave nodes

        def dfs(node):
            if not node: return Counter()
            if not node.left and not node.right: return Counter({0:1})

            counter_left = dfs(node.left)
            counter_right = dfs(node.right)
            nonlocal good_pairs

            for distance_left, left_leave_num in counter_left.items():
                for distance_right, right_leave_num in counter_right.items():
                    if distance_left + distance_right + 2 <= distance:
                        good_pairs += left_leave_num * right_leave_num
            
            return Counter({distance+1: leaf_num for distance, leaf_num in (counter_left + counter_right).items()})
        
        dfs(root)
        return good_pairs


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
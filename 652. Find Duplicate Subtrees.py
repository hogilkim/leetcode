# solve again Jan 22, 2024 652

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        patterns = defaultdict(int)
        output = []

        def dfs(node):
            if not node: return "#"
            if not node.left and not node.right:
                patterns[str(node.val)] += 1
                if patterns[str(node.val)] == 2: output.append(node)
                return str(node.val)
            
            string = str(node.val)
            string += 'l' + dfs(node.left)
            string += 'r' + dfs(node.right)
            
            patterns[string] += 1
            if patterns[string] == 2: output.append(node)
            return string

        dfs(root)

        return output
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # bfs solution
        queue = deque([root])
        result = []
        
        while queue:
            this_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                this_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(sum(this_level)/len(this_level))
        return result
        
        
        # dfs solution
#         level_map = {}
        
        
#         def dfs(node, level):
#             if not node: return
            
#             if level not in level_map:
#                 level_map[level] = [node.val]
#             else: level_map[level].append(node.val)
#             dfs(node.left, level+1)
#             dfs(node.right, level+1)
            
#         dfs(root, 0)
#         result = []
        
#         i = 0
        
#         while i in level_map:
#             result.append( sum(level_map[i])/len(level_map[i] ))
#             i += 1
#         return result
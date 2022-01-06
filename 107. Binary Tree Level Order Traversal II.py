# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        node_queue = collections.deque([root])
        res = []
        
        while node_queue:
            
            nodes_in_level = []
            
            for i in range(len(node_queue)):
                curr = node_queue.popleft()
                nodes_in_level.append(curr.val)
                if curr.left: node_queue.append(curr.left)
                if curr.right: node_queue.append(curr.right)
            
            res.append(nodes_in_level)
        
        return reversed(res)
                
            
        
        
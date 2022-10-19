# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node, prev_val, sequence):
            if not node:
                return sequence
            
            curr_sequence = 0
            
            if prev_val + 1 == node.val:
                sequence += 1
                curr_sequence = sequence
            else:
                curr_sequence = 1
            
            left = dfs(node.left, node.val, curr_sequence)
            right = dfs(node.right, node.val, curr_sequence)
            
            # return max seqeunce btw sequence, left, right
            return max(sequence, left, right)
        
        return dfs(root, 0, 0)
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # bfs
        bfs_queue = collections.deque([(root, 1)])
        max_seq = 0
        
        while bfs_queue:
            for _ in range(len(bfs_queue)):
                node, count = bfs_queue.popleft()
                max_seq = max(max_seq, count)
                
                if node.left:
                    bfs_queue.append((node.left, count+1 if node.left.val == node.val+1 else 1))
                if node.right:
                    bfs_queue.append((node.right, count+1 if node.right.val == node.val+1 else 1))
                
        
        return max_seq
        
        # dfs
#         max_seq = 0
        
#         def dfs(node, prev, seq):
#             nonlocal max_seq
            
#             if not node: return
            
#             if node.val == prev+1:
#                 seq += 1
#             else:
#                 seq = 1
            
#             max_seq = max(max_seq, seq)
            
            
#             dfs(node.left, node.val, seq)
#             dfs(node.right, node.val, seq)
            
        
#         dfs(root, root.val, 1)
        
#         return max_seq
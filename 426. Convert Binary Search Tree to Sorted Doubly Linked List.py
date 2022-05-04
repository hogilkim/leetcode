"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
import collections
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # discussion solution
        
        def traverse_double_list(node):
            if not node: return None, None
            lh, lt = traverse_double_list(node.left)
            if lt:
                lt.right = node
                node.left = lt
            rh, rt = traverse_double_list(node.right)
            if rh:
                node.right = rh
                rh.left = node
            
            return (lh or node), (rt or node)
        if not root: return None
        head,tail = traverse_double_list(root)
        
        head.left = tail
        tail.right = head
        return head
        
#        my solution
#         queue = collections.deque([])
#         if not root: return None
        
#         def dfs(node):
#             if not node: return
#             dfs(node.left)
#             queue.append(node.val)
#             dfs(node.right)
#             return
    
#         dfs(root)
#         head = curr = Node(queue.popleft())
#         if not queue:
#             head.right = head.left = head
#             return head
#         last = Node(queue.pop())
        
#         for val in queue:
#             curr.right = Node(val)
#             prev = curr
#             curr = curr.right
#             curr.left = prev
#         curr.right = last
#         last.left = curr
#         last.right = head
#         head.left = last
        
        
#         return head
            
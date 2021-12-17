"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#solve again
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       # hash map approach
        old_to_new = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            new = old_to_new[curr]
            new.next = old_to_new[curr.next]
            new.random = old_to_new[curr.random]
            curr= curr.next
        return old_to_new[head]
    
    # wrong approach
#         old_nodes, new_nodes = [], []
        
#         curr = head
#         new_node = Node(curr.val)
#         new_nodes.append(new_node)
#         old_nodes.append(curr)
#         curr = curr.next
#         old_nodes[0].next = new_nodes[0]
        
        
#         while curr:
#             old_nodes.append(curr)
#             new_node.next = Node(curr.val)
#             new_node = new_node.next
#             new_nodes.append(new_node)
#             old_nodes[-1].next = new_nodes[-1]
#             curr = curr.next
        
#         for i in range(len(new_nodes)):
#             new_nodes[i].random = old_nodes[i].random.next
        
        # return new_nodes[0]
            
        
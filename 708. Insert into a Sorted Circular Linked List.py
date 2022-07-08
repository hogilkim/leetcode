"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)
        if not head:
            insertNode.next = insertNode
            return insertNode
            
        front, back = head.next, head
        
        while front!= head:
            if back.val <= insertVal <= front.val:
                break
            if back.val > front.val and (insertVal > back.val or insertVal < front.val):
                break
            front, back = front.next, back.next
        
        back.next = insertNode
        insertNode.next = front
        return head
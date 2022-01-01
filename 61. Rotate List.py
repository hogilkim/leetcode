# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        curr = head
        node_num = 1
        while curr.next:
            node_num += 1
            curr = curr.next
        curr.next = head
        
        k = k % node_num
        
        end_num = node_num - k
        
        i = 1
        while i <= end_num:
            curr = curr.next
            i+=1
        new_head = curr.next
        curr.next = None
        return new_head
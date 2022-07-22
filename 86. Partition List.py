# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        sub_head = head
        sub_prev = dummy = ListNode(0, head)
        
        while sub_head and sub_head.val < x:
            sub_head = sub_head.next
            sub_prev = sub_prev.next
        
        curr = sub_head
        prev = sub_prev
        
        while curr:
            if curr.val < x:
                tmp_next = curr.next
                sub_prev.next = curr
                curr.next = sub_head
                sub_prev = sub_prev.next
                
                prev.next = tmp_next
                curr = tmp_next
            else:
                curr = curr.next
                prev = prev.next
        
        return dummy.next
            
        
        
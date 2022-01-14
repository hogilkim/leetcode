# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        even_start = head.next
        
        curr = head
        while curr and curr.next:
            odd = curr
            even = curr.next
            odd_next = curr.next.next
            if odd_next:
                even_next = curr.next.next.next
            else:
                even_next = None
            
            odd.next = odd_next
            even.next = even_next
            
            prev = curr
            curr = odd_next
            
        if curr:
            curr.next = even_start
        
        else:
            prev.next = even_start
        
        return head
        
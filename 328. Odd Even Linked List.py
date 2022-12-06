# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        curr = head
        even = curr.next
        even_start = even
        odd = curr
        curr = curr.next.next
        while curr and curr.next:
            odd.next = curr
            curr = curr.next
            even.next = curr
            curr = curr.next
            odd = odd.next
            even = even.next
        
        if curr:
            odd.next = curr
            odd = odd.next
        
        odd.next = even_start
        even.next = None

        return head

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
        
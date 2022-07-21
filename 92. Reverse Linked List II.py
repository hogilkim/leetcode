# 2nd attempt: July 20, 2022
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        
        i = 1
        sub_prev = ListNode(0,head)
        sub_tail = sub_head = head
        
        while i < left:
            sub_prev = sub_prev.next
            sub_tail = sub_tail.next
            sub_head = sub_head.next
            i+=1
        while i < right:
            sub_tail = sub_tail.next
            i+=1
        sub_next = sub_tail.next
        
        # reverse sub linked list
        
        prev, curr, nxt = None, sub_head, sub_head.next
        
        while curr != sub_next:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next if curr else None
        
        sub_prev.next = sub_tail
        sub_head.next = sub_next
        
        return head if left > 1 else sub_tail 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        i = 1
        sub_prev = ListNode() # dummy
        sub_prev.next = head
        
        sub_head, sub_tail = head, head
        
        while i < left:
            sub_prev = sub_prev.next
            sub_head = sub_head.next
            sub_tail = sub_tail.next
            i += 1
            #1
            
        while i < right:
            sub_tail = sub_tail.next
            i += 1
            
            #5
        sub_next = sub_tail.next if sub_tail else None
    
        
        prev, curr, nxt = None, sub_head, sub_head.next
        
        while curr != sub_next:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next if curr else None
        
        sub_prev.next = sub_tail
        sub_head.next = sub_next
        return head if left>1 else sub_tail
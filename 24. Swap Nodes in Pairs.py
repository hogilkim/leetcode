# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        new_start = head.next
        
        curr = head
        prev = None
        while curr and curr.next:
            next_pair = curr.next.next
            
            temp = curr.next
            temp.next = curr
            curr.next = next_pair
            if prev: prev.next = temp
            
            prev = curr
            curr = next_pair
        
        
        return new_start
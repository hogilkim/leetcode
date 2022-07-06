# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        curr, prev = slow, None
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        tail = prev
        
        max_val = 0
        while tail:
            max_val = max(max_val, tail.val + head.val)
            head, tail = head.next, tail.next
            
            
        
        return max_val
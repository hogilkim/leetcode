# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        count, curr = 0, head
        
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count<k: return head
        
        new_head, prev = self.reverse(head, k)
        head.next = self.reverseKGroup(new_head,k)
        
        return prev
    
    def reverse(self, head, count):
        
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
            
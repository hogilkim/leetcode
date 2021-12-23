# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solve again
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return True
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
       
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        
        left_half, right_half = head, prev
        
        while right_half:
            if left_half.val != right_half.val:
                return False
            left_half, right_half = left_half.next, right_half.next
            
        return True
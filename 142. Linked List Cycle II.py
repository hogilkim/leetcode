# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time O(n) space O(1), solve again
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else: return None # while else clause!
        
        while head != slow:
            head = head.next
            slow = slow.next
            
        return slow
        
        # time O(n) space O(n)
        # visited = set()
        # while head:
        #     if head in visited: return head
        #     visited.add(head)
        #     head = head.next
        # return None
    
    
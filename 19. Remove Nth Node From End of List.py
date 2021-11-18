# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head
        
        count = 0
        while right:
            if count < n:
                right = right.next
                count += 1
            else:
                right = right.next
                left = left.next
        
        left.next = left.next.next
        return dummy.next
            
            
#         if not head.next:
#             return None
#         curr = head
#         node_num = 0
#         while curr:
#             curr = curr.next
#             node_num += 1
        
#         curr = head
#         from_beginning = node_num - n
        
#         n = 0
#         if from_beginning == n:
#             return head.next
#         prev=None
#         while n < from_beginning:
#             prev = curr
#             curr = curr.next
#             n+=1
#         prev.next = curr.next
#         return head
        
            
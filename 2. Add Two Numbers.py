# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # second solution
        dummy = ListNode()
        curr = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            value = v1 + v2 + carry
            carry = value//10
            value = value %10
            
            curr.next = ListNode(value)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
        
        
#         result = []
#         while l1 and l2:
#             result.append(l1.val + l2.val)
#             l1 = l1.next
#             l2 = l2.next
            
#         while l1:
#             result.append(l1.val)
#             l1 = l1.next
            
#         while l2:
#             result.append(l2.val)
#             l2 = l2.next
        
#         for i in range(len(result)-1):
#             if result[i] > 9:
#                 result[i] -= 10
#                 result[i+1] += 1
        
#         if result[-1] > 9:
#             result[-1] -= 10
#             result.append(1)
            
#         dummy = ListNode()
#         root = dummy
#         print(result)
        
#         for num in result:
#             root.next = ListNode(num)
#             root = root.next
#         return dummy.next
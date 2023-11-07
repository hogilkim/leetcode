# solve again
# Nov 6, 2023 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        head = dummy

        while list1 or list2:
            if not list1:
                head.next = list2
                list2 = list2.next
            elif not list2:
                head.next = list1
                list1 = list1.next
            
            elif list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            
            else:
                head.next = list1
                list1 = list1.next

            head = head.next
            
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        while l1 or l2:
            if not l1:
                head.next = l2
                l2 = l2.next
            elif not l2:
                head.next = l1
                l1 = l1.next
            
            elif l1.val> l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        return dummy.next
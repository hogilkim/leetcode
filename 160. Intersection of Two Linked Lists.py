# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        
        while currA or currB:
            if currA: currA = currA.next
            else: headB = headB.next
            if currB: currB = currB.next
            else: headA = headA.next
        
        
        while headA is not headB:
            headA = headA.next
            headB = headB.next
            
        return headA
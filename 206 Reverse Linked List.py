# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
           
        return prev
        
        
#         node_list = []
#         curr = head
#         if head == None:
#             return head
#         while (curr != None):
#             node_list.append(curr)
#             curr = curr.next
        
#         new_head = node_list.pop()
#         curr2 = new_head
#         while len(node_list) > 0:
#             curr2.next = node_list.pop()
#             curr2 = curr2.next
#         curr2.next = None
#         return new_head
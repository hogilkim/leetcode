# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_lists = []
        curr_node = head
        while curr_node:
            node_lists.append(curr_node)
            curr_node = curr_node.next
        
        added = set()
        l = 0 
        r = len(node_lists)-1
        
        dummy = ListNode(0)
        
        while l <= r:
            dummy.next = node_lists[l]
            dummy = dummy.next
            dummy.next = node_lists[r]
            dummy = dummy.next
            l += 1
            r -= 1
        dummy.next = None

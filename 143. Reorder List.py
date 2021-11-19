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
        
        # second solution
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        second_half_ptr = slow.next
        second_half_ptr_prev = slow.next = None
        while second_half_ptr:
            temp = second_half_ptr.next
            second_half_ptr.next = second_half_ptr_prev
            second_half_ptr_prev = second_half_ptr
            second_half_ptr = temp
        
        right_node = second_half_ptr_prev
        left_node = head
        while right_node:
            right_next = right_node.next
            left_next = left_node.next
            left_node.next = right_node
            right_node.next = left_next
            right_node, left_node = right_next, left_next
                    
        #first solution
#         node_lists = []
#         curr_node = head
#         while curr_node:
#             node_lists.append(curr_node)
#             curr_node = curr_node.next
        
#         added = set()
#         l = 0 
#         r = len(node_lists)-1
        
#         dummy = ListNode(0)
        
#         while l <= r:
#             dummy.next = node_lists[l]
#             dummy = dummy.next
#             dummy.next = node_lists[r]
#             dummy = dummy.next
#             l += 1
#             r -= 1
#         dummy.next = None

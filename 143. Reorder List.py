# Sep 20, 2026 143-3
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #   s f
        # 1 2 3 4

        #     s   f
        # 1 2 3 4 5

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # if fast.next:
        #     fast = fast.next
        latter_head = slow.next

        # reverse second half
        # 3 4 5
        # p h
        prev = None
        slow.next = None
        while latter_head:
            print(latter_head.val)
            nxt = latter_head.next
            latter_head.next = prev
            prev = latter_head
            latter_head = nxt

        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next

            first = first_next
            second = second_next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# solved - second attempt Jan 12, 2022
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# memorize fast = head.next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        return head


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

        # first solution


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

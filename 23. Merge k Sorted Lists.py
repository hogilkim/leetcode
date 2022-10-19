# Third time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # declare min_heap
        # put first items of each array into min_heap (item, idx_of_array)
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                min_heap.append((lists[i].val,i))
                
                
        heapq.heapify(min_heap)
        
        dummy = head = ListNode()
        
        while min_heap:
            # pop from min_heap
            _, idx = heapq.heappop(min_heap)
            
            # store it into result array
            head.next = lists[idx]
            head = head.next
            
            # get item from idx_of_array if next ListNode is not Null
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(min_heap, (lists[idx].val, idx))
                
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# second attempt - solved
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                min_heap.append([lists[i].val, i])
            
        heapq.heapify(min_heap)
        
        
        dummy = curr = ListNode()
        while min_heap:
            _, index = heapq.heappop(min_heap)
            node = lists[index]
            if lists[index].next:
                lists[index] = lists[index].next
                heapq.heappush(min_heap, [lists[index].val, index])
            curr.next = node
            curr = curr.next
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self.merge(list1, list2))
            lists = merged_list
                
        return lists[0]
    
    def merge(self, l1, l2):
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return dummy.next
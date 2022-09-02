import collections
import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
# Deque solution | Time: O(n) | Space: O(n)
        max_len = 0
        
        # num, idx
        max_dq = collections.deque([])
        min_dq = collections.deque([])
        
        l = 0
        
        for r, num in enumerate(nums):
            while max_dq and num >= max_dq[-1][0]: max_dq.pop()
            while min_dq and num <= min_dq[-1][0]: min_dq.pop()
            max_dq.append([num,r]); min_dq.append([num,r]);
            
            
            # we don't have to do this: --------------------------------------------------
            # while max_dq and min_dq and max_dq[0][0] - min_dq[0][0] > limit:
            #     l += 1
            #     while max_dq and l > max_dq[0][1]: max_dq.popleft()
            #     while min_dq and l > min_dq[0][1]: min_dq.popleft()
            
            # because the elements coming after min_dq[0] or max_dq[0] always have higher
            # idx
            # example: limit: 9
            # nums: 10 1 2 3 4 5 11
            # ---------------------------------------------------------------------------
            
            # this while statement will be operated when new "num" comes at max_dq[0] or min_dq[0]
            while max_dq[0][0] - min_dq[0][0] > limit:
                l += 1
                if max_dq[0][1] < l: max_dq.popleft()
                if min_dq[0][1] < l: min_dq.popleft()
            max_len = max(r-l+1, max_len)
        
        return max_len

# Heap solution | Time: O(n*logn) | Space: O(n)
    
        max_len = 0
        max_heap, min_heap = [],[]
        heapq.heapify(max_heap), heapq.heapify(min_heap)
        l = 0
        
        for r, num in enumerate(nums):
            heapq.heappush(max_heap, (-num,r))
            heapq.heappush(min_heap, (num,r))
            
            while -max_heap[0][0] - min_heap[0][0] > limit:
                l += 1
                while max_heap[0][1] < l: heapq.heappop(max_heap)
                while min_heap[0][1] < l: heapq.heappop(min_heap)
            
            max_len = max(max_len, r-l+1)
        
        return max_len
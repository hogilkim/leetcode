import collections
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
                
        events = sorted(events, key = lambda x:x[0])
        events = collections.deque(events)
        min_heap = []
        heapq.heapify(min_heap)
        day = res = 0
        while events or min_heap:
            if not min_heap: day = events[0][0]
            while events and events[0][0] <= day:
                heapq.heappush(min_heap, events.popleft()[1])
            
            # Wrong!
            # while min_heap and day <= min_heap[0]:
            #     heapq.heappop(min_heap)
            #     day += 1
            #     res += 1
            heapq.heappop(min_heap)
            day += 1
            res += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
        
        
        return res
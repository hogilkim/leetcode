import heapq
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        min_heap = []
        
        heapq.heapify(min_heap)
        
        for start, end in intervals:
            heapq.heappush(min_heap, (start, -end))
        
        
        start, end = heapq.heappop(min_heap)
        res = [(start,-end)]
        
        while min_heap:
            start, end = heapq.heappop(min_heap)
            end *= -1
            
            if start >= res[-1][0] and end <= res[-1][1]:
                continue
            else: res.append((start,end))
    
        return len(res)
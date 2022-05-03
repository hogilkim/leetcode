"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        min_heap = []
        heapq.heapify(min_heap)
        
        for s in schedule:
            for interval in s:
                
                heapq.heappush(min_heap, [interval.start, interval.end])
                
        
        res_complement = []
        res_complement.append(heapq.heappop(min_heap))
        while min_heap:
            start, end = heapq.heappop(min_heap)
            
            if start > res_complement[-1][1]:
                res_complement.append([start,end])
            elif end > res_complement[-1][1]:
                res_complement[-1][1] = end
        
        
        res = []
        for i in range(len(res_complement)-1):
            res.append(Interval(res_complement[i][1], res_complement[i+1][0]))
        return res
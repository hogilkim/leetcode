import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        max_heap = []
        heapq.heapify(max_heap)
        total_time = 0
        
        for t, endt in sorted(courses, key=lambda x:x[1]):
            total_time += t
            heapq.heappush(max_heap, -t)
            if total_time > endt:
                total_time += heapq.heappop(max_heap)
                
        
        return len(max_heap)
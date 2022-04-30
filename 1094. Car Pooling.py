import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x:x[2])
        trips = sorted(trips, key=lambda x:x[1])
        num = 0
        
        min_end_heap = []
        heapq.heapify(min_end_heap)
        
        
        for p, beg, end in trips:
            while min_end_heap and min_end_heap[0][0] <= beg:
                
                e, b, drop = heapq.heappop(min_end_heap)
                num -= drop
            
            num += p
            if num > capacity: return False
            
            heapq.heappush(min_end_heap, (end, beg, p))
        
        
        return True
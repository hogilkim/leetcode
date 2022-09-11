import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed_sum = 0
        
        # stores speed
        min_heap = []
        heapq.heapify(min_heap)
        
        max_performance = 0
        
        for e,s in sorted(zip(efficiency, speed), key=lambda x:x[0], reverse=True):
            speed_sum += s
            heapq.heappush(min_heap, s)
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            max_performance = max(max_performance, speed_sum * e)
        
        return max_performance % (10**9+7)
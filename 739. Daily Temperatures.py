import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        min_heap = []
        
        res = [0] * len(temperatures)
        
        heapq.heapify(min_heap)
        
        for idx, temp in enumerate(temperatures):
            while min_heap and min_heap[0][0] < temp:
                popped_temp, popped_idx = heapq.heappop(min_heap)
                res[popped_idx] = idx - popped_idx
            
            heapq.heappush(min_heap, (temp, idx))
        
        return res
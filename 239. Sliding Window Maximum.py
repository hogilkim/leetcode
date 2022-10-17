import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        heapq.heapify(max_heap)
        
        for idx, num in enumerate(nums):
            
            heapq.heappush(max_heap, (-num, idx))
            
            while max_heap[0][1] < idx - (k-1):
                heapq.heappop(max_heap)
            if len(max_heap) >= k:
                res.append(-max_heap[0][0])
        
        return res
    
    
    # k = 2 idx = 2
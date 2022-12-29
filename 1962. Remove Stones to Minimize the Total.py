import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for num in piles:
            heapq.heappush(max_heap, -num)
        
        while k:
            popped = -heapq.heappop(max_heap)

            heapq.heappush(max_heap, -(popped-popped//2) )
            k -= 1
        
        return -sum(max_heap)
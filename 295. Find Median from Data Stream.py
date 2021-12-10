# Heap!
# Solve again

class MedianFinder:

    def __init__(self):
        self.small_heap, self.large_heap = [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -1* num)
        
        if (self.small_heap and self.large_heap and 
            (-1*self.small_heap[0]) > self.large_heap[0]):
                heapq.heappush(self.large_heap, -1*heapq.heappop(self.small_heap))
        
        if (len(self.small_heap) > len(self.large_heap) + 1):
            heapq.heappush(self.large_heap, -1*heapq.heappop(self.small_heap))
            
        if (len(self.large_heap) > len(self.small_heap) + 1):
            heapq.heappush(self.small_heap, -1*heapq.heappop(self.large_heap))
        
    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (self.large_heap[0] + -1*self.small_heap[0])/2
        elif len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        else:
            return self.large_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# Third Dec 26, 2023 295-3
class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        idx = self.bisect_left(num)
        self.nums = self.nums[:idx] + [num] + self.nums[idx:]
        
    def findMedian(self) -> float:
        if len(self.nums)%2: return self.nums[len(self.nums)//2]
        return ( self.nums[len(self.nums)//2] + self.nums[len(self.nums)//2-1] ) / 2
    
    def bisect_left(self, num):
        l, r = 0, len(self.nums)
        
        while l < r:
            mid = (l+r)//2

            if self.nums[mid] < num:
                l = mid + 1
            
            else: r = mid

        return l

# second Nov 12 2022
import heapq
class MedianFinder:

    def __init__(self):
        self.small_half = []
        self.large_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half, -1*num)
        
        if self.small_half and self.large_half and -1*self.small_half[0] > self.large_half[0]:
            heapq.heappush(self.large_half, -1*heapq.heappop(self.small_half))
        
        if len(self.small_half) > len(self.large_half) + 1:
            heapq.heappush(self.large_half, -1*heapq.heappop(self.small_half))
        
        elif len(self.small_half) < len(self.large_half):
            heapq.heappush(self.small_half, -1*heapq.heappop(self.large_half))

    def findMedian(self) -> float:
        if len(self.small_half) == len(self.large_half):
            
            return (-self.small_half[0]+self.large_half[0])/2
        else:
            return -self.small_half[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

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
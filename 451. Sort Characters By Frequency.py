from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        max_heap = []
        heapq.heapify(max_heap)
        
        for key, val in counter.items():
            heapq.heappush(max_heap, (-val, key))
        
        res = ""
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            
            res += (-freq)*char
        
        return res
# first attempt - Jan 11
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        
        counter = collections.Counter(s)
        
        min_heap = []
        
        for key in counter.keys():
            min_heap.append( [ -counter[key], key ] )
        
        heapq.heapify(min_heap)
        
        result = ""
        
        while min_heap:
            frequency, char = heapq.heappop(min_heap)
            
            for i in range(-1*frequency):
                result += char
        
        return result
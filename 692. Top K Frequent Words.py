import heapq
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        
        max_heap = []
        
        for key, val in counter.items():
            max_heap.append((-val, key))
        
        heapq.heapify(max_heap)
        
        res = []
        
        while k and max_heap:
            freq, word = heapq.heappop(max_heap)
            res.append(word)
            k -= 1
        return res
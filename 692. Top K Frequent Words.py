# Oct 6, 2026 692-2
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = Counter(words)

        heap = []
        heapq.heapify(heap)

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        return res


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

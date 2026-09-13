# Sep 13, 2026 347-3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heap.append((-freq, num))

        heapq.heapify(heap)
        res = []

        for _ in range(k):
            element = heapq.heappop(heap)
            res.append(element[1])
        return res


# second attempt - solved! Jan 9
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = collections.Counter(nums)

        max_heap = []
        for key in counter.keys():
            max_heap.append([-counter[key], key])
        heapq.heapify(max_heap)

        result = []
        for i in range(k):
            _, key = heapq.heappop(max_heap)
            result.append(key)

        return result


import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums).items()
        sorted_counter = sorted(counter, key=lambda pair: pair[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_counter[i][0])

        return result

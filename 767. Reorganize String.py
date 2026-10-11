# Oct 10, 2026 767-2
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        maxheap = []
        heapq.heapify(maxheap)
        counter = Counter(s)
        for key in counter.keys():
            heapq.heappush(maxheap, (-counter[key], key))

        res = ""

        while maxheap:
            temp = []
            count, alph = heapq.heappop(maxheap)
            temp.append((count, alph))

            if res and res[-1] == alph:
                if not maxheap:
                    return ""
                temp.append(heapq.heappop(maxheap))

            res += temp[-1][1]
            temp[-1] = (temp[-1][0] + 1, temp[-1][1])
            for num, char in temp:
                if num < 0:
                    heapq.heappush(maxheap, (num, char))

        return res


# solve again

import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter = collections.Counter(s)

        max_heap = [[-count, char] for char, count in s_counter.items()]
        heapq.heapify(max_heap)

        prev = None
        res = ""

        # add to res alternatively
        while max_heap or prev:
            if prev and not max_heap:
                return ""

            count, char = heapq.heappop(max_heap)

            res += char
            count += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if count < 0:
                prev = [count, char]

        return res

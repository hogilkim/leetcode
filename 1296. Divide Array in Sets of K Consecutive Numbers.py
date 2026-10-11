from collections import Counter
import heapq


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counter = Counter(nums)
        maxheap = []
        for key in counter.keys():
            maxheap.append((key, counter[key]))

        heapq.heapify(maxheap)

        while maxheap:
            temparr = []
            prev = None
            for _ in range(k):
                if not maxheap:
                    return False
                temparr.append(heapq.heappop(maxheap))
                if prev and prev + 1 != temparr[-1][0]:
                    return False
                prev = temparr[-1][0]

            for num, count in temparr:
                count -= 1
                if count > 0:
                    heapq.heappush(maxheap, (num, count))

        return True

import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        heap = []
        heapq.heapify(heap)
        for num in hand:
            heapq.heappush(heap, num)
        res = [[] for _ in range(len(hand) // groupSize)]

        while heap:
            element = heapq.heappop(heap)
            for lst in res:
                if len(lst) == 0:
                    lst.append(element)
                    element = -1
                    break
                elif lst[-1] + 1 == element and len(lst) < groupSize:
                    lst.append(element)
                    element = -1
                    break
            if element > -1:
                return False
        return True

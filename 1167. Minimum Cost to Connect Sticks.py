import heapq

# Oct 10, 2026 1167-3


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)

        cost = 0

        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            cost += first + second

            heapq.heappush(sticks, first + second)

        return cost


import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0

        while len(sticks) >= 2:
            stick1, stick2 = heapq.heappop(sticks), heapq.heappop(sticks)
            res += stick1 + stick2

            heapq.heappush(sticks, stick1 + stick2)

        return res


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        costs = 0
        stick_1 = stick_2 = 0

        while sticks:
            stick_1 = heapq.heappop(sticks)
            if sticks:
                stick_2 = heapq.heappop(sticks)
            else:
                return costs

            new_stick = stick_1 + stick_2
            costs += new_stick

            heapq.heappush(sticks, new_stick)

        return costs

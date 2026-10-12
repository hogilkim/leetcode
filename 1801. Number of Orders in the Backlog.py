# Oct 12, 2026 1801
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_heap = []  # min heap
        buy_heap = []  # max heap

        heapq.heapify(sell_heap)
        heapq.heapify(buy_heap)

        for order in orders:
            price, amount, orderType = order
            if orderType == 0:  # buy, meax heap
                heapq.heappush(buy_heap, [-price, amount])
            else:
                heapq.heappush(sell_heap, [price, amount])
            while buy_heap and sell_heap and sell_heap[0][0] <= -buy_heap[0][0]:
                execution = min(sell_heap[0][1], buy_heap[0][1])
                sell_heap[0][1] -= execution
                buy_heap[0][1] -= execution
                if sell_heap[0][1] == 0:
                    heapq.heappop(sell_heap)
                if buy_heap[0][1] == 0:
                    heapq.heappop(buy_heap)
        count = 0
        for _, amount in buy_heap:
            count += amount
        for _, amount in sell_heap:
            count += amount
        return count % (10**9 + 7)

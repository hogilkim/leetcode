from collections import deque
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []

        tasks = deque( sorted([ (e, p, idx) for idx, (e, p) in enumerate(tasks) ]) )
        min_heap = []
        heapq.heapify(min_heap)

        t = tasks[0][0]
        num = 0
        while tasks or min_heap:
            while tasks and t >= tasks[0][0]:
                e, p, idx = tasks.popleft()
                heapq.heappush(min_heap, (p, idx))
            if min_heap:
                p, idx = heapq.heappop(min_heap)
                res.append(idx)
                num += 1
                t += p
            elif tasks:
                t = tasks[0][0]
        return res





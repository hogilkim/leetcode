from collections import defaultdict, deque
import math
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        endpoints = set()
        graph = defaultdict(set)
        
        for v1, v2 in roads:
            graph[v1].add(v2)
            graph[v2].add(v1)

            if len(graph[v1]) == 1: endpoints.add(v1)
            elif v1 in endpoints: endpoints.remove(v1)
            if len(graph[v2]) == 1: endpoints.add(v2)
            elif v2 in endpoints: endpoints.remove(v2)

        people = {}

        dq = deque(list(endpoints))

        res = 0

        while dq:
            node = dq.popleft()
            if node == 0: continue
            if node not in people: people[node] = 1
            nxt = list(graph[node])[0]
            if nxt not in people: people[nxt] = 1
            del graph[node]
            graph[nxt].remove(node)

            people[nxt]+=people[node]
            res += math.ceil(people[node]/seats)
            del people[node]
            if len(graph[nxt]) == 1: dq.append(nxt)
        
        return res
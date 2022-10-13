from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dic make a graph key: node value:reachable node, cost
        graph = defaultdict(list)
        
        for frm, to, cost in flights:
            graph[frm].append((to, cost))

            
        # queue: (stops, costs, curr)
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, 0, src))
        
        
        min_prices = [float('inf') for _ in range(n)]
        min_prices[src] = 0
        
        # while queue
        while queue:
            stop, total_cost, curr_node = heapq.heappop(queue)
                
            # for loop graph[curr_node]
            for nxtnode, cost in graph[curr_node]:
                if stop<=k and total_cost + cost < min_prices[nxtnode]:
                    min_prices[nxtnode] = total_cost+cost
                    heapq.heappush(queue, (stop+1, min_prices[nxtnode], nxtnode))          

                    
                    
        return min_prices[dst] if min_prices[dst] != float('inf') else -1
        
        
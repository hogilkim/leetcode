import collections

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target: return 0
        
        stop_to_bus = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus)
                
        #stop: bus1, bus2,...
        
        
        stops_queue = collections.deque([source])
        
        res = 0
        visited = set()
        
        while stops_queue:
            
            res += 1
            
            for _ in range(len(stops_queue)):
                curr_stop = stops_queue.popleft()
                
                for bus in stop_to_bus[curr_stop]:
                    if bus in visited: continue
                    
                    for stop in routes[bus]:
                        if stop == target: return res
                        
                        stops_queue.append(stop)
                    
                    visited.add(bus)
        return -1
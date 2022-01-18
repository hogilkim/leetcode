# solved
# first attempt - Jan 17, 2022
import collections  
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = collections.Counter(tasks)
        
        max_heap = []
        
        for key in counter.keys():
            max_heap.append([-counter[key], key])
            
        
        heapq.heapify(max_heap)
        
        cycle = n+1
        
        
        result = []
        while max_heap:
            curr_cycle = []
            for i in range(cycle):
                if max_heap:
                    curr = heapq.heappop(max_heap)
                    curr[0] += 1
                    curr_cycle.append(curr)
                else:
                    curr_cycle.append(None)
            
            for task in curr_cycle:
                if task:
                    result.append(task[1])
                    if task[0] < 0:
                        heapq.heappush(max_heap, task)
                else:
                    result.append(None)
            
        
        while not result[-1]:
            result.pop()
        
        return len(result)
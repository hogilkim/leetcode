# Dec 18, 2023 621-2
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_heap = []
        heapq.heapify(max_heap)
        for task in task_counter.keys():
            heapq.heappush(max_heap, [-task_counter[task], task])
        
        total_time = 0
        idles = 0
        while max_heap:
            available_task_num = n+1
            done_task = []
            while max_heap and available_task_num > 0:
                curr_task = heapq.heappop(max_heap)
                curr_task[0] += 1
                done_task.append(curr_task)
                available_task_num -= 1
            
            total_time += n+1
            idles = n+1 - len(done_task)
            while done_task:
                item = done_task.pop()
                if item[0] < 0: 
                    heapq.heappush(max_heap, item)
        if idles: total_time -= idles

        return total_time

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
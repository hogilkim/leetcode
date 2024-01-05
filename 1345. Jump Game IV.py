# almost solved. Needed to remove duplicate process
# Jan 4, 2024 1345-2
from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        num_to_idx = defaultdict(list)
        for idx, num in enumerate(arr):
            num_to_idx[num].append(idx)
        queue = deque([(0,0)])
        visited = set()
        visited.add(0)


        while queue:
            
            idx, steps = queue.popleft()
            if idx == len(arr)-1: return steps

            # append idx with same num
            curr_num = arr[idx]
            if curr_num in num_to_idx:
                for i in range(len(num_to_idx[curr_num])-1,-1,-1):
                    new_idx = num_to_idx[curr_num][i]
                    if new_idx not in visited:
                        queue.append((new_idx, steps+1))
                        visited.add(new_idx)
                del num_to_idx[curr_num]
            
            if idx-1 not in visited and idx-1 > 0:
                queue.append((idx-1, steps+1))
                visited.add(idx-1)
            
            if idx+1 not in visited and idx + 1 < len(arr):
                queue.append((idx+1, steps+1))
                visited.add(idx+1)
        


# solve again
import collections
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1 : return 0
        
        graph = collections.defaultdict(list)
        
        for index,num in enumerate(arr):
            graph[num].append(index)
            
        queue = collections.deque([0])
        steps = 0
        while queue:
            steps += 1
            
            for _ in range(len(queue)):
                idx = queue.popleft()
                
                if idx - 1 > 0 and arr[idx - 1] in graph:
                    queue.append(idx-1)
                    
                if idx + 1 == len(arr) - 1:
                    return steps
                
                if idx + 1 < len(arr) - 1 and arr[idx+1] in graph:
                    queue.append(idx+1)
                
                for jump_index in graph.pop(arr[idx],[]):
                    if jump_index == len(arr) -1:
                        return steps
                    if jump_index != idx:
                        queue.append(jump_index)
        
        return steps
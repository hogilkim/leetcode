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
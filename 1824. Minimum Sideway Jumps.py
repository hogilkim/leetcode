from collections import deque
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        min_steps ={}
        
        res = float('inf')
                                # steps, currpos, lane
        queue = collections.deque([(0, 0, 2)])
        
        while queue:
            steps, currpos, currlane = queue.popleft()
            while currpos < len(obstacles)-1 and obstacles[currpos+1] != currlane:
                    currpos+=1
            
            if currpos == len(obstacles)-1: res = min(res, steps)
            elif currpos in min_steps and min_steps[currpos] <= steps: continue
            else:
                min_steps[currpos] = steps
                
                for lane in range(1, 4):
                    if lane != currlane and obstacles[currpos] != lane:
                        queue.append((steps+1, currpos, lane))
        
        return res
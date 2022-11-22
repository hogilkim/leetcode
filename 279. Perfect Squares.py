import math
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        
        queue = deque([(n,0)])
        
        while queue:
            num, steps = queue.popleft()
            
            for sqside in range(int(math.sqrt(num)), 0, -1):
                newnum = num - sqside**2
                if newnum == 0: return steps+1
                queue.append((newnum, steps+1))
        
        
        
        
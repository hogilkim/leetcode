#second attempt - solved
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROW, COL = len(grid), len(grid[0])
        
                    # row, col, k, steps
        queue = deque([(0,0,k,0)])
        visited = set([(0,0,k)])
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        while queue:
            r, c, oldk, steps = queue.popleft()
            
            if (r,c) == (ROW-1, COL-1):
                return steps
            
            for rdir, cdir in directions:
                nr, nc = r+rdir, c+cdir
                
                if 0<=nr<ROW and 0<=nc<COL:
                    new_k = oldk - grid[nr][nc]
                    if (nr,nc,new_k) not in visited and new_k >= 0:
                        visited.add((nr,nc,new_k))
                        queue.append((nr,nc,new_k,steps+1))
        
        return -1

from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        queue = deque([(0,0,k,0)])
        visited = set((0,0,k))
        
        directions = [(0,1),(1,0), (0,-1),(-1,0)]
        
        while queue:
            r, c, curr_k, steps = queue.popleft()
            
            if (r,c) == (ROW-1, COL-1): return steps
            
            
            for rdir, cdir in directions:
                nr, nc = r+rdir, c+cdir
                
                if 0<=nr<ROW and 0<=nc<COL:
                    new_k = curr_k - grid[nr][nc]
                    if new_k >=0 and (nr,nc,new_k) not in visited:
                        visited.add((nr,nc,new_k))
                        queue.append((nr,nc,new_k,steps+1))
                        
            
        return -1
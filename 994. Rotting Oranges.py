# Dec 5, 2023 944-2 solved
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque([])
        visited = set()
        orange_count = 0
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2: 
                    queue.append((row, col))
                
                elif grid[row][col] == 1:
                    orange_count += 1

        if not orange_count: return 0
        orange_count += len(queue)

        
        minute = -1
        while queue:
            minute += 1
            for _ in range(len(queue)):
                orange_count -= 1
                row, col = queue.popleft()
                
                for rdir, cdir in dirs:
                    nr, nc = row + rdir, col + cdir
                    if 0<=nr<ROW and 0<=nc<COL and (nr, nc) not in visited and grid[nr][nc]==1:
                        visited.add((nr, nc))
                        queue.append((nr,nc))
        print(orange_count)
        return minute if orange_count == 0 else -1

import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        oranges = set()
        
        rotten_start = []
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    oranges.add((row,col))
                elif grid[row][col] == 2:
                    rotten_start.append((row,col))
                    
        if not oranges: return 0
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        queue = collections.deque(rotten_start)
        
        time = -1
        
        while queue:          
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for row_dir, col_dir in directions:
                    if (row+row_dir, col+col_dir) in oranges:
                        queue.append((row+row_dir, col+col_dir))
                        oranges.remove((row+row_dir, col+col_dir))
                
            time += 1
                
        return time if not oranges else -1
                    
        
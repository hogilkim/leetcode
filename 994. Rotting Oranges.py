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
                    
        
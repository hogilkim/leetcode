import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        queue = collections.deque([(0,0)])
        
        ROW, COL = len(grid), len(grid[0])
        if ROW == 1: return 1
        
        visited = set()
        visited.add((0,0))
        distance = 1
        
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        while queue:
            
            distance += 1
            for i in range(len(queue)):
                row, col = queue.popleft()
                for r_dir, c_dir in directions:
                    nr, nc = row+r_dir, col+c_dir

                    if 0<=nr<ROW and 0<=nc<COL and (nr,nc) not in visited\
                    and grid[nr][nc]==0:
                        if (nr,nc) == (ROW-1,COL-1): return distance
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            
            
        return -1
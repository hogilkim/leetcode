import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        ROW, COL = len(grid), len(grid[0])
        
        max_area = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r, c):
            area = 0
            queue = collections.deque([(r,c)])
            visited.add((r,c))
            area = 0
            while queue:
                area += len(queue)
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for r_dir, c_dir in directions:
                        nr, nc = row+r_dir, col+c_dir
                        if 0<=nr<ROW and 0<=nc<COL and (nr,nc) not in visited and grid[nr][nc]:
                            visited.add((nr,nc))
                            queue.append((nr,nc))
                        
            return area
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] and (row,col) not in visited:
                    max_area = max(max_area, bfs(row,col))
        
        
        return max_area
# dfs! solve again
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(r,c):
            q = collections.deque()
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            q.append((r,c))
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                for dir_row, dir_col in directions:
                    near_row, near_col = dir_row + row, dir_col + col
                    if (near_row in range(rows) and near_col in range(cols) 
                        and grid[near_row][near_col] == "1" and (near_row, near_col) not in visited):
                        q.append((near_row, near_col))
                        visited.add((near_row, near_col))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands +=1
        return islands
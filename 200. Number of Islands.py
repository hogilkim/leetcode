# Third attempt - solved Dec 5, 2023
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            visited.add((r,c))

            for rd, cd in dirs:
                nr, nc = r + rd, c + cd

                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited and grid[nr][nc] == "1":
                    dfs(nr, nc)

        islands = 0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands

# second attempt - Jan 9 Solved!
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        
        visited = set()
        
        ROW, COL = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        
        def dfs(row, col):
            if row >= ROW or col >= COL or row < 0 or col < 0 or (row,col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row,col))
            
            for row_dir, col_dir in directions:
                dfs(row + row_dir, col + col_dir)
            
        
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    island_count += 1
        
        return island_count

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
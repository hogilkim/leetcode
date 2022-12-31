class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        path = set()

        start = (0,0)
        goal = (0,0)
        obstacles = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    goal = (row, col)
                elif grid[row][col] == -1:
                    obstacles += 1
                elif grid[row][col] == 1:
                    start = (row, col)
        res = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r, c):
            path.add((r,c))
            if len(path) == ROW*COL - obstacles and (r,c) == goal:
                nonlocal res
                res += 1
            else:
                for rd, cd in directions:
                    nr, nc = r+rd, c+cd
                    if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc] != -1 and (nr, nc) not in path:
                        dfs(nr, nc)
            path.remove((r,c))
        
        dfs(start[0], start[1])
        return res
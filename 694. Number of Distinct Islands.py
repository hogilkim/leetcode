# second attempt - Oct 22, 2022 solved

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set()
        visited = set()
        
        dic = {
            (1,0): "d",
            (0,1): "r",
            (-1,0): "u",
            (0,-1): "l"
        }
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        ROW, COL = len(grid), len(grid[0])
        
        def dfs(r,c, prev_dir):
            
            shape = prev_dir
            visited.add((r,c))
            
            for rd, cd in directions:
                nr, nc = r+rd, c+cd
                if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    shape += dfs(nr,nc, dic[(rd,cd)])
            
            return shape +"b"
        
        for row in range(ROW):
            for col in range(COL):
                if (row,col) not in visited and grid[row][col] == 1:
                    shapes.add(dfs(row,col,""))
        
        return len(shapes)

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set()
        visited = set()
        
        ROW, COL = len(grid), len(grid[0])
        dic = {
            (1, 0): "d",
            (0, 1): "r",
            (-1, 0): "u",
            (0, -1): "l"
        }
        
        directions = dic.keys()
        def dfs(r, c):
            shape = ""
            visited.add((r,c))
            for rdir, cdir in directions:
                nr, nc = r+rdir, c+cdir
                if 0<=nr<ROW and 0<=nc<COL and (nr, nc) not in visited and grid[nr][nc]:
                    shape += dic[(rdir, cdir)] + dfs(nr, nc)
            shape += "b"
            return shape
        
        res = 0
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] and (r,c) not in visited:
                    shape = dfs(r,c)
                    print(shape)
                    if shape not in shapes:
                        shapes.add(shape)
                        res += 1
        return res
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        island1, island2 = set(), set()
        direc = [(1,0),(0,1), (-1,0), (0,-1)]
        
        queue = deque([])
        # identify islands
        def dfs(r, c, island):
            if (r,c) in island1 or (r,c) in island2: return
            if grid[r][c] == 0: return
            # add each coordinate if 1
            if grid[r][c] == 1:
                if island == 1:
                    island1.add((r,c))
                    queue.append((r,c,0))
                else:
                    island2.add((r,c))
            
            for rd, cd in direc:
            # for loop to go through all directions and call dfs again
                nr, nc = r+rd, c+cd
                if 0<=nr<ROW and 0<=nc<COL:
                    dfs(nr, nc, island)
        
        for row in range(ROW):
            for col in range(COL):
                if len(island1) == 0: dfs(row,col,1)
                else: dfs(row,col, 2)
        
        
        def bfs():
            while queue:
                for _ in range(len(queue)):
                    r, c, dis = queue.popleft()
                    if (r,c) in island2:
                        return dis
                    elif grid[r][c] == 2: continue
                    for rd, cd in direc:
                        nr, nc = r+rd, c+cd
                        if 0<=nr<ROW and 0<=nc<COL:
                            if grid[nr][nc] == 1 and (r,c) in island1: continue
                            queue.append((nr,nc,dis+1))
                    grid[r][c] = 2
                
        
        
        
        return bfs()-1
        
        
        
        
        
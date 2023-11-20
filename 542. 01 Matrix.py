# Nov 19, 2023 542-2 solve again
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        visited = set()
        direcs = [(0,1), (1,0), (-1,0), (0, -1)]
        res = [[0 for _ in range(COL)] for _ in range(ROW)]
        queue = deque([])

        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        while queue:
            r, c = queue.popleft()
            
            for rd, cd in direcs:
                nr, nc = r + rd, c + cd
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited:
                    res[nr][nc] = res[r][c] + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return res

import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = collections.deque([])
        
        ROW, COL = len(mat), len(mat[0])
        visited = set()
        for i in range(ROW):
            for j in range(COL):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        
        while queue:
            r,c = queue.popleft()
            
            for r_dir, c_dir in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0<=r+r_dir<ROW and 0<=c+c_dir<COL and (r+r_dir, c+c_dir) not in visited:
                    mat[r+r_dir][c+c_dir] = mat[r][c] + 1
                    visited.add((r+r_dir, c+c_dir))
                    queue.append((r+r_dir, c+c_dir))
            
            
        return mat
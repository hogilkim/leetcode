class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(move, r, c):
            if move < 0: return 0
            if not (0<=r<m and 0<=c<n): return 1
            
            if (move,r,c) not in memo:
                res = 0

                for r_dir, c_dir in directions:
                    new_r, new_c = r+r_dir, c+c_dir
                    res += dfs(move-1, new_r, new_c)
                memo[(move,r,c)] = res%(10**9+7)
            return memo[(move,r,c)]
            
        return dfs(maxMove, startRow, startColumn)
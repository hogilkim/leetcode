class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dic = {}
        
        ROW, COL = len(matrix), len(matrix[0])
        directions = [(1,-1),(1,1),(1,0)]

        def dfs(r, c):
            if r == ROW-1:
                return matrix[r][c]
            if (r,c) in dic: return dic[(r,c)]
            

            min_path = float('inf')

            for rd, cd in directions:
                nr, nc = r + rd, c+cd
                if 0<=nr<ROW and 0<=nc<COL:
                    min_path = min(min_path, dfs(nr,nc))
            
            dic[(r,c)] = min_path + matrix[r][c]

            return min_path + matrix[r][c]


        return min(dfs(0,c) for c in range(COL))
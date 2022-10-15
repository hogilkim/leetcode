class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        
        l, r = 0, n - 1
        u, d = 0, n - 1
        
        num = 1
        
        while l<=r or u<=d:
            # upleft -> upright
            for i in range(l, r+1):
                matrix[u][i] = num
                num += 1
                # upline filled u+=1
            u += 1
            
            # upright -> downright
            for i in range(u, d+1):
                matrix[i][r] = num
                num += 1
                # right line filled r -= 1
            r -= 1
            
            # downright -> downleft
            for i in range(r, l-1, -1):
                matrix[d][i] = num
                num += 1
                # down line filled d -= 1
            d -= 1
            
            
            # downleft->upleft
            for i in range(d, u-1, -1):
                matrix[i][l] = num
                num += 1
                 # left line filled l += 1
            l += 1
            
        return matrix
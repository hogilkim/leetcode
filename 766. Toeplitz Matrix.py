class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        
        for col in range(COL):
            r, c = 0, col
            num = matrix[r][c]
            while r<ROW and c<COL:
                if num != matrix[r][c]: return False
                
                c += 1
                r += 1
        
        for row in range(ROW):
            r, c = row, 0
            num = matrix[r][c]
            while r<ROW and c<COL:
                if num != matrix[r][c]: return False
                
                c += 1
                r += 1
        
        
        return True
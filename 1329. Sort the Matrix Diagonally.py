class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        
        # iterate ROWs first
        
        for row in range(ROW):
            self.sortAndReplace(row, 0, mat)
        # iterate COLs
        
        for col in range(1, COL):
            self.sortAndReplace(0, col, mat)
        
        return mat
            
    def sortAndReplace(self, start_row, start_col, mat):
        ROW, COL = len(mat), len(mat[0])
        temp = []
        r,c = start_row, start_col
        
        while r < ROW and c < COL:
            temp.append(mat[r][c])
            r += 1
            c += 1

        temp = sorted(temp, reverse = True)
        
        
        r,c = start_row, start_col
        
        while r < ROW and c < COL:
            mat[r][c] = temp.pop()
            r += 1
            c += 1
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.prefix_mat = [ [0]*(COL+1) for _ in range(ROW+1) ]
        
        for r in range(ROW):
            prefix = 0
            for c in range(COL):
                prefix += matrix[r][c]
                # the sum of the rectangle above the currenct self.prefix_mat[r][c]
                above_rect = self.prefix_mat[r][c+1]
                self.prefix_mat[r+1][c+1] = prefix + above_rect

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1+=1
        col1+=1
        row2+=1
        col2+=1
        
        # whole rect - left - above + topleft(duplicate deduction)
        
        whole = self.prefix_mat[row2][col2]
        left = self.prefix_mat[row2][col1-1]
        above = self.prefix_mat[row1-1][col2]
        topleft = self.prefix_mat[row1-1][col1-1]
        
        return whole - left - above + topleft
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
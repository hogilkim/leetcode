#second solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW, COL = len(matrix), len(matrix[0])
        
        set_to_zero = set()
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(row, col, row_dir, col_dir):
            if row >= ROW or col >= COL or row < 0 or col < 0:
                return
            
            
            if row_dir == 0 and col_dir == 0 and matrix[row][col] == 0 and (row,col) not in set_to_zero:
                for dir_row, dir_col in directions:
                    dfs(row+dir_row, col+dir_col, dir_row, dir_col)
                
                
            elif row_dir != 0 or col_dir != 0:
                if matrix[row][col] != 0:
                    set_to_zero.add((row,col))
                    matrix[row][col] = 0
                
                dfs(row+row_dir, col+col_dir, row_dir, col_dir)
                
            
        for row in range(ROW):
            for col in range(COL):
                dfs(row,col,0,0)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = []
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    indices.append([row, column])
        
        def row_zero(row, column):
            up_row, down_row = row-1,row+1
            
            while up_row >=0:
                matrix[up_row][column] = 0
                up_row -= 1
            while down_row < len(matrix):
                matrix[down_row][column] = 0
                down_row +=1
                
        def column_zero(row, column):
            l_column, r_column = column-1, column+1
            
            while l_column >= 0:
                matrix[row][l_column] = 0
                l_column -= 1
            while r_column < len(matrix[row]):
                matrix[row][r_column] = 0
                r_column +=1
        
        for row,column in indices:
            row_zero(row, column)
            column_zero(row, column)
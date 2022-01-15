# solve again
# first attempt - Jan 15, 2022
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        
        r,c = 0, COL-1
        
        while r < ROW and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c]>target:
                c -= 1
            else: # matrix[r][c] == target
                return True
        
        return False
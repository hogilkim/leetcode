# Solve again
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Solve again
        left, right = 0, len(matrix)-1
        
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                top_left = matrix[top][left+i]
                
                # top left <- bottom left
                matrix[top][left+i] = matrix[bottom-i][left]
                
                # bottom left <- bottom right
                matrix[bottom-i][left] = matrix[bottom][right-i]
                
                # bottom right <- top right
                matrix[bottom][right-i] = matrix[top+i][right]
                
                #top right <- top left
                matrix[top+i][right] = top_left            
            left += 1
            right -= 1
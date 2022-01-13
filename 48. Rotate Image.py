# solved
# second attempt - Jan 13, 2022
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        
        while left < right or top < bottom:
            for i in range(right - left):
                # tl->tr
                temp_rt = matrix[top+i][right]
                matrix[top+i][right] = matrix[top][left+i]
                
                # rt->rb
                temp_rb = matrix[bottom][right-i]
                matrix[bottom][right-i] = temp_rt
                
                #rb->lb
                temp_lb = matrix[bottom-i][left]
                matrix[bottom-i][left] = temp_rb
                
                #lb->tl
                matrix[top][left+i] = temp_lb
            
            left +=1
            right -=1
            top+=1
            bottom-=1
        
        return matrix
    


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
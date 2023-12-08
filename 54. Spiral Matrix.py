# solve again
# Dec 8, 2023 54-3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, down = 0, len(matrix)
    
        res = []
        
        while left < right and top < down:
            # top left -> top right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # top right -> down right
            for i in range(top, down):
                res.append(matrix[i][right-1])
            right -= 1

            if left >= right or top >= down: break

            # down right -> down left
            for i in range(right-1, left-1, -1):
                res.append(matrix[down-1][i])
            down -= 1

            # down left -> top left
            for i in range(down-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res


#second attempt - solved Jan 11, 2022
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        curr_row, curr_col = 0,0
        result = []
        
        while left <= right and top <= bottom:
            # left -> right
            curr_row = top
            curr_col = left
            while curr_col <= right:
                
                result.append(matrix[curr_row][curr_col])
                curr_col += 1
            # top -> right
            curr_row = top+1
            curr_col = right
            while curr_row <= bottom:
                result.append(matrix[curr_row][curr_col])
                curr_row += 1
            # right -> left
            curr_row = bottom
            curr_col = right - 1
            while curr_col >= left and top<bottom:
                result.append(matrix[curr_row][curr_col])
                curr_col -= 1
            # bottom -> top
            curr_row = bottom-1
            curr_col = left
            while curr_row >= top+1 and left < right:
                result.append(matrix[curr_row][curr_col])
                curr_row -= 1
                
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return result
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        
        result = []
        while left < right and top < bottom:
            print(left, right, top, bottom)
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            
            for j in range(top, bottom):
                result.append(matrix[j][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
                
            for k in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][k])
            bottom -= 1
            
            for l in range(bottom-1, top-1, -1):
                result.append(matrix[l][left])    
            left += 1
            
            
            
        return result
    
    
    
#         left, right = 0, len(matrix[0])-1
#         top, bottom = 0, len(matrix)-1
        
        
#         result = []
#         visited = set()
#         while (left <= right or top <= bottom) and (left>=0 and right>=0 and top>=0 and bottom>=0):
#             print(left, right, top, bottom)
#             for i in range(left, right+1):
#                 if (top,i) not in visited:
#                     result.append(matrix[top][i])
#                     visited.add((top,i))                
#             for j in range(top+1, bottom+1):
#                 if (j,right) not in visited:
#                     result.append(matrix[j][right])
#                     visited.add((j,right))
#             if top < bottom:
#                 for k in range(right-1, left-1, -1):
#                     if (bottom, k) not in visited:
#                         result.append(matrix[bottom][k])
#                         visited.add((bottom,k))
#             if left < right:
#                 for l in range(bottom-1, top, -1):
#                     if (l, left) not in visited:
#                         result.append(matrix[l][left])
#                         visited.add((l,left))
#             left += 1
#             right -= 1
#             top += 1
#             bottom -= 1
#         return result
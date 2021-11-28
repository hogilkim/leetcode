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
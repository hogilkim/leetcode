class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # O(n) solution
        for row in range(len(triangle)-2,-1,-1):
            for i in range(len(triangle[row])):
                triangle[row][i] += min(triangle[row+1][i], triangle[row+1][i+1])
        
        return triangle[0][0]
        
        
        # memoization solution - accepted 55.22% runtime, 7.76% memory
#         dic={} #key:(level, index) val: pathsum
        
#         def backtracking(level, index):
#             if level == len(triangle): return 0
#             elif (level, index) in dic: return dic[(level,index)]
            
#             dic[(level,index)] = triangle[level][index] + min(backtracking(level+1, index), backtracking(level+1, index+1))
            
#             return dic[(level,index)]
        
#         return backtracking(0,0)
        
        
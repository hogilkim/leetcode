from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # another solution
        
        row = [1]*n
        for i in range(m-1):
            new_row = [1]*n
            for j in range(1, n):
                new_row[j] = new_row[j-1] + row[j]
            row = new_row
        return row[n-1]
        
        
        # my solution
#         visit_queue = collections.deque([[0,0]])
        
#         dp = [[0 for i in range(n)] for j in range(m)]
        
#         dp[0][0] = 1
        
#         while visit_queue:
#             point = visit_queue.popleft()
#             add = dp[point[0]][point[1]]
#             if dp[point[0]][point[1]] < 2:
#                 if point[0] > 0:
#                     add += dp[point[0]-1][point[1]]
#                 if point[1] > 0:
#                     add += dp[point[0]][point[1]-1]
#                 dp[point[0]][point[1]] = add
#                 if point[0] + 1 < m:
#                     visit_queue.append([point[0]+1,point[1]])
#                 if point[1] + 1 < n:
#                     visit_queue.append([point[0],point[1]+1])            
#         return dp[m-1][n-1]
        
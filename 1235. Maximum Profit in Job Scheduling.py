# solve again
# Dec 24, 2023 1235-3
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:(x[1], x[0]))
        dp = [[0,0]]

        for s, e, p in jobs:
            # compare with previous job
            idx = self.bisect_left(dp, [s+1])-1
            if dp[idx][1] + p > dp[-1][1]:
                dp.append([e, dp[idx][1]+p])
        return dp[-1][1]



    def bisect_left(self, array, value):

        l, r = 0, len(array)

        while l < r:
            mid = (l+r)//2

            if array[mid] < value:
                l = mid + 1
            else:
                r = mid
        
        return l

import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime, profit), key=lambda x:x[1])
        
        dp = [[0,0]]
        
        for s,e,p in jobs:
            i = bisect.bisect_left(dp, [s+1])-1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1]+p])
        
        return dp[-1][1]

import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        start, end, profit = zip(*sorted(zip(startTime, endTime, profit)))
        
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(n)}
        
        dp = [0 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], profit[i]+dp[jump[i]])
            
        
        return dp[0]
        
#         TLE
#         memo = {}
        
        
#         jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        
#         def backtracking(i, end_time):
#             if i >= len(jobs): return 0

#             if jobs[i][0] < end_time: return backtracking(i+1, end_time)
    
#             if (i, end_time) in memo: return memo[(i, end_time)]

#             memo[(i, end_time)] = max(backtracking(i+1, jobs[i][1]) + jobs[i][2],\
#                          backtracking(i+1, end_time))

#             return memo[(i, end_time)]
        
        
        
#         backtracking(0, 0)
#         return memo[(0,0)]
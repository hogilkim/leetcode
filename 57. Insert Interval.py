# solved with O(nlogn), not with O(n)
# second attempt - Jan 13, 2022
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #O(n)
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [ min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1]) ]
        result.append(newInterval)
        return result
            
        
        #O(nlogn)
#         intervals.append(newInterval)
#         intervals = sorted(intervals, key=lambda x:x[1])
#         intervals = sorted(intervals, key=lambda x:x[0])
#         i=0
#         while i < len(intervals):
                
#             if i < len(intervals) -1 and intervals[i][1] >= intervals[i+1][0]:
#                 intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
#                 intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
#                 del intervals[i+1]
                
#             else: i += 1   
#         return intervals
        


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
# O(n) Solution
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
        
        
# My Solution: O(nlogn)        
#         intervals.append(newInterval)
#         intervals = sorted(intervals, key=lambda x:x[1])
#         intervals = sorted(intervals, key=lambda x:x[0])
        
#         i = 0
#         while i < len(intervals) - 1:
#             # inserted overlapped
#             if intervals[i+1][0] <= intervals[i][1]:
#                 if intervals[i+1][1] <= intervals[i][1]:
#                     del intervals[i+1][1]
#                 else:
#                     intervals[i][1] = intervals[i+1][1]
#                 del intervals[i+1]
#             elif intervals[i][1] == intervals[i+1][0]:
#                 intervals[i][1] = intervals[i+1][1]
#                 del intervals[i+1]
#             else:
#                 i+=1
#         return intervals
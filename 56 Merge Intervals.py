# Fourth try - solved 
# Dec 7, 2023 56-4
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x:(x[0], x[1]))

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
              intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
              del intervals[i+1]
            else:
              i += 1
        
        return intervals

        # if not intervals: return []
        # intervals = sorted(intervals, key=lambda x:x[0])
        # res = [intervals[0]]

        # for start, end in intervals[1:]:
        #     if res[-1][1] >= start:
        #         res[-1][1] = max(res[-1][1], end)
        #     else:
        #         res.append([start, end])
        
        # return res

# third try Sep 15, 2022
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:(x[0], x[1]))        
        i = 0
        
        while i < len(intervals) - 1: 
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
            else:
                i += 1
        
        return intervals
# second try Jan 7, 2022 solved!
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x:x[1])
        intervals = sorted(intervals, key=lambda x:x[0])
        
        i = 0
        
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] <= intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]       
                
                del intervals[i+1]
            else:
                i+=1
        
        return intervals

class Solution(object):
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max (intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
            else:
                i += 1
        return intervals
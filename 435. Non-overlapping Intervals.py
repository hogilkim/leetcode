# second attempt Jan 10 - solved!
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        intervals = sorted(intervals, key=lambda x:x[0])
        count = 0
        i=0
        while i < len(intervals) -1:
            if intervals[i][0]<=intervals[i+1][0]<intervals[i][1]:
                # delete i+1
                if intervals[i][1] <= intervals[i+1][1]:
                    del intervals[i+1]
                # delete i
                else:
                    del intervals[i]
                count += 1
            else:
                i += 1
        
        return count
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # solve again!
        intervals.sort()
        
        res = 0
        previous_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= previous_end:
                previous_end = end
            else:
                res+=1
                previous_end = min(previous_end, end)
                
        return res
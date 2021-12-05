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
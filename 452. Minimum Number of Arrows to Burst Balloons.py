class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[0])
        overlaps = [ [points[0][0], points[0][1]] ]

        for beg, end in points[1:]:
            if overlaps[-1][0] <= beg <= overlaps[-1][1]:
                overlaps[-1][0] = max(beg, overlaps[-1][0])
                overlaps[-1][1] = min(end, overlaps[-1][1])
            else:
                overlaps.append([beg,end])
        return len(overlaps)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[0])
        
        overlaps = [points[0]]
        
        for interval in points[1:]:
            if overlaps[-1][1] >= interval[0]:
                overlaps[-1] = [max(interval[0], overlaps[-1][0]), min(interval[1], overlaps[-1][1]) ]
            else:
                overlaps.append(interval)
                
        
        
        return len(overlaps)
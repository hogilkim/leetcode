from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        

        def calcdxdy(p1, p2):
            if p1[0]-p2[0] == 0:
                return p1[0]
            slope = (p1[1]-p2[1])/(p1[0]-p2[0])
            b = p1[1] - slope*p1[0]
            return ( slope, b )
        
        res = 0

        for i in range(len(points)):
            dic = defaultdict(int)
            for j in range(i+1, len(points)):
                dic[calcdxdy(points[i], points[j])] += 1
            if dic: res = max( res, max(dic.values()) )
        
        return res + 1
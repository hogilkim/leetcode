# Nov 20, 2023 973-2
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(points, key=lambda x:x[0]**2 + x[1]**2)[:k]

        min_heap = []
        heapq.heapify(min_heap)

        for x, y in points:
            heapq.heappush(min_heap, (x**2+y**2, x, y))
        
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x,y])
        
        return res

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # time: O(n logn solution)  space: O(1)
        return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[0:k]    
            
            
# heap solution time: O(n logn) space: O(n)
#         min_heap = []
#         heapq.heapify(min_heap)

#         for i in range(len(points)):
#             heapq.heappush(min_heap, [ points[i][0]**2 + points[i][1]**2, points[i][0], points[i][1] ])
            
        
#         res = []
#         for j in range(k):
#             _,x,y = heapq.heappop(min_heap)
#             res.append([x,y])
#         return res
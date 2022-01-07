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
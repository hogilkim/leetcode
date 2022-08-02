# Second - Aug 1st, 2022
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = [(matrix[i][0], i, 0) for i in range(len(matrix)) ]
        
        heapq.heapify(min_heap)
        
        res = min_heap[0][0]
        for _ in range(k):
            res, i, j = heapq.heappop(min_heap)
            if j + 1< len(matrix[0]):
                heapq.heappush(min_heap,(matrix[i][j+1],i,j+1))
        
        return res

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        
        for array in matrix:
            min_heap.append(array[0])
            del array[0]
        
        heapq.heapify(min_heap)
        
        th = 1
        while min_heap:
            num = heapq.heappop(min_heap)
            if th == k:
                return num
            
            min_val, index = float('inf'),-1
            for i in range(len(matrix)):
                if matrix[i] and matrix[i][0] < min_val:
                    index = i
                    min_val = matrix[i][0]
            
            th += 1
            if index > -1:
                heapq.heappush(min_heap, matrix[index][0])
                del matrix[index][0]
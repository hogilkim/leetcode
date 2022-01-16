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
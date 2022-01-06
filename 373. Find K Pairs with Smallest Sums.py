# solve again 

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
       
        if len(nums1)*len(nums2) < 1: return []
        
        min_heap = [[nums1[0] + nums2[0], 0, 0]]
        heapq.heapify(min_heap)
        visited = set()
        visited.add((0,0))
        res = []
        
        while min_heap and len(res) < k:
            _, i, j = heapq.heappop(min_heap)
            res.append([nums1[i],nums2[j]])
            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(min_heap, [nums1[i+1] + nums2[j], i+1, j])
                visited.add((i+1, j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(min_heap, [nums1[i] + nums2[j+1], i, j+1])
                visited.add((i, j+1))
        
        return res
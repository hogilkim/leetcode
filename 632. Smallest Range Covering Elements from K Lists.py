import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        
        min_range = -10e5,10e5
        
        min_heap = [(lst[0], idx, 0) for idx, lst in enumerate(nums) ]
        heapq.heapify(min_heap)
        
        max_val = max([lst[0] for lst in min_heap])
        
        while min_heap:
            min_val, list_index, num_index = heapq.heappop(min_heap)
            
            if max_val - min_val < min_range[1] - min_range[0]:
                min_range = min_val, max_val
            
            if num_index + 1 == len(nums[list_index]): return min_range
            
            next_num = nums[list_index][num_index+1]
            max_val = max(max_val, next_num)
            
            heapq.heappush(min_heap, (next_num, list_index, num_index+1))
        
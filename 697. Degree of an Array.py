import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        index_map = collections.defaultdict(list)
        max_deg = 0
        for idx, num in enumerate(nums):
            index_map[num].append(idx)
            max_deg = max(max_deg, len(index_map[num]))
        
        min_len = float('inf')
        
        for key, idx_list in index_map.items():
            if len(idx_list) == max_deg:
                min_len = min(min_len, idx_list[-1] - idx_list[0] + 1)
        
        return min_len
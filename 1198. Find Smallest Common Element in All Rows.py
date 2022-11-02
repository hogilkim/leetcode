from collections import defaultdict
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counter = defaultdict(int)
        ROWS = len(mat)
        
        for row in mat:
            for num in row:
                counter[num] += 1
        
        
        for key in sorted(counter.keys()):
            if counter[key] == ROWS: return key
        
        return -1
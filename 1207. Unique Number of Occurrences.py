import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        
        seen = set()
        
        for key, val in counter.items():
            if val in seen:
                return False
            seen.add(val)
            
        
        return True
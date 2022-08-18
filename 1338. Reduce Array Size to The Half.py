import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        og_len = len(arr)
        
        counter = collections.Counter(arr)
        
        freq_sorted = sorted([val for key, val in counter.items()])
        
        removed = 0
        set_num = 0
        
        while removed < og_len//2:
            removed += freq_sorted.pop()
            set_num += 1
        
        return set_num
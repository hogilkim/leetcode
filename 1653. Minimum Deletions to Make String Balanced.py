import collections
class Solution:
    def minimumDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        
        builder = collections.defaultdict(int)
        
        min_del = min(counter['a'], counter['b'])
        
        for char in s:
            builder[char]+=1
            
            deletions = 0
            deletions += builder['b']
            deletions += counter['a'] - builder['a']
            
            min_del = min(min_del, deletions)
        
        return min_del
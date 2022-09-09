from collections import defaultdict
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        a_to_d = defaultdict(list)
        res = 0
        max_d = -1
        
        for a, d in properties:
            a_to_d[a].append(d)
        
        for key in sorted(list(a_to_d.keys()), reverse=True):
            for d in a_to_d[key]:
                if d < max_d: res += 1
            
            max_d = max(max_d, max(a_to_d[key]))
        
        return res
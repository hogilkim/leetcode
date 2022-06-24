import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_t = collections.Counter(t)
        counter_s = collections.Counter(s)
        
        for key in counter_s.keys():
            if counter_t[key] - counter_s[key]: return key
            del counter_t[key]
            
        
        return list(counter_t.keys())[0]
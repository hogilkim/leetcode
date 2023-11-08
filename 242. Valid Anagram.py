import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        LEN = len(s)
        counter = collections.Counter()

        for i in range(LEN):
            counter[s[i]] += 1
            counter[t[i]] -= 1
        
        for char in s:
            if counter[char] != 0: return False
        
        return True

        #return collections.Counter(s) == collections.Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
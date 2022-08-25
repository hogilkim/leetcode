import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_counter = collections.Counter(ransomNote)
        mag_counter = collections.Counter(magazine)
        
        for key in rans_counter:
            if key not in mag_counter: return False
            if rans_counter[key] > mag_counter[key]: return False
        
        return True
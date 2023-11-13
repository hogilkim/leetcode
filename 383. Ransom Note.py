# Nov 12, 2023 383-2

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        for key in c1.keys():
            if key not in c2: return False
        
            elif c1[key] > c2[key]: return False
        
        return True

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_counter = collections.Counter(ransomNote)
        mag_counter = collections.Counter(magazine)
        
        for key in rans_counter:
            if key not in mag_counter: return False
            if rans_counter[key] > mag_counter[key]: return False
        
        return True
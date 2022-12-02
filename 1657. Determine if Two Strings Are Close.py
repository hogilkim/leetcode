from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        if set(word1) == set(word2) and list(sorted(c1.values())) == list(sorted(c2.values())):
            return True
        return False
        
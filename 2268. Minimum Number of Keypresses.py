from collections import Counter
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)
        
        chars = sorted([(char, counter[char]) for char in counter.keys()], key = lambda x:-x[1])
        
        res = 0
        savedchars = 0
        
        for char, freq in chars:
            res += (divmod(savedchars,9)[0]+1)*freq 
            savedchars+= 1
            
        return res
        
        
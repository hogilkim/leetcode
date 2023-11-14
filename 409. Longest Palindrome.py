from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        odd = 0

        for key in counter.keys():
            length += counter[key]//2 * 2
            if odd == 0 and counter[key]%2:
                odd = 1
        
        return length + odd
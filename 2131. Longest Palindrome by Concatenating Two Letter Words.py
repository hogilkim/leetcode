from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        center = 0
        palin_diff = 0
        palin_same = 0
        
        for word, count in counter.items():
            if word[0]==word[1]:
                palin_same += count//2*2
                
                if count%2==1: center =2
            
            else:
                palin_diff += min(counter[word], counter[word[::-1]])*0.5
        
        return palin_same*2 + int(palin_diff)*4 + center
                
                
                
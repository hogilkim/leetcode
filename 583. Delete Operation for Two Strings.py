class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
            
        long, short = len(word1), len(word2)
        
        prev = [i for i in range(long+1)]
        
        for idx, char in enumerate(word2):
            curr = [0]*(long+1)
            curr[0] = idx + 1
            for i in range(1,long+1):
                if char == word1[i-1]:
                    curr[i] = prev[i-1]
                else:
                    curr[i] = 1+min(prev[i], curr[i-1])
            
            prev = curr
        
        return curr[-1]
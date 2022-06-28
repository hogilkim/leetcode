import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        
        freqs = sorted([val for key, val in counter.items()], reverse=True)
        
        res = 0
        print(freqs)
        for i in range(len(freqs)-1):
            
            if freqs[i]-freqs[i+1] < 0:
                res += abs(freqs[i]-freqs[i+1])
                freqs[i+1] -= abs(freqs[i]-freqs[i+1])
                res += abs(freqs[i]-freqs[i+1])
            if freqs[i] and freqs[i]-freqs[i+1]==0:
                freqs[i+1] -= 1
                res += 1
        
        return res
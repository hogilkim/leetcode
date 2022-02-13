class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        compressed = []
        
        val1 = freq1 = val2 = freq2 = 0
        
        while encoded1 or encoded2:
            if encoded1 and not freq1:
                val1, freq1 = encoded1.pop()
            if encoded2 and not freq2:
                val2, freq2 = encoded2.pop()
                
            prod = val1*val2
            min_freq = min(freq1, freq2)
            if compressed and compressed[-1][0] == prod:
                compressed[-1][1] += min_freq
            else:
                compressed.append([prod, min_freq])
            
            freq1 -= min_freq
            freq2 -= min_freq
        
        return reversed(compressed)
            
            
                
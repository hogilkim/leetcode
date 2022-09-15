from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2: return []
        changed = sorted(changed)
        N = len(changed)
        
        zero_counter = 0
        while changed and changed[0] == 0:
            changed.pop(0)
            zero_counter+=1
        
        if zero_counter%2: return []
        
        og = [0]*(zero_counter//2)
        counter = Counter(changed)
        
        for key in sorted(counter.keys()):
            if counter[key] == 0: continue
            if counter[key*2] == 0: return []
            counter[key*2] -= counter[key]
            

        
        for key in counter.keys():
            og += [key]*counter[key]
        return og if len(og)*2 == N else []
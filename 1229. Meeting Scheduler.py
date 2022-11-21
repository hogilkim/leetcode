class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1)
        slots2 = sorted(slots2)
        
        j = 0        
        
        for i in range(len(slots1)):
            while j < len(slots2):
                s1_start, s1_end, s2_start, s2_end = slots1[i][0], slots1[i][1], slots2[j][0], slots2[j][1]
                
                start = max(s1_start, s2_start)
                end = min(s1_end, s2_end)
                
                if end - start >= duration:
                    return [start,start+duration]
                    
                if slots1[i][1] <= slots2[j][1]: break
                j += 1
            
        
        return []
                
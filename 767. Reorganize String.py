# solve again

import collections

class Solution:
    def reorganizeString(self, s: str) -> str:
        s_counter = collections.Counter(s)
        
        max_heap = [[-count, char] for char, count in s_counter.items()]
        heapq.heapify(max_heap)
        
        
        prev = None
        res = ""
        
        # add to res alternatively
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            count, char = heapq.heappop(max_heap)
            
            res += char
            count += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if count < 0 :
                prev = [count, char]
                
        
        return res
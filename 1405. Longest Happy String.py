# solve again

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        heapq.heapify(max_heap)
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        res = ""
        
        while max_heap:
            first_num, first_char = heapq.heappop(max_heap)
            if len(res) > 1 and res[-1]==res[-2]==first_char:
                if not max_heap:
                    return res
                second_num, second_char = heapq.heappop(max_heap)
                res += second_char
                second_num += 1
                if second_num < 0:
                    heapq.heappush(max_heap, (second_num, second_char))
            res += first_char
            first_num += 1
            if first_num < 0:
                heapq.heappush(max_heap, (first_num, first_char))
            
        return res
        
            
#         max_heap = [[-a,'a'], [-b,'b'], [-c, 'c']]
#         heapq.heapify(max_heap)
        
#         res = ""
#         while max_heap:
#             num_1, char_1 = heapq.heappop(max_heap)
#             if res and res[-1] == char_1: break
#             if num_1 <= -2: 
#                 res += char_1 + char_1
#                 num_1 += 2
#             elif num_1 == -1: 
#                 res += char_1
#                 num_1 += 1
            
#             if max_heap:
#                 num_2, char_2 = heapq.heappop(max_heap)
#                 if num_2 <= -2: 
#                     res += char_2 + char_2
#                     num_2 += 2
#                 elif num_2 == -1: 
#                     res += char_2
#                     num_2 += 1
                
#                 if num_2 < 0: heapq.heappush(max_heap, [num_2, char_2])
            
#             if num_1 < 0: heapq.heappush(max_heap, [num_1, char_1])
            
        
#         return res
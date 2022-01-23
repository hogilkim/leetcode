import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        count = 0
        
        for key in s_counter.keys():
            if key in t_counter:
                count += abs(s_counter[key] - t_counter[key])
            else:
                count += s_counter[key]
        
        for key in t_counter.keys():
            if key not in s_counter:
                count += t_counter[key]
        
        return count//2
    
    
#         s_counter = collections.Counter(s)
#         t_counter = collections.Counter(t)
        
#         s_array,t_array = [0]*26, [0]*26
        
#         for key in s_counter.keys():
#             s_array[ord(key) - ord('a')] = s_counter[key]
        
#         for key in t_counter.keys():
#             t_array[ord(key) - ord('a')] = t_counter[key]
           
        
        
#         count = 0
#         for i in range(26):
#             count += abs(s_array[i] - t_array[i])
        
#         return count//2

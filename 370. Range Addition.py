# solve again #Amazon
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # time: O(k*n) space: O(n)
        
        result = [0]*length
        
        for start, end, inc in updates:
            result[start] += inc
            if end + 1 < length:
                result[end+1] -= inc
        
        for i in range(1, length):
            result[i] += result[i-1]
            
        return result
        
        # brute force #time: O(range*n) space: O(n)
#         result = [0]*length
        
#         for update in updates:
#             start = update[0]
#             end = update[1]
#             inc = update[2]
            
#             for i in range(start, end+1):
#                 result[i] += inc
        
        
#         return result

        
        
        
       
        
import collections
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = collections.deque([i for i in range(1,10)])
        res = []
        
        while queue:
            element = queue.popleft()
            
            if low<=element<=high:
                res.append(element)
            last = element % 10
            if last<9: queue.append(element*10+last+1)
        
        return res
        
        
#         res = []
        
#         # for each length
#         for length in range(len(str(low)), len(str(high))+1):
#             # from which to start? available start value <= 10-length
#             for i in range(1, 10-length+1):
#                 num = 0
#                 # the actual building process
#                 for j in range(i, length+i):
#                     num = num*10+j
#                 if low<=num<=high:
#                     res.append(num)
        
        
#         return res
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        res = 0
        count = [0]*60
        
        for t in time:
            res += count[t%60]
            count [-t%60] += 1
        
        return res
    
    
    
    # wrong solution
#         res = 0
#         def backtracking(part_sum, idx):
#             nonlocal res
#             if idx == len(time): return
            
#             part_sum += time[idx]
            
#             if part_sum%60 == 0: res += 1
            
#             # choose idx
            
#             backtracking(part_sum, idx + 1)
#             part_sum -= time[idx]
            
#             # not choose idx
#             backtracking(part_sum, idx + 1)
        
#         backtracking(0,0)
        
        
#         return res
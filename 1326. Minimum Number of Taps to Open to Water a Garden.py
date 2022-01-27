class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_jump = [0]*(n+1)
        
        for i, r in enumerate(ranges):
            jump_from, jump_to = max(0, i-r), min(n, i+r)
            max_jump[jump_from] = max(max_jump[jump_from], jump_to-jump_from)
        
        # ---
        curr_pos = jump_to = step = 0
        
        while jump_to < n:
            step+=1
            curr_pos, jump_to = jump_to, max(i+max_jump[i] for i in range(curr_pos, jump_to+1))
            if curr_pos == jump_to:
                return -1
            
        return step
        
        
#       k: num of ranges-> time: O(2^k)
#         self.min_tap = -1
#         intervals = []
        
#         for i in range(len(ranges)):
#             if ranges[i]:
#                 intervals.append([max(0, i - ranges[i]), min(n, i+ranges[i])])
            
#         def backtracking(covered, not_covered_start, i):
#             if not_covered_start == n:
#                 self.min_tap = min(self.min_tap, len(covered)) if self.min_tap > -1 else len(covered)
#                 return
#             if i >= len(intervals):
#                 return
            
#             # decide to include watertap i
#             if intervals[i][0] <= not_covered_start < intervals[i][1]:
#                 covered.append(intervals[i])
#                 backtracking(covered, intervals[i][1], i+1)
#                 covered.pop()
            
#             # not include watertap i
#             backtracking(covered, not_covered_start, i+1)
            
            
#         backtracking([],0,0)
#         return self.min_tap
        
        
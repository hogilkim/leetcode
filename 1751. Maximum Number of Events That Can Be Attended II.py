# solve again
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        cache = {}
        
        def dp(end, event_index, event_left):
            # base case 1
            if event_left == 0 or event_index == len(events):
                return 0
            
            # if already calculated
            if (end, event_index, event_left) in cache:
                return cache[(end, event_index, event_left)]
            
            event_start, event_end, event_value = events[event_index]
            
            # base case 2
            if event_start <= end:
                return dp(end, event_index+1, event_left)
            
            
            # choice 1: attend
            attend = event_value + dp(event_end, event_index + 1, event_left-1)
            # choice 2: skip
            skip = dp(end, event_index+1, event_left)
            
            cache[(end, event_index, event_left)] = max(attend, skip)
            return cache[(end, event_index, event_left)]
        
        dp(0,0,k)
        return cache[(0,0,k)]
        # return dp(0,0,k)
        
            
        
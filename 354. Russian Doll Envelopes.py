from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        
        envelopes = sorted(envelopes, key=lambda x: (x[0],-x[1]))
        
        dp = []
        
        for w,h in envelopes:
            
            idx = bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        
        return len(dp)
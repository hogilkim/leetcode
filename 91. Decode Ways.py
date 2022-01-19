# solve again
# second attempt - Jan 18, 2022

class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0: return 0
        dp = [0]*(len(s)+1)
        dp[0:2] = [1,1]
        
        for i in range(2, len(s) + 1):
            if int(s[i-1]) > 0 :
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            
        
        
        return dp[-1]
class Solution:

    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0:2] = [1,1]

        for i in range(2, len(s) + 1): 
            # One step jump
            if 0 < int(s[i-1:i]):    #(2)
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
                
        return dp[-1]
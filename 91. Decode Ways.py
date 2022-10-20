# Third Oct 20, 2022 
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
            
        # dp size len(s) + 1
        dp = [0] * (len(s) + 1)
        dp[0] = 1; dp[1] = 1
        
        # for loop
        for i in range(1,len(s)):
            # s[i] >0 -> add dp[i+1]
            if int(s[i]) > 0: dp[i+1] += dp[i]
                
            # 10<=s[i-1] + s[i] <= 26 -> add dp[i+1]
            if 10<=int(s[i-1:i+1])<=26: dp[i+1] += dp[i-1]
        
        return dp[-1]


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
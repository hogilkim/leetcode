class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     a f e
    #   0 0 0 0
    # a 0 1 1 1
    # b 0 1 1 1
    # c 0 1 1 1
    # a 0 1 1 1
    # e 0 1 1 2
        dp = [ [ 0 for _ in range(len(text1)+1) ] for _ in range(len(text2)+1) ]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[i][j]
# solve again
# Third attempt - Dec 10, 2023
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in range(len(dp)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and "".join(s[i:i+len(word)]) == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]: break
        
        return dp[0]

# solve again
# second attempt Jan 13 2022
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if (i+len(word) <= len(s)) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        
        return dp[0]
# solve again
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # solve again
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = [0] * 26

        for char in s:
            curr = ord(char) - ord('a')
            longest = 1
            for prev in range(len(dp)):
                if abs(curr - prev) <= k:
                    longest = max(longest, dp[prev] + 1)
            dp[curr] = longest
        
        return max(dp)
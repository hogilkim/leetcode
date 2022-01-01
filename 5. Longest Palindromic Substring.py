# Try this again
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res = max(self.helper(i,i,s), self.helper(i,i+1,s), res, key=len)
        return res
            
    def helper(self, l, r, s):
        while l>=0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


# Solved, but previous solution is much better
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_l = len(s)
        max_r = 0
        for i in range(len(s)):
            l1, r1 = self.longest_palin(s, i, i)
            if r1 - l1 + 1> max_len:
                max_len = r1-l1+1
                max_l = l1
                max_r = r1
            l2, r2 = self.longest_palin(s, i, i+1)
            if r2 - l2 + 1 > max_len:
                max_len = r2-l2+1
                max_l = l2
                max_r = r2
        return s[max_l:max_r + 1]
        
        
        
    def longest_palin(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return l+1, r-1
            l -= 1
            r += 1
        return l+1, r-1
        
        
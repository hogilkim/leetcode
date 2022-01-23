# solve again
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                
                return self.isPalin(s[l+1:r+1]) or self.isPalin(s[l:r])
            l += 1
            r -= 1
            
        return True
    
    def isPalin(self, s):
        return s == s[::-1]
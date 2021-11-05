class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.helper(i,i,s)
            count += self.helper(i,i+1,s)
        return count
        
        
    def helper(self, l,r,s):
        count = 0
        while l>=0 and r<len(s):
            if s[r] == s[l]:
                count+=1
                r+=1
                l-=1
            else:
                l = -1
        return count
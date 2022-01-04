# second try - solved
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palin = 0
        for i in range(len(s)):
            total_palin += self.helper(s,i,i) + self.helper(s,i,i+1)
        
        return total_palin
        
        
    def helper(self, s, l, r):
        if r >= len(s): return 0
        
        palin_num = 0
        while l>=0 and r < len(s):
            if s[l] == s[r]:
                palin_num += 1
            else:
                break
            l-=1
            r+=1
        return palin_num

        
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
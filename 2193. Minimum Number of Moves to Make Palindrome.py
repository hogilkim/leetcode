class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        END_IDX = len(s) - 1
        res = 0
        s = list(s)
        
        for left in range(len(s)//2):
            right = END_IDX - left
            
            if s[left] == s[right]: continue
                
            l,r = left, right
            
            while s[left] != s[r]:
                r -= 1
            
            while s[right] != s[l]:
                l += 1
            
            if right - r < l - left:
                res += right - r
                for i in range(r, right):
                    s[i] = s[i+1]
            
            else:
                res += l - left
                for i in range(l,left,-1):
                    s[i] = s[i-1]
            
        
        return res
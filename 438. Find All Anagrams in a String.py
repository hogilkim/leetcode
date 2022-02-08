class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        s_alphabets = [0] * 26
        p_alphabets = [0] * 26
        
        for i in range(len(p)):
            p_alphabets[ord(p[i]) - ord('a')] += 1
            #s_alphabets[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(s)):
            if i >= len(p):
                s_alphabets[ord(s[i-len(p)]) - ord('a')] -= 1
            s_alphabets[ord(s[i]) - ord('a')] += 1
            if s_alphabets == p_alphabets:
                res.append(i-len(p) + 1)
        
        return res
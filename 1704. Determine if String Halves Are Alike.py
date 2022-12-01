class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        
        front = back = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                if i < len(s)//2:
                    front += 1
                else: back +=1
        
        return front == back
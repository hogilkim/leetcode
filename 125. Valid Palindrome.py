class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                new_s += char.lower()
            elif '0' <= char <= '9':
                new_s += char
        
        return new_s == new_s[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = ""
        for ch in s:
            if ch.isalnum():
                lower_s += ch.lower()
        lower_s_reverse = lower_s[::-1]
        return lower_s == lower_s_reverse
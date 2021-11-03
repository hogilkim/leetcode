class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = ""
        for ch in s:
            if ch.isalnum():
                lower_s += ch.lower()
        lower_s_reverse = lower_s[::-1]
        return lower_s == lower_s_reverse
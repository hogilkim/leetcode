class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = pos = 0
        
        for char in reversed(columnTitle):
            digit = ord(char) - ord('A') + 1
            ans += digit * 26 ** pos
            pos += 1
        return ans
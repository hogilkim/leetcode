# Dec 16, 2023 8

class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        idx = 0

        while idx < len(s) and s[idx] == " ":
            idx += 1
        
        neg = False
        if idx < len(s) and s[idx] in "+-":
            if s[idx] == "-": neg = True
            idx+=1
        
        num = 0

        while idx < len(s) and s[idx].isdigit():
            num = num*10 + int(s[idx])
            if num > MAX_INT: return MIN_INT if neg else MAX_INT
            idx += 1
        
        return -num if neg else num

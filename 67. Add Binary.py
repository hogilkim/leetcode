# Nov 15, 2023 67
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        LEN = max(len(a), len(b))

        curr = 0
        res = ""
        for i in range(LEN):
            if i < len(a):
                curr += int(a[i])
            if i < len(b):
                curr += int(b[i])

            res += str(curr%2)
            curr //= 2
        
        if curr: res += "1"

        return res[::-1]
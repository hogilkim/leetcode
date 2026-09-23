# Sep 22, 2026
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1list = list(reversed(list(num1)))
        num2list = list(reversed(list(num2)))
        res = [0] * max(len(num1), len(num2)) * 2
        carry = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = ord(num1list[i]) - ord("0")
                digit2 = ord(num2list[j]) - ord("0")
                res[i + j] += digit1 * digit2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10

        while res and res[-1] == 0:
            res.pop()
        output = ""
        for char in list(reversed(res)):
            output += str(char)
        return output

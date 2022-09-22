class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        slist = list(s)
        res = []
        for idx, char in enumerate(slist):
            if char == " ":
                while stack:
                    res.append(stack.pop())
                res.append(" ")
            else: stack.append(char)
        return "".join(res+stack[::-1])
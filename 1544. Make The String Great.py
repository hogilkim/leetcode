# Oct 11, 2026 1544-2
class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        diff = abs(ord("A") - ord("a"))

        for char in s[1:]:
            if stack and abs(ord(char) - ord(stack[-1])) == diff:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in list(s):
            lower = char.lower()
            upper = char.upper()
            if stack and (
                stack[-1] == lower
                and char == upper
                or stack[-1] == upper
                and char == lower
            ):
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

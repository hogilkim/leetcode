# Sep 5, 2026 20-3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        converter = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in "[{(":
                stack.append(char)
            elif stack and converter[char] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        converter = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in "({[":
                stack.append(char)
            elif not stack:
                return False
            elif stack and stack[-1] == converter[char]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "{":
                stack.append(char)
            elif char == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif char == "[":
                stack.append(char)
            elif char == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

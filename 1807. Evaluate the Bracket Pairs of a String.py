# Oct 14, 2026 1807
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        convert_map = {}
        for key, val in knowledge:
            convert_map[key] = val

        stack = [""]

        for char in s:
            if char == "(":
                stack.append("")
            elif char == ")":
                key = stack.pop()
                value = convert_map.get(key, "?")
                stack[-1] += value
            else:
                stack[-1] += char

        return stack[0]

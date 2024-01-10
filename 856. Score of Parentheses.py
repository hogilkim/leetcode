# Solve again, Jan 9, 2024 856-2
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scores = [0]

        for char in s:
            if char == "(":
                scores.append(0)
            else:
                val = scores.pop()
                scores[-1] += max(val*2, 1)
        
        return scores[0]


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(val*2, 1)
        
        return stack[-1]
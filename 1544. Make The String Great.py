class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in list(s):
            lower = char.lower()
            upper = char.upper()
            if stack and (stack[-1] == lower and char == upper or stack[-1] == upper and char == lower):
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
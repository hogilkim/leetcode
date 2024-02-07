# Solve again Feb 6, 2024 316
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)

        stack = []
        in_stack = set()
        for char in s:
            counter[char] -= 1

            if char in in_stack: continue
            while stack and stack[-1] > char and counter[stack[-1]] >= 1:
                in_stack.remove(stack[-1])
                stack.pop()

            stack.append(char)
            in_stack.add(char)
        
        return "".join(stack)

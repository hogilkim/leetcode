class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        open_stack = []

        for idx, char in enumerate(s):
            if char == "(":
                open_stack.append(idx)
            if char == "*":
                star_stack.append(idx)

            if char == ")":
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while open_stack and star_stack:
            if open_stack[-1] > star_stack[-1]:
                return False
            open_stack.pop()
            star_stack.pop()
        return len(open_stack) == 0

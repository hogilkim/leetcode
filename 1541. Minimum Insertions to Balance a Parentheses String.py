# Solve again, Jan 19, 2024 1541
class Solution:
    def minInsertions(self, s: str) -> int:
        need_close = 0
        add_open = 0

        for char in s:
            if char == "(":
                # not fully closed. need open on the left
                if need_close%2:
                    # add open
                    add_open += 1
                    need_close -= 1
                need_close += 2
            else:
                need_close -= 1
                # not enough open. need open on the left
                if need_close < 0:
                    add_open += 1
                    need_close += 2
        
        return add_open + need_close
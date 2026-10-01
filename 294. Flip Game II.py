class Solution:
    def canWin(self, currentState: str) -> bool:
        memo = {}

        def backtracking(curr):
            if curr in memo:
                return memo[curr]
            curr = list(curr)
            for i in range(len(curr) - 1):
                if curr[i] == curr[i + 1] == "+":
                    curr[i] = "-"
                    curr[i + 1] = "-"
                    if not backtracking("".join(curr)):
                        curr[i] = "+"
                        curr[i + 1] = "+"
                        memo["".join(curr)] = True
                        return True
                    curr[i] = "+"
                    curr[i + 1] = "+"
            memo["".join(curr)] = False
            return False

        return backtracking(currentState)

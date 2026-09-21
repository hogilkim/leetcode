# Sep 21, 2026 22-2
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtracking(substring, opens, close):
            if len(substring) == n * 2:
                res.append(substring)
                return
            # if len(substring) == 5:
            #     print(substring, opens)
            # open new
            if opens < n:
                backtracking(substring + "(", opens + 1, close)
            if close < opens:
                backtracking(substring + ")", opens, close + 1)

        backtracking("", 0, 0)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, left, right):
            if left + right == 2 * n:
                res.append(string)
                return
            # choose to include (
            if left < n:
                dfs(string + "(", left + 1, right)

            if right < left:
                dfs(string + ")", left, right + 1)

        dfs("", 0, 0)
        return res

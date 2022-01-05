class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(string, left, right):
            if left + right == 2*n:
                res.append(string)
                return
            # choose to include (
            if left < n:
                dfs(string+'(', left + 1, right)
            
            if right < left:
                dfs(string+')', left, right+1)
        dfs("", 0, 0)
        return res
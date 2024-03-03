# Solve again
# Mar 2, 2024 32
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        record = [0]*len(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if stack and s[i] == ")":
                record[stack.pop()] = 1
                record[i] = 1
        

        res = curr = 0

        for num in record:
            if num == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 0
        
        return max(res, curr)
# solve again
# very hard for me. Took too long time to just understand.
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []  #  non-decreasing 
        arr = [float('-inf')] + arr + [float('-inf')]
        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] > n:
                cur = stack.pop()
                res += arr[cur] * (i - cur) * (cur - stack[-1]) 
            stack.append(i)
        return res % (10**9 + 7)
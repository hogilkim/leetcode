class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        res = 0
        stack = []
        arr = [0] + arr + [0]
        for idx, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                curr = stack.pop()
                res += arr[curr]*(idx-curr)*(curr-stack[-1])
            stack.append(idx)
        
        return res%MOD
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
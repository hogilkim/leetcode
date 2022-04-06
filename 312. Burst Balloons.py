class Solution:
    def maxCoins(self, nums: List[int]) -> int:
#         nums  = [1] + nums + [1]
        
#         dp = {}
        
#         def dfs(l, r):
#             if (l,r) in dp: return dp[(l,r)]
#             elif l == r:
#                 dp[(l,r)] = nums[l-1]*nums[l]*nums[l+1]
#                 return dp[(l,r)]
            
#             coins = 0
#             for i in range(l, r+1):
#                 coins = max( coins, nums[l-1]*nums[i]*nums[r+1] + dfs(l, i-1) + dfs(i+1, r) )
#             dp[(l,r)] = coins
#             return coins
        
#         dfs(1,len(nums)-2)
#         return dp[(1,len(nums)-2)]




        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)


# second attempt - solved
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for value in range(amount+1):
            for coin in coins:
                if value - coin >= 0:
                    dp[value] = min(dp[value], dp[value-coin] + 1)
                
        return dp[value] if dp[value] < amount+1 else -1
        
        
        
        
#         coins = sorted(coins)
#         dp = [0] * (amount + 1)
        
        
#         for value in range(1, amount+1):
#             min_coin_nums = 2**31
#             for i in range(len(coins)-1, -1, -1):
#                 if value - coins[i] > 0:
#                     candidate = dp[value-coins[i]]
#                     if candidate != -1:
#                         min_coin_nums = min( min_coin_nums, dp[value - coins[i]] + 1 )
#                 elif value%coins[i] == 0:
#                     min_coin_nums = min( min_coin_nums, value//coins[i] )
            
#             dp[value] = min_coin_nums if min_coin_nums < 2**31 else -1        
#         return dp[amount]


#  -------------------------------------------------------------------------------------
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1]*(amount+1)
        dp[0] = 0
        
        for a in range(1, amount +1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    print("a:",a,"a-c:", a-c, dp, sep=" ")
        return dp[amount] if dp[amount] != amount + 1 else -1
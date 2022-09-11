class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0]*len(prices) # profits
        
        if k > len(prices):
            res = 0
            for i in range(1,len(prices)):
                if prices[i] - prices[i-1] > 0 : res += prices[i] - prices[i-1]
            return res
        
        for _ in range(k):
            prof_minus_price = -prices[0]
            profit = 0
            for i in range(1, len(dp)):
                prof_minus_price = max(prof_minus_price, dp[i] - prices[i])
                profit = max(profit, prof_minus_price + prices[i])
                dp[i] = profit
        
        return dp[-1]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # stores maximum profit that it can make in each day
        profits = []
        
        #           [3,3,5,0,0,3,1,4]
        # profits = [0,0,2,2,2,2,2,3]
        
        min_buy_price = float('inf')
        max_profit = 0
        for price in prices:
            min_buy_price = min(min_buy_price, price)
            max_profit = max(max_profit, price - min_buy_price)
            profits.append(max_profit)
        
        total_max_profit = max_profit
        max_sell_price = 0
        
        # backward for loop
        for i in range(len(profits)-1, 0, -1):
            # prices =  [3,3,5,0, 0,3,1,4]
            # profits = [0,0,2,2, 2,2,2,3]
            
            max_sell_price = max(max_sell_price, prices[i])
            
            # compare max_sell_price - curr_price + profits[i-1] AND total_max_profit -> store maximum
            total_max_profit = max(total_max_profit, max_sell_price - prices[i] + profits[i-1])
        
        return total_max_profit
            
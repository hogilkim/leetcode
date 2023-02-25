class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')

        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)


        return max_profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_diff = 0
        for price in prices:
            min_price = min(min_price, price)
            diff = price - min_price
            max_diff = max(diff, max_diff)
        return max_diff
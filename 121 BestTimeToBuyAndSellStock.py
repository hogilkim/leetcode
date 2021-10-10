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
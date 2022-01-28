class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # O(n) time. O(n) space
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
            stack.append(i)
            
        return prices
        
        # O(n^2)
#         result = []
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[i] >= prices[j]:
#                     result.append(prices[i] - prices[j])
#                     break
#                 if j == len(prices)-1:
#                     result.append(prices[i])
#         result.append(prices[-1])
        
#         return result
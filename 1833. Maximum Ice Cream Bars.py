class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        bars = 0
        for cost in costs:
            if cost <= coins:
                coins -= cost
                bars += 1
            else: break
        
        return bars
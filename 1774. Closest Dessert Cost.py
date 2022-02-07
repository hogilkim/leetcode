# solve again
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        min_diff = float('inf')
        cost = float('inf')
        
        def backtracking(total_cost, index):
            nonlocal cost, min_diff
            if abs(total_cost - target) < min_diff:
                min_diff = abs(total_cost - target)
                cost = total_cost
            elif abs(total_cost - target) == min_diff:
                cost = min(cost, total_cost)
            
            
            if index >= len(toppingCosts): return
            
            for topping_num in range(3):
                backtracking(total_cost + toppingCosts[index]*topping_num, index+1)
        
        for base in baseCosts:
            backtracking(base, 0)
        
        return cost
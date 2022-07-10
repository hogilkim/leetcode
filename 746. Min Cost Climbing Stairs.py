class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, prev_prev = cost[1],cost[0]
        
        for i in range(2, len(cost)):
            prev_prev, prev = prev, cost[i] + min(prev_prev, prev)
        
        return min(prev, prev_prev)
            
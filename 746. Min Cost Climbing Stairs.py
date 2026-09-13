# Sep 13, 2026 746-2
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0]*len(cost)
        # dp[0]=cost[0]
        # dp[1]=cost[1]

        # for i in range(2, len(cost)):
        #     dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        # return min(dp[-1],dp[-2])

        prevprev, prev = cost[0], cost[1]

        for i in range(2, len(cost)):
            prevprev, prev = prev, min(prevprev, prev) + cost[i]

        return min(prevprev, prev)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, prev_prev = cost[1], cost[0]

        for i in range(2, len(cost)):
            prev_prev, prev = prev, cost[i] + min(prev_prev, prev)

        return min(prev, prev_prev)

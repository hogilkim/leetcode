import heapq
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        l = 0
        costs_sum = 0
        chargeTimeMax = []
        # heapq.heapify(chargeTimeMax)
        res = 0
        
        for r in range(len(chargeTimes)):
            costs_sum += runningCosts[r]
            heapq.heappush(chargeTimeMax, (-chargeTimes[r], r))
            
            while l <= r:
                # pop chargeTimes that is out of the window l <--> r
                while chargeTimeMax and chargeTimeMax[0][1] < l:
                    heapq.heappop(chargeTimeMax)
                
                # total cost of running a robot
                total_cost = -chargeTimeMax[0][0] + (r-l+1)*costs_sum
                
                # can run the robot
                if total_cost <= budget: 
                    res = max(res, r-l+1)
                    break
                # cannot run the robot
                else:
                    costs_sum -= runningCosts[l]
                    l += 1                    
        return res
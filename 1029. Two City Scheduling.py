class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([i for i,j in costs]) + sum(sorted([j-i for i,j in costs])[:len(costs)//2])
#         cost = float('inf')
        
        
#         def backtracking(cityA, cityB, totalCost, idx):
#             nonlocal cost
            
#             if len(cityA) + len(cityB) == len(costs):
#                 cost = min(totalCost, cost)
            
#             # choose cityA
#             if len(cityA) < len(costs)//2:
#                 cityA.append(costs[idx][0])
#                 backtracking(cityA, cityB, totalCost + costs[idx][0], idx+1)
#                 cityA.pop()
            
#             # choose cityB
#             if len(cityB) < len(costs)//2:
#                 cityB.append(costs[idx][1])
#                 backtracking(cityA, cityB, totalCost +costs[idx][1], idx+1)
#                 cityB.pop()
            
            
#         backtracking([],[],0,0)
#         return cost
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        red = blue = green = 0
        
        for r,b,g in costs:
            red, blue, green = min(blue, green) + r, min(red,green) + b, min(red,blue) + g
        
        return min(red,blue,green)
        
        
        
#         if not costs: return 0
#         memo = {} # key: (house, color) val = costs
        
#         def paint_costs(house, color):
#             if (house, color) in memo:
#                 return memo[(house,color)]
#             if house >= len(costs): return 0
            
#             total_cost = costs[house][color]
            
#             if color == 0:
#                 total_cost += min(paint_costs(house+1, 1), paint_costs(house+1, 2))
#             elif color == 1:
#                 total_cost += min(paint_costs(house+1, 0), paint_costs(house+1, 2))
#             else:
#                 total_cost += min(paint_costs(house+1, 0), paint_costs(house+1, 1))
            
#             memo[(house, color)] = total_cost
#             return total_cost
        
#         return min(paint_costs(0,0), paint_costs(0,1), paint_costs(0,2))

        
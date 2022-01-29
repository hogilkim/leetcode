class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
         
        costs = 0
        stick_1 = stick_2 = 0
        
        while sticks:
            stick_1 = heapq.heappop(sticks)
            if sticks: stick_2 = heapq.heappop(sticks)
            else: return costs
            
            new_stick = stick_1 + stick_2
            costs += new_stick
            
            heapq.heappush(sticks, new_stick)
        
        return costs
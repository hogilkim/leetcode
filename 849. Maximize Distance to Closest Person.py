class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        empty_seats = []
        
        for idx, empty in enumerate(seats):
            if empty: empty_seats.append(idx)
        
        
        if len(empty_seats) == 1:
            return max(empty_seats[0], len(seats)-1-empty_seats[0])
        
        max_dis = 0
        
        for i in range(len(empty_seats)-1):
            max_dis = max(max_dis, (empty_seats[i+1] - empty_seats[i])//2)
        
        if not seats[0]:
            max_dis = max(max_dis, empty_seats[0])
        if not seats[-1]:
            max_dis = max(max_dis, len(seats) - empty_seats[-1]-1)
        
        return max_dis
        
        
                
                
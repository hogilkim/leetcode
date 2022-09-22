class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        times = sorted(times)
        
        l= 0
        r = min_time = totalTrips * times[-1]
        
        while l < r:
            mid = (l+r)//2
            trips = self.calc_trips(times, mid)
            if totalTrips <= trips: min_time = min(min_time, mid)
            
            if trips < totalTrips:
                l = mid + 1
            else:
                r = mid
        
        return l
            
    
    def calc_trips(self, times, t):
        trips = 0
        for time in times:
            if t < time: break
            trips += t//time
            
        return trips
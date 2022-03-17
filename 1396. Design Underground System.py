class UndergroundSystem:

    def __init__(self):
        # key: id, val: [station, checkin_time]
        self.checkins = {} 
        
        # key: (startStation, endStation) val: [total_times, nums]
        self.times = {} 
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, checkin_time = self.checkins[id]
        if (startStation, stationName) not in self.times:
            self.times[(startStation, stationName)] = [0, 0]
        self.times[(startStation, stationName)][0] += t - checkin_time
        self.times[(startStation, stationName)][1] += 1
        
        del self.checkins[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, nums = self.times[(startStation, endStation)]
        return total_time/nums


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
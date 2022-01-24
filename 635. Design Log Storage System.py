# solve again
class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        index = {"Year":4, "Month":7, "Day":10, "Hour":13, "Minute":16, "Second":19}[granularity]
        return [i for i, time in self.logs \
                if start[:index]<= time[:index] <= end[:index]]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
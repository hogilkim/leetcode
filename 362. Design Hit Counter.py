import collections
class HitCounter:

    def __init__(self):
        self.records = collections.deque([])

    def hit(self, timestamp: int) -> None:
        self.records.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.records and timestamp - self.records[0] >= 300:
            self.records.popleft()
        
        return len(self.records)
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
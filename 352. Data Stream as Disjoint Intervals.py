class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        l, r = 0, len(self.intervals)-1
        while l <= r:
            mid = (l+r)//2
            if self.intervals[mid][0] <= value <= self.intervals[mid][1]: return
            elif value < self.intervals[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        pos = l
        self.intervals.insert(pos, [value,value])
        if pos + 1 < len(self.intervals) and self.intervals[pos+1][0] == value + 1:
            self.intervals[pos][1] = self.intervals[pos+1][1]
            del self.intervals[pos+1]
        if pos - 1 >= 0 and self.intervals[pos-1][1] == value - 1:
            self.intervals[pos][0] = self.intervals[pos-1][0]
            del self.intervals[pos-1]


    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
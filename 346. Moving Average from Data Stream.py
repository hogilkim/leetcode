# Sep 30, 2026 346
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.datalist = []
        self.head = 0
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.datalist) >= self.size:
            self.total = self.total - self.datalist[self.head] + val
            self.datalist[self.head] = val
            self.head = (self.head + 1) % self.size
        else:
            self.datalist.append(val)
            self.total += val
        return self.total / len(self.datalist)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.curr_left = 0
        self.curr_right = 0
        self.arr = []

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.curr_right += 1
        if (self.curr_right - self.curr_left) > self.size:
            self.curr_left += 1
        return sum(self.arr[self.curr_left : self.curr_right + 1]) / (
            self.curr_right - self.curr_left
        )


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

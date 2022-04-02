class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.curr_left = 0
        self.curr_right = 0
        self.arr = []

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.curr_right += 1
        if (self.curr_right - self.curr_left) > self.size: self.curr_left += 1
        return sum(self.arr[self.curr_left:self.curr_right + 1]) / (self.curr_right - self.curr_left )


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
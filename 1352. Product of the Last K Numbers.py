class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.last_zero = -1
    def add(self, num: int) -> None:
        if not num: self.last_zero = len(self.nums)
        if not self.nums or not self.nums[-1]: self.nums.append(num)
        else:
            self.nums.append(self.nums[-1]*num)

    def getProduct(self, k: int) -> int:
        start_idx = len(self.nums) - k
        if self.last_zero >= start_idx: return 0
        elif start_idx == 0 or self.nums[start_idx-1] == 0: return self.nums[-1]
        return self.nums[-1] // self.nums[start_idx-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
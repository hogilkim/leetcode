class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_by_range = []
        total_sum = 0
        for num in nums:
            total_sum += num
            self.sum_by_range.append(total_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left >0:
            return self.sum_by_range[right] - self.sum_by_range[left-1]
        else:
            return self.sum_by_range[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
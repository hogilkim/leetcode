# solve again Jan 21, 2024 259
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        l = 0
        res = 0

        for l in range(len(nums)-2):
            r = len(nums)-1
            m = l + 1
            while m < r:
                three_sum = nums[l] + nums[r] + nums[m]
                if three_sum < target:
                    res += r - m
                    m += 1
                else:
                    r -= 1
        
        return res



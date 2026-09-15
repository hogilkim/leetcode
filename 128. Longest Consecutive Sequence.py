# solve again
# Sep 15, 2026 128
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0

        nums = set(nums)
        while nums:
            curr = nums.pop()
            inc = curr + 1
            dec = curr - 1
            currlen = 1
            while inc in nums:
                nums.remove(inc)
                inc += 1
                currlen += 1
            while dec in nums:
                nums.remove(dec)
                dec -= 1
                currlen += 1
            max_len = max(max_len, currlen)

        return max_len


# solve again
# second attempt - Jan 17, 2022
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_len = 0

        while nums:
            inc = dec = nums.pop()

            while inc + 1 in nums:
                inc += 1
                nums.remove(inc)
            while dec - 1 in nums:
                dec -= 1
                nums.remove(dec)

            max_len = max(max_len, inc - dec + 1)

        return max_len


# O(nlogn) solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(list(set(nums)))

        consequtive_num = 1
        max_consequtive_num = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                consequtive_num += 1
            else:
                consequtive_num = 1
            max_consequtive_num = max(max_consequtive_num, consequtive_num)

        return 0 if len(nums) == 0 else max_consequtive_num

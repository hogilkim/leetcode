# Sep 2, 2026 217-4
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# Nov 14, 2023 217-3


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# solved Oct 30, 2022
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums) > len(nums_set):
            return True
        return False

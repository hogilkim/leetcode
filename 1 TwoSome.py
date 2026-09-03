# Sep 3, 2026 1-3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        # for loop
        for idx, num in enumerate(nums):
            # key: element value: index
            # check in dic, is target - num there?
            if target - num in dic:
                # if so, return
                return [dic[target - num], idx]
            # store current num and index
            dic[num] = idx


# Nov 5, 2023
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()

        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], idx]
            else:
                dic[num] = idx


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solved twice, success
        seenMap = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in seenMap:
                return [seenMap[diff], index]
            seenMap[value] = index

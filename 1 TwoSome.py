# Nov 5, 2023 
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()

        for idx, num in enumerate(nums):
            if target-num in dic: return [dic[target-num], idx]
            else: dic[num]=idx

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solved twice, success
        seenMap = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seenMap:
                return [seenMap[diff], index]
            seenMap[value] = index
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solved twice, success
        seenMap = {}
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in seenMap:
                return [seenMap[diff], index]
            seenMap[value] = index
            
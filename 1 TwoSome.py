class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seenMap = {}
        
        for i, value in enumerate(nums):
            diff = target - value
            if diff in seenMap:
                return [seenMap[diff], i]
            seenMap[value] = i
        return
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums_len = len(nums)
        nums=set(sorted(nums))
        return [i for i in range(1, nums_len+1) if i not in nums]
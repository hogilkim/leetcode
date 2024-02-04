class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [idx for idx, num in enumerate(sorted(nums)) if num==target]
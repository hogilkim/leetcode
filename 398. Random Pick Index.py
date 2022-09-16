from collections import defaultdict
from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.dictionary = defaultdict(list)
        
        for idx, num in enumerate(nums):
            self.dictionary[num].append(idx)

    def pick(self, target: int) -> int:
        return self.dictionary[target][randint(0,len(self.dictionary[target])-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
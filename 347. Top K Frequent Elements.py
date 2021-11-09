import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums).items()
        sorted_counter = sorted(counter, key = lambda pair: pair[1], reverse = True)
        result = []
        for i in range(k):
            result.append(sorted_counter[i][0])
            

        return result
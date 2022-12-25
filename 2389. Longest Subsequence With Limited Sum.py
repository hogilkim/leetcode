import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        preSum = [0]

        for n in sorted(nums):
            preSum.append(preSum[-1] + n)
        
        res = [bisect.bisect_right(preSum, query)-1 for query in queries]
        
        return res
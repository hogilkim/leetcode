# solve again
# Oct 5, 2026 560-2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        count = 0
        currsum = 0
        for num in nums:
            currsum += num
            diff = currsum - k
            count += prefix_map.get(diff, 0)
            prefix_map[currsum] = 1 + prefix_map.get(currsum, 0)
        return count


# solve again
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = 0
        prefix_sum = {0: 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)

        return res

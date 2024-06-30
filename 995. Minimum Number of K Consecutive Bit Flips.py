from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queue = deque([])
        res = 0

        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.popleft()

            if (len(queue) + nums[i]) % 2 == 0:
                if i + k > len(nums): return -1
                queue.append(i)
                res += 1
        
        return res
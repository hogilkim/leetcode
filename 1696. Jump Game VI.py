
# deque dp solution
import collections
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        deque = collections.deque([(nums[0],0)])
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            while deque[0][1] < i-k : deque.popleft()
            
            dp[i] = nums[i] + deque[0][0]
            
            while deque and deque[-1][0] < dp[i]:
                deque.pop()
            deque.append((dp[i],i))
        
        return dp[-1]


# max heap dp solution
import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return nums[0]
        max_heap = [(-nums[0], 0)]
        heapq.heapify(max_heap)
        
        for i in range(1, len(nums)):
            while max_heap[0][1] < i-k: heapq.heappop(max_heap)
            
            curr_max = max_heap[0][0]
            heapq.heappush(max_heap,(curr_max-nums[i], i))
            if i == len(nums) -1: return -(curr_max - nums[i])
        
        
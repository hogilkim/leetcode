class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        maxSum = float('-inf')
        minSum = float('inf')

        currMaxSum = float('-inf')
        currMinSum = float('inf')

        for num in nums:
            totalSum += num
            currMaxSum = max(currMaxSum + num, num)
            currMinSum = min(currMinSum + num, num)

            maxSum = max(maxSum, currMaxSum)
            minSum = min(minSum, currMinSum)
        
        if totalSum == minSum: return maxSum
        return max(maxSum, totalSum-minSum)

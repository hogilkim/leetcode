class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        res = 1
        maxSum -= n
        max_left = index
        max_right = n - index - 1
        left = right = 0

        while maxSum > 0:
            res += 1
            left_sum = min(max_left, left)
            right_sum = min(max_right, right)
            left += 1
            right += 1

            maxSum -= (1+left_sum + right_sum)

            if left_sum == max_left and right_sum == max_right:
                break
        
        if maxSum > 0:
            res += maxSum // n
        
        return res if maxSum >= 0 else res - 1



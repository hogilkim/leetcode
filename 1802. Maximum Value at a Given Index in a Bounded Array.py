# Solve again Jan 31, 2024 1802-2
class Solution:
    def getSum(self, peak, index, n):
        left_val = max(peak - index, 0) # left min val
        right_val = max(peak - (n - index - 1), 0) # right min val
        # sum of each side: Sn = n/2 * (a1 + a2)
        res = ( (peak + left_val) * (peak - left_val + 1) + (peak + right_val) * (peak - right_val + 1) ) // 2
        return res - peak


    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        left, right = 0, maxSum

        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(mid, index, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left + 1
    

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



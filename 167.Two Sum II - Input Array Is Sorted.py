# Sep 4, 2026 167-2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [l + 1, r + 1]
            elif twosum < target:
                l += 1
            else:
                r -= 1
        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

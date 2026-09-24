# solve again
# Sep 23, 2026 74-2
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        mid = -1
        while top <= bottom:
            mid = (bottom + top) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break

        search_list = matrix[mid]

        l, r = 0, len(search_list) - 1
        while l <= r:
            mid = (l + r) // 2

            if search_list[mid] < target:
                l = mid + 1
            elif search_list[mid] > target:
                r = mid - 1
            else:
                return True

        return False


# solve again
# fisrt attempt - Jan 11
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break

        nums = matrix[mid]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if target <= nums[mid]:
                right -= 1
            else:
                left += 1

        return False

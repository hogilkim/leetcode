# Oct 2, 2026 34-3
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]
        # bisect left
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        left = l
        if len(nums) == l or nums[l] != target:
            return [-1, -1]

        # bisect right
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        right = l
        return [left, right - 1]


# Second: July 24
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        left = l
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [left, r] if left <= r else [-1, -1]


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         def searchLeft(x):
#             l, r = 0, len(nums)-1

#             while l<=r:
#                 mid = (l+r)//2

#                 if x > nums[mid]: l = mid + 1
#                 else: r = mid - 1
#             return l

#         def searchRight(x):
#             l, r = 0, len(nums)-1
#             while l<=r:
#                 mid = (l+r)//2

#                 if x < nums[mid]:
#                     r = mid - 1
#                 else: l = mid + 1

#             return r

#         tar = target
#         l = searchLeft(tar)
#         r = searchRight(tar)

#         return [l,r] if l<=r else [-1,-1]

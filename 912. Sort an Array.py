class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = (len(arr)) // 2

            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            i = j = k = 0
            res = [0] * (len(left) + len(right))

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res[k] = left[i]
                    i += 1
                else:
                    res[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                res[k] = left[i]
                k += 1
                i += 1
            while j < len(right):
                res[k] = right[j]
                j += 1
                k += 1
            return res

        return mergesort(nums)

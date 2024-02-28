# Solve again
# Feb 27, 2024 179
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        def mergeSort(array):
            if len(array)>1:
                half = len(array)//2
                left = array[:half]
                right = array[half:]

                mergeSort(left)
                mergeSort(right)

                i = j = k = 0

                while i < len(left) and j < len(right):
                    if left[i] + right[j] > right[j] + left[i]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1
                
                while j < len(right):
                    array[k] = right[j]
                    j += 1
                    k += 1
        mergeSort(nums)
        res = "".join(nums)
        if int(res) == 0: return "0"
        return res
# Dec 7, 2023 75-2 solve again
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, mid, r = 0, 0, len(nums)-1

        while mid <= r:
            print(l,mid,r,nums)
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                mid += 1
                l += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1

# solve again
# first attempt - Jan 15, 2022
import collections
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # solve again.
        
        left, right = 0, len(nums)-1
        while left < right - 1:
            mid = (left + right)//2
            
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            if nums[mid] > nums[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] >= nums[right] else right
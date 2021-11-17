class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right,middle = 0, len(nums)-1, int(len(nums)/2)
        
        min_val = 5001
        while left <= right:
            if nums[left] < nums[right]:
                min_val = min(min_val, nums[left])
                break
            
            middle = int((left+right)/2)
            if nums[middle]  < nums[left]:
                min_val = min(min_val, nums[middle])
                right = middle - 1
                middle = int(right - left)/2
            else:
                min_val = min(min_val, nums[middle])
                left = middle + 1
                middle = int(right - left)/2
            
        return min_val
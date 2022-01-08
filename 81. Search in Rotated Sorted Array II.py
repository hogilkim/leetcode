# solve again
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            while nums[l] == nums[mid] and l < mid:
                l += 1
            while nums[r] == nums[mid] and r > mid:
                r -= 1
            # first half sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # second half sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        
        return False
# second attempt Jan 9 - solve again
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_num = 5000
        while l <= r:
            if nums[l] < nums[r]:
                return min(min_num, nums[l])
            mid = (l+r) // 2
            min_num = min(min_num, nums[mid])
            
            # 2 3 4 5 6 7 0 1
            # left sorted
            if nums[l] <= nums[mid]:
                    l = mid + 1
                    
            # 6 7 0 1 2 3 4 5
            else:
                    r = mid - 1
        
        return min_num
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
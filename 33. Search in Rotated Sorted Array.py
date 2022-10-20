# Third time. solve again.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            
            if nums[l] <= nums[mid]:
                
                if nums[l] <= target and target < nums[mid]: r = mid - 1
                else: l = mid + 1
            
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else: r = mid - 1
                
                    
        
        return -1
        
# second time. Solved!
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            print(mid)
            if nums[mid] == target:
                return mid
            # left sorted
            # 1 2 3 4 5 6 0
            if nums[l] <= nums[mid]:
                # target on the left
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                # target on the right
                else:
                    l = mid + 1
            
            
            # right sorted
            # 4 5 0 1 2 3 
            else:
                # target on the right
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                
                # target on the left
                else:
                    r = mid - 1
        
        return -1
        
class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            # 2 3 4 '5' 6 7 0 1
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]: 
                    left = mid + 1
                else:
                    right = mid - 1

            # 6 7 0 '1' 2 3 4 5      
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                    
                else:
                    left = mid + 1
        return -1
    
    
    
    
    
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        
        prev = 0
        for pivot, num in enumerate(nums):
            left += prev
            right -= num
            
            if left == right: return pivot
            

            prev = num
        
        
        return -1
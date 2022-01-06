class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        closest = float('inf')
        
        for i in range(len(nums)):
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if abs(three_sum - target) < diff:
                    diff = abs(three_sum - target)
                    closest = three_sum
                
                if three_sum > target:
                    right -=1
                else:
                    left += 1
        
        return closest
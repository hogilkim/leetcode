# second attempt - Oct 7, 2022 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        answer = 0
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            
            if i>0 and nums[i] == nums[i-1]: continue
            
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if abs(target-threeSum)<diff:
                    answer = threeSum
                    diff = abs(target-threeSum)

                if threeSum < target:
                    l += 1
                else:
                    r -= 1
        
        return answer

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
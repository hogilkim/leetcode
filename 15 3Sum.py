class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        a_history = []
        for i in range(len(nums)-2):
            if nums[i] in a_history:
                continue
            a = nums[i]
            a_history.append(a)
            
            target = (-1)*a
            left = i + 1
            right = len(nums)-1
            print(a)
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] == target:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    
        return result
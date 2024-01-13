#Jan 13, 2024 2242
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        operations = 0
        while l < r:
            if nums[l] < nums[r]:
                nums[l+1] += nums[l]
                l += 1
                operations += 1
            elif nums[l] > nums[r]:
                nums[r-1] += nums[r]
                r -= 1
                operations += 1
            else:
                l+=1
                r-=1
        
        return operations
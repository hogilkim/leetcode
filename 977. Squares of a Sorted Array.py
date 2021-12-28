class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l, r = 0, len(nums)-1
        
        answer = []
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            
            if left > right:
                answer.append(left**2)
                l += 1
            else:
                answer.append(right**2)
                r -= 1
        
        return reversed(answer)
        
#         for i in range(len(nums)):
#             nums[i] = nums[i]**2
            
#         return sorted(nums)
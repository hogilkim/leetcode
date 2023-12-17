# solve again
# Dec 17, 11-3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0

        while l < r:
            max_area = max( max_area, min(height[l], height[r]) * (r-l) )

            if height[l] < height[r]:
                l += 1
            else: r -= 1
        
        return max_area

# solved
# second attempt Jan 17, 2022
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        
        max_area = 0
        
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right - left) )
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
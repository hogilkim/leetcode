# solve again
# second attempt - Jan 20, 2022

class Solution:
    def trap(self, height: List[int]) -> int:

        
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        
        total_water = 0
        
        while l<r:
            if left_max <= right_max:
                l+=1
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
        
        return total_water
        
        
class Solution:
    def trap(self, height: List[int]) -> int:
        # solve again
        if not height: return 0
        left_ptr, right_ptr = 0, len(height)-1
        left_max, right_max = height[left_ptr], height[right_ptr]
        
        total_water = 0
        
        while left_ptr < right_ptr:
            if left_max <= right_max:
                left_ptr += 1
                left_max = max(left_max, height[left_ptr])
                total_water += left_max - height[left_ptr]
            else:
                right_ptr -= 1
                right_max = max(right_max, height[right_ptr])
                total_water += right_max - height[right_ptr]
        return total_water
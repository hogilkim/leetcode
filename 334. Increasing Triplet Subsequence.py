class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_small = second_small = float('inf')
        
        for num in nums:
            if num <= first_small:
                first_small = num
            elif num <= second_small:
                second_small = num
            else:
                return True
        
        return False
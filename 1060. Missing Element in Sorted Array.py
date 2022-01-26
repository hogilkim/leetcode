class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        potential = nums[0] + 1
        
        for num in nums[1:]:
            while potential < num:
                
                k -= 1
                if k == 0:
                    return potential
                potential += 1
            potential+=1
        
        return potential + k - 1
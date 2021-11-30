class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        bigger_val = 0
        smaller_val = 0
        
        for num in nums:
            temp = max(bigger_val, num + smaller_val)
            smaller_val = bigger_val
            bigger_val = temp
            
        
        return bigger_val
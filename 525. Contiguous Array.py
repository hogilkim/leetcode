class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        table = {count:0}
        
        for i, num in enumerate(nums):
            idx = i+1
            if num == 0: count -= 1
            elif num == 1: count += 1
            
            if count in table:
                max_length = max(max_length, idx - table[count])
            else:
                table[count] = idx
            
            
        
        return max_length
            
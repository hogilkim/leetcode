class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        pre_ones = -1
        curr_ones = 0
        max_len = 0
        
        for num in nums:
            if num == 0:
                pre_ones, curr_ones = curr_ones, 0
            else:
                curr_ones += 1
            max_len = max(max_len, pre_ones + 1 + curr_ones)
        
        
        return max_len
        
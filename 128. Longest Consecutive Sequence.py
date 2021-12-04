class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(list(set(nums)))
        
        consequtive_num = 1
        max_consequtive_num = 1        
        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1] + 1):
                consequtive_num += 1
            else:
                consequtive_num = 1
            max_consequtive_num = max(max_consequtive_num, consequtive_num)
                
        return 0 if len(nums)==0 else max_consequtive_num
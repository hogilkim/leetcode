# solve again
# second attempt - Jan 17, 2022
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        max_len = 0
        
        while nums:
            inc = dec = nums.pop()
            
            while inc + 1 in nums:
                inc += 1
                nums.remove(inc)
            while dec - 1 in nums:
                dec -= 1
                nums.remove(dec)
            
            max_len = max(max_len, inc - dec + 1)
        
        return max_len

# O(nlogn) solution
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
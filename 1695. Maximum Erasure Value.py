class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        subarr_set = set()
        
        max_score = 0
        curr_sum = 0
        l = 0
        
        for idx, num in enumerate(nums):
            if num in subarr_set:
                while l < idx and num != nums[l]:
                    curr_sum -= nums[l]
                    subarr_set.remove(nums[l])
                    l+= 1
                if idx != l:
                    curr_sum -= nums[l]
                    subarr_set.remove(nums[l])
                    l+= 1
            subarr_set.add(num)
            curr_sum += num
            
            max_score = max(max_score, curr_sum)
        
        
        return max_score
                    
            
            
            
        
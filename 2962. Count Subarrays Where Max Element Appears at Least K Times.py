# Mar 30, 2024 2962
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num_count = 0
        max_num = max(nums)

        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == max_num: max_num_count += 1

            while max_num_count > k and l < r:
                if nums[l] == max_num:
                    max_num_count -= 1
                    l += 1
            
            while max_num_count == k and l < r and nums[l] != max_num:
                l += 1
            
            if max_num_count == k:
                res += l + 1
        
        return res
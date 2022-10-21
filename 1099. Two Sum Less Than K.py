class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        # not sorted, k can be any random number
        
        nums = sorted(nums)
        
        # two ptrs l r
        l, r = 0, len(nums)-1
        
        max_twosum = 0
        
        # while l<r:
        while l<r:
            # if l+r < k:
            if nums[l] + nums[r] < k:
                
                # save max result
                max_twosum = max(max_twosum, nums[l] + nums[r])
                l+= 1
            
            else:
                r -= 1
            
        
        return max_twosum if max_twosum>0 else -1
        
        

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums)-1
        res = -1
        nums = sorted(nums)
        while l < r:
            if nums[l] + nums[r] < k:
                res = max(res, nums[l] + nums[r])
                l += 1
            else:
                r -= 1
        return res
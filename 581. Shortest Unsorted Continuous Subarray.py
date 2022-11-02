class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        l, r = 0, len(nums)-1
        
        while l < len(nums)-1 and nums[l] <= nums[l+1]: l += 1
        while r > 0 and nums[r] >= nums[r-1]: r -= 1
        
        if l>r: return 0
        
        minnum, maxnum = float('inf'), float('-inf')
        
        for i in range(l,r+1):
            minnum = min(minnum, nums[i])
            maxnum = max(maxnum, nums[i])
        
        while l>0 and nums[l-1] > minnum: l -= 1
        while r < len(nums)-1 and nums[r+1] < maxnum: r+=1
        
        return r-l+1
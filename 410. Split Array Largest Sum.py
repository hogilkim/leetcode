class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums)
        
        while low < high:
            divisions, split_sum = 1, 0
            mid = (low+high)//2
            for num in nums:
                if split_sum + num <= mid:
                    split_sum += num
                else:
                    divisions += 1
                    split_sum = num
            
            if divisions <= m: high = mid
            else: low = mid + 1
        
        return low
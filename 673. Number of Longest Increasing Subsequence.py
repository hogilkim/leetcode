# solve again
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis_lengths = [1] * len(nums)
        count = [1] * len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(len(nums)-1, i , -1):
                if nums[i] < nums[j]:
                    if lis_lengths[i] - 1 < lis_lengths[j]:
                        lis_lengths[i] = lis_lengths[j] + 1
                        count[i] = count[j]
                    elif lis_lengths[i] - 1 == lis_lengths[j]:
                        count[i] += count[j]
                        
        print(lis_lengths)
        print(count)
        
        max_lis = max(lis_lengths)
        max_lis_count = 0
        for k in range(len(lis_lengths)):
            if max_lis == lis_lengths[k]:
                max_lis_count += count[k]
        
        return max_lis_count
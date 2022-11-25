class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def moreThanKPairs(guess):
            count = 0
            i = 0
            j = 1
            while i < len(nums):
                while j < len(nums) and nums[j] - nums[i] <= guess:
                    j += 1

                count += j - i - 1
                if count >= k: break
                i += 1
            # print(count, k)
            return count >= k
            
        nums.sort()
        low, high = 0, nums[-1]-nums[0]
        
        while low < high:
            mid = (low+high)//2
            
            if moreThanKPairs(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
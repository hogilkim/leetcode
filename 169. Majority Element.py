import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Third solution time: O(n), space: O(1)
        candidate, counter = nums[0], 0
        for num in nums:
            if num == candidate:
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                candidate = num
                counter = 0
        
        return candidate
        
        # one line solution time: O(n logn), space: O(1)
        # return sorted(nums)[len(nums)//2]
    
        # first solution time: O(n) Space: O(1) ~ O(n)
        # counter = collections.Counter(nums)
        # nums_uniq = list(set(nums))
        # for num in nums_uniq:
        #     if counter[num] > len(nums)//2:
        #         return num
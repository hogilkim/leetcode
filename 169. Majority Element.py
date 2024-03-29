# Nov 14, 2023 169-2

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = nums[0]
        count = 0

        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                candidate = num
                count = 0
        
        return candidate

        # counter = Counter(nums)
        # LEN = len(nums)

        # for key in counter:
        #     if counter[key] > LEN/2:
        #         return key
        
        # return

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
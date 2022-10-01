from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        
        left1 = left2 = 0
        
        res = 0
        
        for num in nums:
            counter[num] += 1
            
            if len(counter) == k + 1:
                del counter[nums[left2]]
                left2 += 1
                left1 = left2
            
            if len(counter) == k:
                while counter[nums[left2]]>1:
                    counter[nums[left2]] -= 1
                    left2 += 1
                
                res += left2 - left1 + 1
        
        return res
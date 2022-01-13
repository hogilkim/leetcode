# solve again
# First attempt - Jan 12, 2022
# honestly, x 100% understood
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer, mask = 0,0
        
        for i in range(32,-1,-1):
            mask |= 1<<i
            found = {num & mask for num in nums}
            start = answer | 1<<i
            
            if any(start^pref in found for pref in found):
                answer = start
        return answer
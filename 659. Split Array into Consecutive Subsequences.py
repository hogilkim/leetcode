import collections
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        nxt = collections.defaultdict(int)
        
        for num in nums:
            if not freq[num]: continue
            
            if nxt[num]:
                nxt[num] -= 1
                nxt[num+1] += 1
            
            elif freq[num+1] and freq[num+2]:
                freq[num+1] -= 1
                freq[num+2] -= 1
                nxt[num+3] += 1
            
            else: return False
            
            freq[num] -= 1
        
        return True
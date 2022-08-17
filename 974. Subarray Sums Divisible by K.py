import collections
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        acc = 0
        
        accdic = collections.defaultdict(int)
        accdic[0]+=1
        res = 0
        for num in nums:
            acc = (acc+num)%k
            res += accdic[acc]
            accdic[acc] += 1
        
        return res
            

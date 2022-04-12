import collections
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        
        dic = collections.defaultdict(list)
        
        for key in counter.keys():
            dic[counter[key]].append(key)
        
        res = []
        for key in sorted(dic.keys()):
            for val in sorted(dic[key], reverse=True):
                for freq in range(key):
                    res.append(val)
        
        return res
        
        
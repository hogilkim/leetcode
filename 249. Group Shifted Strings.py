import collections
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # key: (diffs) val: string
        # time: O(n*k) where k:avg num of chars in strings space: O(n)
        
        dic = defaultdict(list)
        
        for string in strings:
            if len(string) == 1:
                dic[(0)].append(string)
            else:
                diffs = []
                for i in range(1, len(string)):
                    diff = ord(string[i]) - ord(string[i-1])
                    if diff < 0: diff += 26
                    diffs.append(diff)
                
                dic[tuple(diffs)].append(string)
        
        
        res = []
        
        for key in dic.keys():
            res.append(dic[key])
        
        return res
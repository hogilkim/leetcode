from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ga = defaultdict(list)
        
        for word in strs:
            ga[tuple(sorted(list(word)))].append(word)
        
        return ga.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        counter_map = defaultdict(list)
        for string in strs:
            # sort by Counter's key
            count = tuple(sorted(Counter(string).items()))
            counter_map[count].append(string)

        return counter_map.values()
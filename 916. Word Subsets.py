import collections
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2_union = collections.defaultdict(int)
        for word in words2:
            temp_counter = collections.Counter(word)
            for key in temp_counter:
                word2_union[key] = max(word2_union[key], temp_counter[key])
        
        res = []
        
        for word in words1:
            temp_counter = collections.Counter(word)
            res.append(word)
            for key in word2_union:
                if key not in temp_counter or temp_counter[key] < word2_union[key]: 
                    res.pop(); break;
        
        return res
                
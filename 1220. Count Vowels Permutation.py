import collections
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dic = {
            "a":['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        prev_counter = {"a":1, "e":1,"i":1,"o":1,"u":1}
        
        
        for _ in range(n-1):
            curr_counter = collections.defaultdict(int)
            for key, freq in prev_counter.items():
                for char in dic[key]:
                    curr_counter[char] += freq
            prev_counter = curr_counter
        
        res = 0
        
        for key, val in prev_counter.items():
            res += val
        
        return res % (10**9+7)
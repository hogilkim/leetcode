# solve again
# Dec 20, 2023 76
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = Counter(t), Counter()
        s_counter = Counter(s)
        
        for key in need.keys():
            if key not in s_counter or need[key] > s_counter[key]: return ""


        res = s
        l = 0
        match = 0

        for r, char in enumerate(s):
            if char in need:
                have[char] += 1
                match += have[char] == need[char]

            while match==len(need) and l <= r:
                res = min(res, s[l:r+1], key=len)
                if s[l] in need:
                    match -= need[s[l]] == have[s[l]]
                    have[s[l]] -= 1
                    
                l += 1
        
        return res
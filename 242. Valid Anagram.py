# Sep 3, 2026 242-3
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter

        s_counter = Counter(s)
        t_counter = Counter(t)

        for key in s_counter:
            if key not in s_counter:
                return False
            if s_counter[key] != t_counter[key]:
                return False
        return True


import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        LEN = len(s)
        counter = collections.Counter()

        for i in range(LEN):
            counter[s[i]] += 1
            counter[t[i]] -= 1

        for char in s:
            if counter[char] != 0:
                return False

        return True

        # return collections.Counter(s) == collections.Counter(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

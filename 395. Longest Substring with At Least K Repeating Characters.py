# Solved, but has better solution
# Jan 27, 2024 395
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s or k > len(s): return 0
        counter = Counter(s)

        for idx, char in enumerate(s):
            if counter[char] < k:
                return max(self.longestSubstring(s[:idx], k), self.longestSubstring(s[idx+1:], k))
        return len(s)

        # s_counter = Counter(s)
        # count = 0
        # visited = set()

        # def backtracking(l, r, counter):
        #     visited.add((l,r))
        #     nonlocal count
        #     while l < r and counter[s[l]] < k:
        #         counter[s[l]] -= 1
        #         l += 1
        #     while l < r and counter[s[r]] < k:
        #         counter[s[r]] -= 1
        #         r -= 1
        #     have_less_than_k = any( 0 < value < k for value in counter.values())
        #     if not have_less_than_k:
        #         count = max(count, r - l + 1)
        #         return
            
            
        #     if (l+1, r) not in visited and l+1 < r:
        #         counter[s[l]] -= 1
        #         backtracking(l+1, r, counter.copy())
        #         counter[s[l]] += 1

        #     if (l, r-1) not in visited and l < r - 1:
        #         counter[s[r]] -= 1
        #         backtracking(l, r-1, counter.copy())
        #         counter[s[r]] += 1
            
        # backtracking(0, len(s)-1, s_counter.copy())
        # return count
                
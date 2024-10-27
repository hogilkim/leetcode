# solve again
# Oct 27, 2024 1593
class Solution:
    def maxUniqueSplit(self, s: str) -> int:        
        max_len = 0
        sub_string_set = set()
        def backtracking(start):
            nonlocal max_len
            if start == len(s):
                max_len = max(max_len, len(sub_string_set))
                return
            
            for end in range(start+1, len(s)+1):
                substring = s[start:end]
                if substring not in sub_string_set:
                    sub_string_set.add(substring)
                    backtracking(end)
                    sub_string_set.remove(substring)

        backtracking(0)
        return max_len
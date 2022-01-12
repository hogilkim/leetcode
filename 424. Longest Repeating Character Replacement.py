# second attempt - Jan 11 2022
# solve again
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        curr_len = 0
        max_len = 0
        counter = {}
        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right], 0)
            curr_len += 1
            if curr_len - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
                curr_len -=1
            max_len = max(max_len, curr_len)
        
        return max_len
# try to solve again
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        curr_len = 0
        max_len = 0
        count = {}
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            curr_len += 1
            if curr_len - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                curr_len -= 1
            max_len = max(max_len, curr_len)
        return max_len
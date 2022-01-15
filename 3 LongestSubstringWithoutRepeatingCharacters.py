# solved
# second attempt - Jan 15, 2022
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, r = 0, 1
        
        substrings = set([s[0]])
        max_len = 1
        
        while r < len(s):
            if s[r] not in substrings:
                substrings.add(s[r])
            else:
                while s[l] != s[r]:
                    substrings.remove(s[l])
                    l+=1
                l += 1
            max_len = max(max_len, r-l+1)
            r+=1
            
            
        
        return max_len
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len = 0
        
        current_substring = ""
        current_len = 0
        for element in s:
            if element in current_substring:
                longest_len=max(current_len, longest_len)
                index = current_substring.index(element)
                current_substring += element
                current_substring = current_substring[index+1:]
                current_len = len(current_substring)
                
            else:
                current_substring += element
                current_len = len(current_substring)
        if current_len > longest_len:
            longest_len = current_len
        return longest_len
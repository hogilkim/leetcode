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
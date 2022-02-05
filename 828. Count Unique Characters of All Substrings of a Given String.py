#https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/129021/O(N)-Java-Solution-DP-Clear-and-easy-to-Understand
import collections
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        res=cur=0
        prevIdxs = [-1]*26
        uniq = [0]*26
        for i,c in enumerate(s):
            ic=ord(c)-ord('A')
            cur -= uniq[ic]
            uniq[ic] = i - prevIdxs[ic]
            cur += uniq[ic]
            prevIdxs[ic] = i
            res += cur        
        return res
            
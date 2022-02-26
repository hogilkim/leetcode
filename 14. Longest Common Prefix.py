class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_pref = strs[0]
        
        for word in strs[1:]:
            pref = ""
            
            for idx, char in enumerate(common_pref):
                if idx >= len(word) or char != word[idx]:
                    break
                pref += char
            common_pref = pref
        
        return common_pref
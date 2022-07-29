class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for word in words:
            if len(word) != len(pattern): continue
            conv_dict = {}
            temp = ""
            used = set()
            for idx, char in enumerate(word):
                if char not in conv_dict:
                    if pattern[idx] in used: break
                    conv_dict[char] = pattern[idx]
                    used.add(pattern[idx])
                temp += conv_dict[char]
            
            if temp == pattern: res.append(word)
        
        return res
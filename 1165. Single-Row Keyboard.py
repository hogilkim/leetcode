class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {}
        for idx, char in enumerate(keyboard):
            dic[char] = idx
        
        res = 0
        curr = 0
        
        for char in word:
            res += abs(dic[char]-curr)
            curr = dic[char]
        
        return res
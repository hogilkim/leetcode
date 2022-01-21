# solve again
# first attempt - Jan 20, 2022
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_dict = {}
        
        for word in words:
            word_dict[word] = 1

        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in word_dict:
                    word_dict[word] = max(word_dict[word], word_dict[prev]+1)
        return max(word_dict.values())
    
    
        
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)
        
        for char in s:
            
            temp = word_dict[char]
            word_dict[char] = []
            
            for subseq in temp:
                if len(subseq) == 1:
                    count += 1
                else:
                    word_dict[subseq[1]].append(subseq[1:])
                    
        return count
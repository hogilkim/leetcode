import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words: return []
        
        word_size = len(words[0])
        num_words = len(words)
        list_size = num_words * word_size
        
        word_counter = collections.Counter(words)
        res = []
        
        for i in range(len(s) - list_size + 1):
            word_dic = dict(word_counter)
            count = 0
            
            for j in range(i, i+list_size, word_size):
                sub_word = s[j:j+word_size]
                if sub_word in word_dic and word_dic[sub_word]>0:
                    word_dic[sub_word] -= 1
                    count += 1
                else: break
            if count == num_words: res.append(i)
        
        return res
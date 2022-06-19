# N: # of words L: avg length of words M: avg length of pref + suff
# Time to make Trie O(N*L^2) | search: O(M)
# Space: O(N*L^2)

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.idx_mark = '@'
        
        for idx, word in enumerate(words):
            word +='#'
            length = len(word)
            word += word
            for i in range(length):
                curr_trie = self.trie
                curr_trie[self.idx_mark] = idx
                for char in word[i:]:
                    if char not in curr_trie:
                        curr_trie[char] = {}
                    curr_trie = curr_trie[char]
                    curr_trie[self.idx_mark] = idx
    def f(self, prefix: str, suffix: str) -> int:

        curr_trie = self.trie
        for char in suffix+"#"+prefix:
            if char not in curr_trie: return -1
            curr_trie = curr_trie[char]
        
        return curr_trie[self.idx_mark]
        
# import collections
# class TrieNode:
#     def __init__(self, char):
#         self.char = char
#         self.next = {}
#         self.idxs = []
# class WordFilter:

#     def __init__(self, words: List[str]):
#         self.pref = TrieNode("")
#         self.suff = TrieNode("")
#         for idx, word in enumerate(words):
#             self.create_trie(word, idx, self.pref)
#             self.create_trie(word[::-1], idx, self.suff)

#     def f(self, prefix: str, suffix: str) -> int:
#         pref_idxs, suff_idxs = self.find_idxlist(prefix, self.pref), self.find_idxlist(suffix[::-1], self.suff)
#         if not pref_idxs or not suff_idxs: return -1 
        
#         pref, suff = pref_idxs.pop(), suff_idxs.pop()
#         while pref_idxs or suff_idxs:
#             if pref == suff: return pref
#             if not suff_idxs or (pref_idxs and pref>suff): pref = pref_idxs.pop()
#             else: suff = suff_idxs.pop()
        
#         return pref
        
    
#     def create_trie(self, word, idx, trie):
#         for char in word:
#             if char not in trie.next:
#                 trie.next[char] = TrieNode(char)
#             trie = trie.next[char]
#             trie.idxs.append(idx)
        
#     def find_idxlist(self, pref_or_suff, trie):
#         for char in pref_or_suff:
#             if char not in trie.next:
#                 return None
#             trie = trie.next[char]
            
#         return trie.idxs.copy()
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
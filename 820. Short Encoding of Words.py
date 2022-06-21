class TrieNode:
    def __init__(self):
        self.children = {}
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        words = sorted(words, reverse=True, key=len)
        trie_root = TrieNode()
        ends = []
        
        
        for word in words:
            node = trie_root
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            if not node.children: ends.append(len(word)+1)
                
        
        return sum(ends)
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    def construct(words):
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
            
        return root
        
    
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        root = TrieNode.construct(words)
        
        res = []
        for i in range(len(text)):
            curr = root
            
            for j in range(i, len(text)):
                if text[j] in curr.children:
                    curr = curr.children[text[j]]
                else:
                    break
                if curr.is_word:
                    res.append([i,j])
        
        return res
        
        
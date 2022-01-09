class Trie:
    def __init__(self):
        self.children = {}
        self.is_reached = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        root.is_reached = True
        
        for word in words:
            curr = root
            for i in range(len(word)):
                if word[i] not in curr.children:
                    curr.children[word[i]] = Trie()
                curr = curr.children[word[i]]
            curr.is_reached = True
        
        
        self.longest_word = ""
        def dfs(part, trie_node):
            if not trie_node.is_reached: 
                part = part[:-1]
                if len(self.longest_word) < len(part) or ( len(part) == len(self.longest_word) and part < self.longest_word):
                    self.longest_word = part
                return
            
            if not trie_node.children:
                if len(self.longest_word) < len(part) or ( len(part) == len(self.longest_word) and part < self.longest_word):
                    self.longest_word = part
                return
            
            for char in trie_node.children.keys():
                dfs(part+char, trie_node.children[char] )
        
        
        dfs("", root)
        return self.longest_word
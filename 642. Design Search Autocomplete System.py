from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.hotness = defaultdict(int)

class Trie:
    def __init__(self, sentences, times):
        self.rootTrie = TrieNode()
        self.currNode = self.rootTrie
        for sentence, time in zip(sentences, times):
            self.build(sentence, time)

    def search(self, char):
        if char == "#":
            self.currNode = self.rootTrie
            return {}
        elif self.currNode == None:
            return {}
        elif char not in self.currNode.children:
            self.currNode = None
            return {}
        
        self.currNode = self.currNode.children[char]
        return self.currNode.hotness
    
    def build(self, sentence, time):
        curr_trie = self.rootTrie
        for char in sentence:
            if char not in curr_trie.children:
                curr_trie.children[char] = TrieNode()
            curr_trie = curr_trie.children[char]
            curr_trie.hotness[sentence] += time

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie(sentences, times)
        self.currword = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.build(self.currword, 1)
            self.currword = ""
        else:
            self.currword += c
            
        hotness_dic = self.trie.search(c)
        if not hotness_dic: return []

        pre_res = [(hotness_dic[key], key) for key in hotness_dic.keys()]
        pre_res = sorted(pre_res, key=lambda x: (-x[0], x[1]))

        return [sentence for _, sentence in pre_res][:3]
            
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
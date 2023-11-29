# solved
# Third attempt - Nov 29, 2023 208-3
class TrieNode:
    def __init__(self):
        self.next = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        trienode = self.head

        for char in word:
            if char not in trienode.next:
                trienode.next[char] = TrieNode()
            trienode = trienode.next[char]
        
        trienode.isWord = True

    def search(self, word: str) -> bool:
        trienode = self.head
        for char in word:
            if char not in trienode.next: return False
            trienode = trienode.next[char]
        
        return trienode.isWord

    def startsWith(self, prefix: str) -> bool:
        trienode = self.head
        for char in prefix:
            if char not in trienode.next: return False
            trienode = trienode.next[char]
        return True
    
    
#solved
# second attempt - Jan 17, 2022
class TrieNode :
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not char in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode :
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char] 
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        if curr.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
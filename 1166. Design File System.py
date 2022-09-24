class TrieNode:
    def __init__(self, v=0):
        self.val = v
        self.children = {}
class FileSystem:

    def __init__(self):
        self.trie = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")[1:]
        trie = self.trie
        
        for p in paths[:-1]:
            if p not in trie.children: return False
            trie = trie.children[p]
        
        if paths[-1] in trie.children: return False
        
        trie.children[paths[-1]] = TrieNode(value)
        return True
        
    def get(self, path: str) -> int:
        
        paths = path.split("/")[1:]
        trie = self.trie
        for p in paths:
            if p not in trie.children: return -1
            trie = trie.children[p]
        
        return trie.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
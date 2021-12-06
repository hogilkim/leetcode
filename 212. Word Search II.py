class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        
        result, visited = set(), set()
        
        def dfs(row, col, node, word):
            if row < 0 or col < 0 or row >= ROWS or col >=COLS or board[row][col] not in node.children or (row, col) in visited:
                return
        
            # board[row][col] is in one if node.children
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWord:
                result.add(word)
            dfs(row+1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col-1, node, word)
            visited.remove((row, col))
            return
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        return list(result)
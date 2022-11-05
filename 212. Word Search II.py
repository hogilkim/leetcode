class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieroot = TrieNode()
        
        for word in words:
            node = trieroot
            
            for idx, char in enumerate(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if idx == len(word)-1:
                    node.word = word
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        ROW, COL = len(board), len(board[0])
        path = set()
        
        res = []
        
        def dfs(row, col, trienode):
            if trienode.word:
                res.append(trienode.word)
                trienode.word = None
            path.add((row,col))
            
            for rd, cd in directions:
                nr, nc = row+rd, col+cd
                if 0<=nr<ROW and 0<=nc<COL and (nr,nc) not in path and board[nr][nc] in trienode.children:
                    dfs(nr,nc,trienode.children[board[nr][nc]])
            
            path.remove((row,col))
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] in trieroot.children:
                    node = trieroot
                    dfs(r,c,node.children[board[r][c]])
        return res

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
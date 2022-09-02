"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        ROW, COL = len(grid), len(grid[0])
        def dfs(row, col, length):
            root = Node(grid[row][col], 1)
            elements = set()
            only_one = True
            for i in range(row, row+length):
                elements = elements.union(set(grid[i][col:col+length]))
                if len(elements) > 1:
                    only_one = False
                    break
            if only_one: return root
            
            half_len = length//2
            root.topLeft = dfs(row,col,half_len)
            root.topRight = dfs(row, col+half_len, half_len)
            root.bottomLeft = dfs(row+half_len,col,half_len)
            root.bottomRight = dfs(row+half_len, col+half_len, half_len)
            root.isLeaf = 0
            return root
        
        return dfs(0,0,ROW)
# third
from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowdic = defaultdict(list)
        coldic = defaultdict(list)
        
        for row, col in stones:
            rowdic[row].append((row,col))
            coldic[col].append((row,col))
            
        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))
            
            for row, col in rowdic[r]:
                if (row,col) not in visited:
                    dfs(row,col)
            
            for row, col in coldic[c]:
                if (row,col) not in visited:
                    dfs(row,col)
                    
        
        island = 0
        
        for row, col in stones:
            if (row,col) not in visited:
                dfs(row,col)
                island += 1
            
        return len(stones) - island

from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        row_map, col_map = defaultdict(list), defaultdict(list)
        stones_set = set()
        
        for r,c in stones:
            row_map[r].append((r,c))
            col_map[c].append((r,c))
            stones_set.add((r,c))
            
        
        # def dfs(r,c):
        def dfs(r,c):
            # remove (r,c) in stones_set
            stones_set.remove((r,c))
            
            # for loop through row_map[r]
            for nr, nc in row_map[r]:
                # if next r,c in stones_set:
                if (nr,nc) in stones_set:
                    dfs(nr,nc)
                    # dfs()
                    
            # for loop through col_map[c]
            for nr, nc in col_map[c]:
                # if next r,c in stones_set:
                if (nr,nc) in stones_set:
                    # dfs
                    dfs(nr,nc)
                    
                    
        groups = 0

        
        
        # for loop
        for r,c in stones:
            # dfs()
            if (r,c) in stones_set:
            # groups += 1
                dfs(r,c)
                groups+=1
        
        return len(stones) - groups
    
    
    # Time Complextiy: O(n) Space: O(n)

from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        # make hash map that shares same row and column
        row_map, col_map = defaultdict(list), defaultdict(list)
        stones_set = set()
        for r, c in stones:
            row_map[r].append((r,c))
            col_map[c].append((r,c))
            stones_set.add((r,c))
        # make set of stones
        
        
        
        def dfs(row, col):
            # remove the curr stone (row,col) from stoneset
            stones_set.remove((row,col))
            # call  dfs with same "row" using hashmap of same rows
            # for loop to go through stones with same row & call dfs
            for r, c in row_map[row]:
                if (r,c) in stones_set:
                    dfs(r,c)
            
            # call another dfs with same "col" using hash map of same col
            # ''
            for r, c in col_map[col]:
                if (r,c) in stones_set:
                    dfs(r,c)
        
        
        
        # variable "num_groups"
        num_groups = 0
        # call dfs and add num_groups 
        for r,c in stones:
            if (r,c) in stones_set:
                dfs(r,c)
                num_groups += 1
        
        # return length of stones - num_groups
        return len(stones) - num_groups
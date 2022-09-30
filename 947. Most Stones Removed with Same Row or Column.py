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
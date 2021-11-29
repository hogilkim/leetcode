class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pacific, atlantic = set(), set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r, c, reachable, prev_height):
            if (r,c) in reachable or r < 0 or c < 0 or c >= COLS or r >= ROWS or prev_height > heights[r][c]:
                return
            
            reachable.add((r,c))
            for r_dir, c_dir in directions:
                dfs(r+r_dir, c+c_dir, reachable, heights[r][c])
            
        
        for c in range(COLS):
            # pacific row
            dfs(0,c,pacific,heights[0][c])
            # atlantic row
            dfs(ROWS-1,c, atlantic, heights[ROWS-1][c])
            
        for r in range(ROWS):
            # pacific col
            dfs(r, 0, pacific, heights[r][0])
            # atlantic col
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
            
        
        result = []
        for c in range(COLS):
            for r in range(ROWS):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        return result
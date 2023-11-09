class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def search(row, col, prev_color):
            visited.add((row,col))
            if image[row][col] != prev_color: return
            image[row][col] = color
            for rd, cd in directions:
                nr, nc = row + rd, col + cd

                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited:
                    search(nr, nc, prev_color)
        
        search(sr, sc, image[sr][sc])

        return image
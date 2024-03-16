class Solution:
    def convert(self, s: str, numRows: int) -> str:
        EMPTY = " "
        if numRows == 1: return s
        conv_array = [ [EMPTY for _ in range(len(s))] for _ in range(numRows) ]
        row, col = 0, 0
        down = 1

        for char in s:
            conv_array[row][col] = char

            if down == 1:
                nr, nc = row+1, col
                if 0<=nr<numRows and 0<=nc<len(conv_array[0]):
                    row, col = nr, nc
                else:
                    down *= -1
                    row -= 1
                    col += 1
            
            else: #up
                nr, nc = row - 1, col + 1
                if 0<=nr<numRows and 0<=nc<len(conv_array[0]):
                    row, col = nr, nc
                else:
                    down *= -1
                    row += 1
        
        res = ""
        for r in range(numRows):
            for c in range(len(conv_array[0])):
                if conv_array[r][c] != EMPTY:
                    res += conv_array[r][c]
        return res
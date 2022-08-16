# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROW, COL = binaryMatrix.dimensions()
        leftmost = -1
        
        r, c = 0, COL-1
        
        while r < ROW and c >=0:
            if binaryMatrix.get(r,c) == 1:
                leftmost = c
                c -= 1
            else:r+=1
        
        return leftmost
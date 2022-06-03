class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(matrix), len(matrix[0])
        
        res = [ [matrix[0][i]] for i in range(COL) ]
        
        for item in matrix[1:]:
            for i in range(COL):
                res[i].append(item[i])
        
        return res
            
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        R1, C1 = len(mat1), len(mat1[0])
        R2, C2 = len(mat2), len(mat2[0])
        
        # R1 C1 R2 C2 -> R1 C2
        
        res = [[0]*C2 for _ in range(R1)]
        
        # c1 = r2
        for r1 in range(R1):
            for c2 in range(C2):
                for c1 in range(C1):
                    res[r1][c2] += mat1[r1][c1] * mat2[c1][c2]
        
        
        return res
                
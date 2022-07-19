import collections
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarrSumTarget(col_sum, target):
            preSum = 0
            cumulative = collections.defaultdict(int)
            total_subarr = 0
            cumulative[0] = 1
            
            for num in col_sum:
                preSum += num
                total_subarr += cumulative[preSum - target]
                cumulative[preSum] += 1
            return total_subarr
        
        ROW, COL = len(matrix), len(matrix[0])
        total_subarr = 0
        for r1 in range(ROW):
            sub_matrix = [0]*COL
            for r2 in range(r1,ROW):
                for c in range(COL):
                    sub_matrix[c] += matrix[r2][c]
                total_subarr += subarrSumTarget(sub_matrix, target)
        
        return total_subarr
                
            
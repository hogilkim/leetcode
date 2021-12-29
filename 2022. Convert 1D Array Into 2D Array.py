class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # row, col = m, n
        
        if m*n != len(original):
            return []
        
        result = []
        i=0
        for row in range(m):
            partial_result = []
            for col in range(n):
                partial_result.append(original[i])
                i += 1
            result.append(partial_result)
        
        return result
import collections
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        ROW, COL = len(mat), len(mat[0])
        dic = collections.defaultdict(list)
        
        if not mat: return res
        
        for i in range(ROW):
            for j in range(COL):
                dic[i+j].append(mat[i][j])
        
        
        for k in range(ROW+COL-1):
            if k %2 == 0:
                res += dic[k][::-1]
            else:
                res += dic[k]
        
        
        return res
                           
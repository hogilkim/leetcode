class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        for i in range(1, numRows):
            part = []
            
            if len(ans[-1]) == 1:
                ans.append([1,1])
            else:
                part.append(1)
                for j in range(len(ans[-1]) - 1):
                    part.append(ans[-1][j] + ans[-1][j+1])
                part.append(1)
                ans.append(part)
        return ans
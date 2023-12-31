# Solve again
# Dec 30, 2023 779-2 
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]

        for row in range(query_row + 1):
            nxt = [0]*(row+2)
            cups = row+1

            for col in range(cups):
                if curr[col]>=1:
                    nxt[col] += (curr[col]-1)/2
                    nxt[col+1] += (curr[col]-1)/2
                    curr[col] = 1
                
            if row != query_row: curr = nxt
        

        return curr[query_glass]


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]
        
        for i in range(query_row + 1):
            nxt = [0] * (i+2)
            
            for j in range(i+1):
                if curr[j] >= 1:
                    nxt[j] += (curr[j] - 1)/2.0
                    nxt[j+1] += (curr[j] - 1)/2.0
                    curr[j] = 1
            
            if i != query_row: curr = nxt
        return curr[query_glass]
            
            
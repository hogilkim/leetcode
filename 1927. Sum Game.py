# Solve again Jan 16, 2024 1927
class Solution:
    def sumGame(self, num: str) -> bool:
        q_cnt1 = 0; n_cnt1 = 0
        
        for char in num[:len(num)//2]:
            if char == "?": q_cnt1 += 1
            else: n_cnt1 += int(char) 
        
        q_cnt2 = 0; n_cnt2 = 0
        for char in num[len(num)//2:]:
            if char == "?": q_cnt2 += 1
            else: n_cnt2 += int(char)
        
        numdiff = n_cnt1 - n_cnt2
        qdiff =  q_cnt2 - q_cnt1
        return not (qdiff%2 == 0 and numdiff == qdiff//2 * 9)
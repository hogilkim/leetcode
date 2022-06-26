class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total_sum = sum(cardPoints)
        sub_len = len(cardPoints) - k
        if not sub_len: return total_sum
        
        curr_sum = 0
        l = 0
        min_sum = float('inf')
        
        for r in range(len(cardPoints)):
            curr_sum += cardPoints[r]
            
            if r -l+1 == sub_len:
                min_sum = min(min_sum, curr_sum)
                curr_sum -= cardPoints[l]
                l += 1
                

        
        return total_sum - min_sum
            
            
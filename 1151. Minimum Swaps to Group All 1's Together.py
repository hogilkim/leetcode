# solve again
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_of_one = sum(data)
        left, right = 0 , num_of_one-1
        
        
        window_count = 0
        for i in range(num_of_one):
            if data[i]: window_count += 1
        
        min_move = num_of_one - window_count
        
        while right < len(data)-1:
            right += 1
            if data[right]:
                window_count += 1
            if data[left]:
                window_count -= 1
            left += 1
            min_move = min(min_move, num_of_one - window_count)
        
        return min_move
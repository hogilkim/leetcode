# SOLVE AGAIN

import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        fruits_sum = 0
        basket = collections.Counter()
        left_ptr = 0
        
        for right_ptr in range(len(fruits)):
            basket[fruits[right_ptr]] += 1
            while len(basket) > 2:
                basket[fruits[left_ptr]]-=1
                if not basket[fruits[left_ptr]]:
                    basket.pop(fruits[left_ptr])
                left_ptr += 1
            fruits_sum = max(fruits_sum, right_ptr - left_ptr + 1)
                    
        return fruits_sum
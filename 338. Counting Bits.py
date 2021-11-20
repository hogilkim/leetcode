class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def helper(num):
            num_of_1 = 0
            while num:
                num_of_1 += num%2
                num = num//2
                
            return num_of_1
        
        return [helper(i) for i in range(n+1)]
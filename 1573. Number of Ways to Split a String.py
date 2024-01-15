#Jan 15, 2024 1573
import math
class Solution:
    def numWays(self, s: str) -> int:
        ones_idx = []
        MOD = 10**9+7
        for idx, char in enumerate(s):
            if char == "1":
                ones_idx.append(idx)

        if len(ones_idx) % 3 != 0:
            return 0
        
        if not ones_idx:
            return math.comb(len(s)-1,2) % MOD
        
        first_start = ones_idx[len(ones_idx)//3-1]
        first_end = ones_idx[len(ones_idx)//3]
        second_start = ones_idx[len(ones_idx)//3*2-1]
        second_end = ones_idx[len(ones_idx)//3*2]

        return ( (first_end - first_start) * (second_end - second_start) ) % MOD

        

        
# Solve again Jan 12, 2024 2217
import math
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        HALFLEN = math.ceil(intLength/2)
        BASE = 10**(HALFLEN-1)

        def get_palin(query):
            val = str(BASE + query - 1)
            if len(val) > HALFLEN: return - 1

            if intLength%2 == 1:
                return int(val+val[-2::-1])
            else:
                return int(val + val[::-1])
        
        return [get_palin(query) for query in queries]
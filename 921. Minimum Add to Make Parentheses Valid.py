class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        count = 0
        for char in s:
            if char == ')':
                if opening < 1: 
                    count += 1
                else:
                    opening -= 1
            
            else:
                opening += 1
        
        return opening + count
            
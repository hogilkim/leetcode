# Solve again Jan 24, 2024 386
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        
        def recursive(num):
            res.append(num)

            if num*10 <= n:
                recursive(num*10)
            
            if num+1 <= n and int(str(num)[-1]) < 9:
                recursive(num+1)
        
        recursive(1)
        return res
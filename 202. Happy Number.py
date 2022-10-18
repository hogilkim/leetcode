class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n:
            n = str(n)
            n = sum( int(n[i])**2 for i in range(len(n)) )
            
            if n in visited: return False
            visited.add(n)
            if n == 1: return True
            
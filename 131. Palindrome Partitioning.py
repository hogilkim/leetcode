class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Solve again
        # Brute Force Solution O(2^n)
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
            for j in range(i, len(s)):
                if self.isPal(i, j, s): 
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res
        
    
    def isPal(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right - 1
        return True
            
            
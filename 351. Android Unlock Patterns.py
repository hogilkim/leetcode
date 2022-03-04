class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        obstacles = {(1,3):2, (1,7):4, (1,9):5, (2,8):5, (3,7):5, (3,1):2, (3,9):6, (4,6):5, (6,4):5, (7,1):4, (7,3):5, (7,9):8, (8,2):5, (9,7):8, (9,3):6, (9,1):5}
        
        res = 0
        path = set()
        
        def backtracking(dot, num):
            nonlocal res
            if dot in path: return
            if num > n: return
            if num >= m: res += 1
            
            path.add(dot)
            
            for nxt in range(1, 10):
                if (dot, nxt) in obstacles and \
                obstacles[(dot,nxt)] not in path:
                    continue
                backtracking(nxt, num+1)
                
            path.remove(dot)
        
        
        for i in range(1,10):
            backtracking(i, 1)

        return res
class Solution:
    def confusingNumberII(self, n: int) -> int:

        rotate = [[0,0], [1,1], [6,9], [8,8], [9,6], ]
        
        self.res = 0
        def dfs(num, rotatedNum, unit):
            if num != rotatedNum: self.res += 1

            for d, rd in rotate:
                if d == 0 and num == 0: continue
                if num*10 + d > n: break
                dfs(num*10 + d, rotatedNum + rd*unit, unit*10)
        
        dfs(0,0,1)
        return self.res
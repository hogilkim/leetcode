from collections import deque
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # bfs solution - beats 91%
        queue = collections.deque([ (1, i) for i in range(1,10) ])
        
        res = []
        
        while queue:
            length, num = queue.popleft()
            
            if length == n: res.append(num)
            else:
                for i in range(10):
                    if abs(num%10 - i) == k:
                        queue.append((length + 1, num*10+i))
        return res
    
    
        # dfs solution - accepted beats 40 %
        LEN = n
        K = k
        res = []
        def dfs(num):
            if len(num) == LEN: 
                res.append(int("".join(num)))
                return
                
            # first digit
            if not len(num):
                for i in range(1, 10):
                    num.append(str(i))
                    dfs(num)
                    num.pop()
            
            # second digit ~ nth digit
            else:
                last_digit = int(num[-1])
                
                if last_digit + K < 10:
                    num.append(str(last_digit + K))
                    dfs(num)
                    num.pop()
                
                if K and 0<=last_digit - K <10:
                    num.append(str(last_digit-K))
                    dfs(num)
                    num.pop()
            
        
        dfs([])
        return res
                

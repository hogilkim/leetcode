class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = list(s)
        while len(s)>1:
            if s[-1] == "1":
                while s and s[-1] == "1": 
                    s.pop()
                    steps+=1
                if s: 
                    s[-1] = "1"
                    steps+=1
                else: 
                    s.append("1")
                    steps+=1
            elif s[-1] == "0":
                while s and s[-1] == "0":
                    s.pop()
                    steps += 1
        
        return steps
                

from collections import defaultdict
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        OPEN, CLOSE = "(", ")"
        state_dic = defaultdict(int)
        state_dic["("] = 1
        state_dic[")"] = -1


        res = []
        
        visited = set()
        
        maxlen = 0
        
        def backtracking(i, state, string):
            if string in visited: return
            if i == len(s):
                nonlocal maxlen, res
                if state != 0 or len(string) < maxlen: return
                
                if len(string)>maxlen:
                    maxlen = len(string)
                    res = []
                res.append(string)
                return
            
            # include i
            
            if state >= 0:
                backtracking(i+1, state+state_dic[s[i]], string+s[i])
            
            
            # X include i
            backtracking(i+1, state, string)
            
            visited.add(string)
        
        backtracking(0,0,"")
        
        return res
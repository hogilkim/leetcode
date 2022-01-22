class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        
        i = 0
        while i < len(s):
            if s[i] =='(':
                stack.append('(')
            
            elif s[i] == ')':
                if not stack:
                    s = s[:i] + s[i+1:]
                    continue
                else:
                    stack.pop()
            i+=1
        
            
        i = len(s)-1
        while stack:
            if s[i] == '(':
                s = s[:i] + s[i+1:]
                stack.pop()
            i -= 1
        
        return s
import collections
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        splitted = path.split('/')
        
        sp_deque = collections.deque(splitted)
        
        buffer = []
        
        while sp_deque:
            popped = sp_deque.popleft()
            
            if not popped or popped == '.':
                continue
            
            if popped == "..":
                if buffer:
                    buffer.pop()
            
            else:
                buffer.append(popped)
                
        
        ans = ""
        
        for file in buffer:
            ans+= '/' + file
        
        return ans if ans else "/"
                
                
        
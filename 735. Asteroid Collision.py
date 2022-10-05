# second attempt: solved
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        
        for ast in asteroids[1:]:
            while stack and stack[-1] > 0 and ast < 0:
                last = stack.pop()
                if last > -ast:
                    ast = 0
                    stack.append(last)
                elif last + ast == 0: ast = 0
                    
                
            
            if ast != 0:
                stack.append(ast)
        
        return stack
            

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] == -ast:
                    stack.pop()
                    break
                elif stack[-1] > -ast:
                    break
                elif stack[-1] < -ast:
                    stack.pop()
            
            else:
                stack.append(ast)
        
        return stack
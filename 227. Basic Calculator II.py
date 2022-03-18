import collections
class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        calc = 0
        
        for idx, char in enumerate(s):
            if '0'<=char<='9':
                stack[-1] = stack[-1] * 10 + int(char)
            if char in "/*+-" or idx == len(s)-1:
                if len(stack) >= 3:
                
                    right = stack.pop()
                    operator = stack.pop()
                    left = stack.pop()
                    if operator == "/":
                        calc = left//right
                        stack.append(calc)
                    elif operator == "*":
                        calc = right*left
                        stack.append(calc)
                    else:
                        stack += [left,operator,right]
                if idx < len(s)-1:
                    stack.append(char)
                    stack.append(0)
        deque = collections.deque(stack)
        
        while len(deque) > 1:
            left = deque.popleft()
            operator = deque.popleft()
            right = deque.popleft()
            
            if operator == "+":
                deque.appendleft(left + right)
            elif operator == "-":
                deque.appendleft(left - right)
            
        return deque[0]
class Solution:
    def calculate(self, s: str) -> int:
        s = list(s)
        
        def update(op, num):
            if op == "+": stack.append(num)
            elif op == "-": stack.append(-num)
                
        stack = [0]
        op = "+"
        curr = 0
        opset = set("+-")
        
        for char in s+['+']:
            
            if char == "(": 
                stack.append(op)
                curr = 0
                op = "+"
                
            elif char in opset:
                update(op, curr)
                curr = 0
                op = char
                
            elif char == ")":
                update(op, curr)
                curr = 0
                temp = 0
                while stack[-1] not in opset:
                    temp += stack.pop()
                update(stack.pop(), temp)
                
            elif char.isdigit():
                curr = curr*10 + int(char)
            
        
        return sum(stack)
            
            
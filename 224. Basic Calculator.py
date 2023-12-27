# Dec 27, 2023 244-3
class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        def calc(num, op):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
        
        operators = ['+', '-']
        op = "+"
        currnum = 0

        for char in s+'+':
            if char in operators:
                calc(currnum, op)
                op = char
                currnum = 0
            elif char.isdigit():
                currnum = currnum*10 + int(char)
            
            elif char == "(":
                currnum = 0
                stack.append(op)
                op = '+'

            elif char == ')':
                tempnum = 0
                calc(currnum, op)
                while stack and stack[-1] not in operators:
                    tempnum += stack.pop()
                calc(tempnum, stack.pop())
                op = '+'
                currnum = 0
        
        return sum(stack)


# second Nov 20, 2022 
class Solution:
    def calculate(self, s: str) -> int:
        s = list(s)
        stack = []
        
        def calc(op, num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
        
        operators = ["+","-"]
        op = "+"
        num = 0
        
        for char in s+["+"]:
            
            if char in operators:
                calc(op, num)
                op = char
                num = 0
            elif char.isdigit():
                num = num*10 + int(char)
            
            elif char == "(":
                stack.append(op)
                op = "+"
                num = 0
                
            elif char == ")":
                calc(op, num)
                op = "+"
                num = 0
                temp = 0
                while stack[-1] not in operators:
                    temp += stack.pop()
                
                temp_op = stack.pop()
                calc(temp_op, temp)
                
            # print(char, stack)
        
                
        return sum(stack)


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
            
            
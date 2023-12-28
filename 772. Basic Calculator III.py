# Dec 27, 2023 772-3
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        def calc(num, op):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop()*num)
            elif op == '/':
                stack.append(int(stack.pop()/num))
        

        ops = list("+-*/")
        prev_op = "+"
        num = 0
        for char in s+"+":
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in ops:
                calc(num, prev_op)
                prev_op = char
                num = 0
            
            elif char == "(":
                stack.append(prev_op)
                prev_op = '+'
                num = 0
            
            else:
                calc(num, prev_op)
                num = 0
                prev_op = ')'

                tempnum = 0
                while stack[-1] not in ops:
                    tempnum += stack.pop()
                calc(tempnum, stack.pop())
                
        return sum(stack)

class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(num, operator):
            if operator == "+":
                # append num stack
                stack.append(num)
            # if -
            elif operator == "-":
                # append -num2 stack
                stack.append(-num)
            # if * 
                # append stack[-1]*num
            elif operator == "*":
                stack.append(stack.pop()*num)
                
            # if /
            elif operator == "/":
                stack.append(int(stack.pop()/num))
                # append stack[-1]/num
            

        
        stack =[]
        
        prev_op = "+"
        num = 0
        ops = list("+-/*")
        
        for char in s+"+":
            # if digit
            if char.isdigit():
                num = 10*num + int(char)
            
            elif char in ops:
                # call helper func (prev_op, num)
                helper(num, prev_op)
                
                prev_op = char
                num = 0
            
            # if char (
            elif char == "(":
                # append num
                # stack.append(num)
                num = 0
                # append operator & prev_op = "+"
                stack.append(prev_op)
                prev_op = "+"
                
            # if char )
            elif char == ")":
                helper(num, prev_op)
                num = 0
                prev_op = ")"
                
                temp =0
                while stack[-1] not in ops:
                    temp += stack.pop()
                helper(temp, stack.pop())
    
        return sum(stack)
                
                
                
            
            


class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op == "+": stack.append(num)
            elif op == "-": stack.append(-num)
            elif op == "/": stack.append(int(stack.pop()/num))
            elif op == "*": stack.append(stack.pop()*num)
                
        
        stack = []
        op = "+"
        num = 0
        opset=set('+-*/')    
        
        
        # when meet op,
        # use previous op
            # + or - -> append to stack
            # / or * -> pop, calculate and append
            # ) -> calcualte + until we meet op
        # then assign curr char to op
        
        # when meet num, update num
        
        # when meet (,
        # append op, initialize num
        
        for char in s+"+":
            if char.isdigit():
                num = num*10 + int(char)
            
            elif char in opset or char == ")":
                update(op, num)
                num = 0
                op = char
                if char == ")":
                    tempnum = 0
                    while stack[-1] not in opset:
                        tempnum += stack.pop()
                    update(stack.pop(), tempnum)
            elif char == "(":
                stack.append(op)
                op = "+"
                num = 0
        return sum(stack)
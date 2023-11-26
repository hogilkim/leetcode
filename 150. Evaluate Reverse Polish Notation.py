# Nov 26, 2023 150-2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "*/+-"

        def calc(num1, num2, op):
            if op == "*":
                return num1 * num2
            elif op == "/":
                return int(num1/num2)
            elif op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2
        
        stack = []
        for token in tokens:
            if token[0].isdigit():
                stack.append(int(token))

            elif token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calc(num1, num2, token))

            else:
                stack.append(-1 * int(token[1:]))

        return stack[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "/*+-"

        def calc(op):
            num2 = stack.pop()
            num1 = stack.pop()
            if op == '+':
                stack.append(num1+num2)
            elif op == '-':
                stack.append(num1-num2)
            elif op == '*':
                stack.append(num1*num2)
            elif op == '/':
                stack.append(int(num1/num2))
        
        for string in tokens:
            if string[0].isdigit():
                stack.append(int(string))

            elif string in operators:
                calc(string)
            
            elif string[0] == "-":
                stack.append(-int(string[1:]))
                    
        return stack[-1]
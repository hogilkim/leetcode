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
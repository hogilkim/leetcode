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
class MyQueue:

    def __init__(self):
        self.pushing_stack = []
        self.popping_stack = []

    def push(self, x: int) -> None:
        self.pushing_stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.popping_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.popping_stack[-1]

    def empty(self) -> bool:
        if self.pushing_stack or self.popping_stack:
            return False
        return True
        
    def move(self):
        if not self.popping_stack:
            while self.pushing_stack:
                self.popping_stack.append(self.pushing_stack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
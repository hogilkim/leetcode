class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.data = [0]*k
        self.front = 0
        self.back = -1
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.back = (self.back+1)%self.max_size
        self.data[self.back] = value
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        if self.front == self.back:
            self.front = 0
            self.back = -1
        else:
            self.front = (self.front+1)%self.max_size

        return True
    
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.front]
    
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.back]
    
    def isEmpty(self) -> bool:
        return self.back == -1

    
    def isFull(self) -> bool:
        return self.back != -1 and (self.back+1)%self.max_size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
import heapq
class MaxStack:

    def __init__(self):
        self.stack = []
        self.id = 0
        self.max_heap = []
        self.mh_popped = set()
        self.st_popped = set()
        
        
        heapq.heapify(self.max_heap)
        
    def push(self, x: int) -> None:
        self.stack.append((x, self.id))
        heapq.heappush(self.max_heap, (-x, -self.id))
        self.id+=1
        
    def pop(self) -> int:
        while self.stack[-1][1]  in self.mh_popped:
            self.stack.pop()
        
        item, pid = self.stack.pop()
        self.st_popped.add(pid)
        return item

    def top(self) -> int:
        while self.stack[-1][1] in self.mh_popped:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while -self.max_heap[0][1] in self.st_popped:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        
        while -self.max_heap[0][1] in self.st_popped:
            heapq.heappop(self.max_heap)
        
        item, pid = heapq.heappop(self.max_heap)
        self.mh_popped.add(-pid)
        
        return -1*item

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
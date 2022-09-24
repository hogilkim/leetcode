import heapq
class ExamRoom:
    def distance(self, x, y):
        if x == -1: 
            return -y
        elif y == self.N:
            return -(self.N - x - 1)
        else:
            return -(abs(x-y)//2)
        
    def __init__(self, n: int):
        self.N = n
        self.heap = [(self.distance(-1, self.N), -1, self.N)]
        heapq.heapify(self.heap)
        
    def seat(self) -> int:
        _, x, y = heapq.heappop(self.heap)
        
        if x == -1:
            seat = 0
        elif y == self.N:
            seat = self.N-1
        else:
            seat = (x+y)//2
        
        heapq.heappush(self.heap, (self.distance(x, seat), x, seat))
        heapq.heappush(self.heap, (self.distance(seat, y), seat, y))
        
        return seat
        
    def leave(self, p: int) -> None:
        head = tail = None
        
        for interval in self.heap:
            if interval[2] == p: head = interval
            elif interval[1] == p: tail = interval
            if head and tail: break
        
        self.heap.remove(head)
        self.heap.remove(tail)
        heapq.heapify(self.heap)
        new_x, new_y = head[1], tail[2]
        heapq.heappush(self.heap, (self.distance(new_x, new_y), new_x, new_y))

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
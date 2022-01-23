import bisect
class MyCalendar:

    def __init__(self):
        self.items = []

    def book(self, start: int, end: int) -> bool:
        start_index = bisect.bisect_right(self.items, start)
        end_index = bisect.bisect_left(self.items, end)
        
        if start_index != end_index or start_index%2:
            return False
        
        
        self.items.insert(start_index, start)
        self.items.insert(start_index+1, end)
        return True
            
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
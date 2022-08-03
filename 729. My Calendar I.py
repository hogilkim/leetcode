# Bisect library implementation
class MyCalendar:

    def __init__(self):
        self.items = []

    def book(self, start: int, end: int) -> bool:
        if not self.items: 
            self.items.append(start); self.items.append(end);
            return True
        
        left, right = self.binary_right(start), self.binary_left(end)
        if left!=right or left%2: return False
        
        self.items.insert(left, start)
        self.items.insert(left+1,end)
        return True
        
        
        
    def binary_left(self, num):
        l, r = 0, len(self.items)
        
        while l < r:
            mid = (l+r)//2
            
            if self.items[mid] < num:
                l = mid + 1
            else:
                r = mid
        return l
    
    def binary_right(self,num):
        l, r = 0, len(self.items)
        while l < r:
            mid = (l+r)//2
            
            if self.items[mid] <= num:
                l = mid + 1
            else:
                r = mid
        return l
        
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# ====
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
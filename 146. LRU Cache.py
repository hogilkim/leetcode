# second time
class Node:
    def __init__(self, key=-1, val=-1, nxt=None, prev = None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev
        
class LRUCache:
    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.size = capacity
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insertlast(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        elif len(self.cache) == self.size:
            delkey = self.left.next.key
            self.remove(self.left.next)
            del self.cache[delkey]
        
        
        new = Node(key,value)
        self.insertlast(new)
        self.cache[key] = new
        
    def insertlast(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node
        
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:
# Solve Again
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # Least Recently Used
        self.left = Node(0, 0)
        # Most Recently Used
        self.right = Node(0,0)
        
        self.left.next, self.right.prev = self.right, self.left
        
    # remove from linked list
    def remove(self, removing_node):
        prev, nxt = removing_node.prev, removing_node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, inserting_node):
        #insert to right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = inserting_node
        inserting_node.next, inserting_node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
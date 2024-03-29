import random
class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.num_map = {}
    def insert(self, val: int) -> bool:
        res = val not in self.num_map
        
        if val not in self.num_map:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
        
        return res

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if val in self.num_map :
            popidx = self.num_map[val]
            self.num_list[popidx] = self.num_list[-1]
            self.num_map[self.num_list[-1]] = popidx
            self.num_list.pop()
            del self.num_map[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

import random
class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        res = val not in self.num_map
        if res:
            self.num_map[val] = len(self.num_list)
            self.num_list.append(val)
        return res
            

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if res:
            idx = self.num_map[val]
            last_val = self.num_list[-1]
            self.num_map[last_val] = idx
            self.num_list[idx] = last_val
            self.num_list.pop()
            del self.num_map[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
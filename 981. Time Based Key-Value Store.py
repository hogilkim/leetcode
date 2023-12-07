# Dec 7, 2023 981
# Solve again

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key_val = defaultdict(list)
        self.key_time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_val[key].append(value)
        self.key_time[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_time[key]: return ""
        if timestamp < self.key_time[key][0]: return ""
        
        l, r = 0, len(self.key_time[key])-1
        found = None
        while l <= r:
            mid = (l+r)//2

            if self.key_time[key][mid] < timestamp:
                l = mid + 1
            elif self.key_time[key][mid] > timestamp: 
                r = mid - 1
            else:
                found = mid
                break
        
        if found != None: return self.key_val[key][found]
        return self.key_val[key][l-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# t = 4
# l   m   r
# l r
# m
# l r
# 1 3 5 7 9
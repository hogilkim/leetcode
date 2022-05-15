import collections
class FreqStack:

    def __init__(self):
        self.val_freq = collections.Counter()
        self.freq_vals = collections.defaultdict(list)
        self.max_freq = 0
    def push(self, val: int) -> None:
        self.val_freq[val] += 1
        
        self.max_freq = max(self.max_freq, self.val_freq[val])
        
        self.freq_vals[self.val_freq[val]].append(val)

    def pop(self) -> int:
        if not self.freq_vals[self.max_freq]:
            self.max_freq -= 1
        popping = self.freq_vals[self.max_freq].pop()
        self.val_freq[popping] -= 1
        return popping
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
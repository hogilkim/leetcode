class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.num = len(self.w)
        for i in range(1,self.num):
            self.w[i] += self.w[i-1]
        
        self.until = self.w[-1]
        
    def pickIndex(self) -> int:
        rand = random.randint(1, self.until)
        
        l, r = 0, self.num-1
        while l < r:
            mid = (l+r)//2
            
            if rand <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
class Solution:
    def mySqrt(self, x: int) -> int:
        
        l,r = 1, x
        
        while l <= r:
            mid = (l+r)//2
            squared = mid*mid
            
            if squared < x: l = mid + 1
            elif squared > x: r = mid - 1
                
            else: return mid
        
        return r
        
#         if x == 1 or not x: return x
        
#         for i in range(1, x//2 + 2):
#             if i*i == x: return i
#             elif i*i > x: return i -1
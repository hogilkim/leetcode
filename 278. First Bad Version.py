#Nov 12, 2023 278-2

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 1, n

        while l < r:
            mid = (l+r)//2

            if isBadVersion(mid):
                r = mid
            
            else:
                l = mid + 1
        
        return l

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left<right:
            mid = (right+left)//2
            
            if isBadVersion(mid): right = mid
            else: left = mid + 1
        
        return right
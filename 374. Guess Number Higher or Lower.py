# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, low = 0) -> int:
        mid = (n+low)//2
        updown = guess(mid)
        
        if updown == 0: return mid
        elif updown == 1: return self.guessNumber(n, mid+1)
        else: return self.guessNumber(mid-1,0)
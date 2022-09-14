#also solve 31. next permutation
class Solution:
    def nextPalindrome(self, num: str) -> str:
        mid = ""
        if len(num) <=1: return ""
        if len(num)%2: mid = num[len(num)//2]
        first_half = list(num[:len(num)//2])
        
        
        i = len(first_half) - 1
        
        while i > 0 and first_half[i-1] >= first_half[i]:
            i -= 1
            
        if i == 0: return ""
        
        j = len(first_half) -1
        k = i - 1
        
        while first_half[k] >= first_half[j]: j -= 1
        first_half[k], first_half[j] = first_half[j], first_half[k]
        
        # first_half[k+1:] = sorted(first_half[k+1:]) # this is also correct
        # OR this is equal to the above (sorting [k+1:])
        l,r = k+1, len(first_half)-1
        
        while l < r:
            first_half[l], first_half[r] = first_half[r], first_half[l]
            l += 1
            r -= 1
        
        
        first_half = "".join(first_half)
        return first_half + mid + first_half[::-1]
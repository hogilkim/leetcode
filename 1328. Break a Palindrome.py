class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1: return ""
        palindrome = list(palindrome)
        ptr = 0
        
        while ptr < len(palindrome) and palindrome[ptr] == "a":
            ptr+=1
            if len(palindrome)%2 and ptr == len(palindrome)//2:
                ptr+=1
        
        if ptr < len(palindrome): 
            palindrome[ptr] = "a"
            return "".join(palindrome)
        
        palindrome[-1] = "b"
        return "".join(palindrome)
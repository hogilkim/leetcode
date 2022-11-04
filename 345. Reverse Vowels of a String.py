class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        s=list(s)
        for char in s:
            if char in "aeiouAEIOU": stack.append(char)
        
        res = [stack.pop() if char in "aeiouAEIOU" else char for char in s ]
        
        return "".join(res)
        
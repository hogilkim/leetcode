class Solution:
    def confusingNumber(self, n: int) -> bool:
        dic = {
            "1":"1", "0":"0","6":"9","8":"8","9":"6"
        }

        newnum = ""
        for char in str(n):
            if char not in dic: return False
            newnum+=dic[char]
        
        return newnum[::-1] != str(n)
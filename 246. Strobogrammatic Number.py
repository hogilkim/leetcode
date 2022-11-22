class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {
            "0":"0", "1":"1", "6":"9", "9":"6","8":"8"
        }
        num = list(num)
        l, r = 0, len(num)-1
        
        while l <= r:
            if num[l] in dic and num[r] == dic[num[l]]:
                l+=1
                r-=1
            else:
                return False
        
        return True
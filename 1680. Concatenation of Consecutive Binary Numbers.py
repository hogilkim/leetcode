class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = ""
        for i in range(1,n+1):
            num+=format(i,"b")
        return int(num,2)%(10**9 + 7)
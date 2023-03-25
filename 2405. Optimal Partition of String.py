class Solution:
    def partitionString(self, s: str) -> int:
        charset = set()
        partitions = 1
        for char in s:
            if char in charset:
                partitions+=1
                charset = set()
            charset.add(char)
        
        return partitions
import collections
class Solution:
    def maximumSwap(self, num: int) -> int:
        
        max_indices = {i: 0 for i in range(10)}
        str_num = str(num)
        
        for index, number in enumerate(str_num):
            max_indices[int(number)] = max(max_indices[int(number)], index)
        
        
        for i, n in enumerate(str_num):
            for x in range(9, int(n), -1):
                if i < max_indices[x]:
                    l = list(str_num)
                    l[i], l[max_indices[x]] = l[max_indices[x]], l[i]
                    return int("".join(l))        
        return num
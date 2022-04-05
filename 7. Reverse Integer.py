class Solution:
    def reverse(self, x: int) -> int:
        sign = [-1,1][x>0]
        
        res = sign * int(str(abs(x))[::-1])
        return res if -(2**31)-1 < res < 2**31 else 0
#         sign = "" if x > 0 else "-"
        
#         if x < 0:
#             x *= -1
        
#         num_list = list(str(x))
#         while num_list and num_list[-1] == "0":
#             num_list.pop()
#         if not num_list: return 0
#         res = int(sign + "".join(num_list[::-1]))
#         return res if -(2**31)-1 < res < 2**31 else 0
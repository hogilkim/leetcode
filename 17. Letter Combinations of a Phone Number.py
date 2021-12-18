#solve again
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # second solution
        res = []
        digit_to_alphabet = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def dfs(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for char in digit_to_alphabet[digits[i]]:
                dfs(i+1, curr_str+char)
            
        if digits:
            dfs(0,"")

        return res        
#         digit_to_alphabet = []
#         alphabets = "abcdefghijklmnopqrstuvwxyz"
#         for digit in digits:
#             if int(digit) < 7:
#                 digit_to_alphabet.append(alphabets[3* (int(digit)-2) : 3*(int(digit)-1) ])
#             elif int(digit) == 7:
#                 digit_to_alphabet.append("pqrs")
#             elif int(digit) == 8:
#                 digit_to_alphabet.append("tuv")
#             else:
#                 digit_to_alphabet.append("wxyz")
        
#         if digit_to_alphabet:
#             result = digit_to_alphabet[0]
#         else:
#             return []
        
#         for i in range(1, len(digit_to_alphabet)):
#             temp = set(result)
#             result = []
#             for c1 in digit_to_alphabet[i]:
#                 for c2 in temp:
#                     result.append(c2+c1)
        
#         return set(result)
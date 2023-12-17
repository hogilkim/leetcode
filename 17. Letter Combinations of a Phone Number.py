# solved 
# third attempt - Dec 17, 2023 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        
        if not digits: return []
        def backtracking(idx, dgs, comb):
            if idx >= len(dgs):
                res.append(comb)
                return
            
            for char in digit_to_alphabet[dgs[idx]]:
                backtracking(idx+1, dgs, comb+char)
        
        backtracking(0, digits, "")
        return res
    
# solved 
# second attempt - Jan 15, 2022
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        
        def backtracking(part):
            if len(part) == len(digits):
                res.append(part)
                return
            
            index = len(part)
            
            for char in digit_to_alphabet[digits[index]]:
                part += char
                backtracking(part)
                part = part[:-1]
            
        if digits:
            backtracking("")
        return res

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
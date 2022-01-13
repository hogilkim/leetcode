# solved!
# Jan 13, 2022
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        result = []
        
        def backtracking(part, i):
            if i >= len(s): 
                result.append(part)
                return
                
            if "0" <= s[i] <="9":
                backtracking(part + s[i], i + 1)
            else:
                # lowercase
                backtracking(part+s[i].lower(), i+1)
                
                # uppercase
                backtracking(part+s[i].upper(), i+1)
            
            
            
        backtracking("", 0)
        
        return result
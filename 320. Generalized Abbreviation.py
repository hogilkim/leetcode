# solved
# first attempt - Jan 18, 2022
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        
        result = []
        
        def backtracking(part, i, prev):
            # result
            if i >= len(word):
                if prev>0:
                    part += str(prev)
                result.append(part)
                return
            
            # add char
            case1 = part
            if prev > 0:
                case1 += str(prev)
            case1 += word[i]
            
            backtracking(case1, i+1, 0)
            
            
            # add number
            prev += 1
            backtracking(part, i+1, prev)
            
        
        backtracking("", 0, 0)
        
        return result
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        num = 0
        for char in abbr:
            if "0" <= char <= "9":
                if not num and char == "0": return False
                num = num * 10 + int(char)
            
            elif num and "a" <= char <= "z":
                i += num 
                # print(char, word[i], i)
                if i > len(word) -1 or word[i] != char: return False
                num = 0
                i += 1
            # not num and char
            else:
                # print("else", char, word[i], i)
                
                if i > len(word) -1 or word[i] != char: return False
                i += 1
                
        if num: i += num
        # print(i)
        return True if i == len(word) else False
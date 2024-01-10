# Solve again, Jan 10, 2024 
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = " ".join(sentence) + " "
        valid_spaces = 0

        rows_one_block = 0

        for r in range(rows):
            rows_one_block = r
            valid_spaces += cols
            
            while sentence[valid_spaces%len(sentence)] != " ": valid_spaces -= 1

            if valid_spaces%len(sentence) == 0:
                break

            valid_spaces += 1
                
        return ((valid_spaces+1) // len(sentence)) * (rows // (rows_one_block+1))

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = " ".join(sentence) + " "
        valid_spaces = 0

        for _ in range(rows):
            valid_spaces += cols
            while sentence[valid_spaces%len(sentence)] != " ": valid_spaces -= 1
            valid_spaces += 1
        
        return valid_spaces // len(sentence)
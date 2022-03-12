class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        
        i = 0
        n = len(words)
        
        while i < n:
            j = i + 1
            line_len = len(words[i])
            
            while j < n and line_len + len(words[j]) + (j-i-1) < maxWidth:
                line_len += len(words[j])
                j += 1
            
            diff = maxWidth - line_len
            num_of_words = j - i
            
            if num_of_words == 1 or j >= n:
                res.append(self.leftJustify(words, diff, i, j))
            else:
                res.append(self.middleJustify(words,diff,i,j))
            
            i = j
        
        return res
    
    
    def leftJustify(self, words, diff, i, j):
        spaces_on_right = diff - (j - i - 1)
        
        res = " ".join(words[i:j])
        
        res += " "*spaces_on_right
        
        return res
    
    def middleJustify(self, words, diff, i, j):
        spaces_needed = j - i - 1
        spaces = diff // spaces_needed
        extra_spaces = diff % spaces_needed
        
        res = words[i]
        
        for k in range(i+1, j):
            spaces_to_apply = spaces
            if extra_spaces:
                spaces_to_apply += 1
                extra_spaces -= 1
            res += " "*spaces_to_apply + words[k]
        
        return res
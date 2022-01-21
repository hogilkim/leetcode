# solve again
# First Attempt - Jan 20, 2022 
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    
        words = set(words)
        
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words and suffix in words:
                    memo[word] = True
                    break
                if prefix in words and dfs(suffix):
                    memo[word] = True
                    break
            return memo[word]
        
        return [word for word in words if dfs(word)]
import collections
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        lex_dic = collections.defaultdict(set)
        LEN = len(s1)
        
        for i in range(LEN):
            lex_dic[s1[i]].add(s2[i])
            lex_dic[s2[i]].add(s1[i])
        res = []
        
        
        memo = {}
        def dfs(char, visited):
            if char in memo: return memo[char]
            visited.add(char)
            res = char
            for ch in lex_dic[char]:
                if ch not in visited: 
                    res = min(res, dfs(ch, visited))
            
            return res
                
        
        for char in baseStr:
            visited = set()
            min_char = dfs(char, visited)
            res.append(min_char)
            for c in visited: memo[c] = min_char
        return "".join(res)
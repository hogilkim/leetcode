from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = collections.deque([(0,s1)])
        visited = set([s1])
        while queue:
            steps, string = queue.popleft()
            if string == s2: return steps
            
            i = 0
            while i < len(s1) and string[i] == s2[i]: i += 1
                
            for j in range(i+1, len(s2)):
                if string[j] != s2[i]: continue
                new_string = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                if new_string in visited: continue
                visited.add(new_string)
                queue.append((steps+1, new_string))
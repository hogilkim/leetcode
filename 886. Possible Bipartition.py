# solve again
from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes: return True
        NO_COLOR, RED, BLUE = 0,1,-1

        color_map = defaultdict(int)
        dislike_map = defaultdict(list)

        for p1, p2 in dislikes:
            dislike_map[p1].append(p2)
            dislike_map[p2].append(p1)

        def dfs(person, color):
            color_map[person] = color

            for xlikep in dislike_map[person]:
                if color_map[xlikep] == color: return False
                if color_map[xlikep] == NO_COLOR and not dfs(xlikep, -color): return False
            
            return True
        
        for person in range(1, n+1):
            if color_map[person] == NO_COLOR and not dfs(person, RED):
                return False
        
        return True

# solve again
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes: return True
        NO_COLOR, RED, BLUE = 0, 1, -1
        
        color_map = defaultdict(int)
        dislike_map = defaultdict(list)
        
        def dfs(person, color):
            color_map[person] = color
            
            for dislike_person in dislike_map[person]:
                
                if color_map[dislike_person] == color:
                    return False
                
                if color_map[dislike_person] == NO_COLOR and not dfs(dislike_person, -color):
                    return False
            
            return True
        
        for p1, p2 in dislikes:
            dislike_map[p1].append(p2)
            dislike_map[p2].append(p1)
        
        for person in range(1, n+1):
            if color_map[person] == NO_COLOR and not dfs(person, RED):
                return False
        return True
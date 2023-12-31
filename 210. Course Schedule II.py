# Solve again
# Dec 31, 2023 210-3
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        available_courses = defaultdict(list)

        for course, prereq in prerequisites:
            available_courses[course].append(prereq)
        
        res = []
        visited = set()
        path = set()

        def dfs(course):
            if course in path: return False
            if course in visited: return True

            visited.add(course)
            path.add(course)
            
            for prereq in available_courses[course]:
                if not dfs(prereq): return False

            res.append(course)
            path.remove(course)

            return True
        

        return res if all(dfs(course) for course in range(numCourses)) else []

# second try - solved!
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {num:[] for num in range(numCourses)}
        
        for a,b in prerequisites:
            prereqs[a].append(b)
            
        path = set()
        visited = set()
        res = []
        
        def dfs(course):
            if course in path: return False
            elif course in visited: return True

            
            path.add(course)
            
            for prereq in prereqs[course]:
                if not dfs(prereq): return False
            
            res.append(course)
            path.remove(course)
            visited.add(course)
            
            return True
        
        return res if all(dfs(course) for course in range(numCourses)) else []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = {i:[] for i in range(numCourses)}
        for prerequisite in prerequisites:
            prereq_map[prerequisite[0]].append(prerequisite[1])
        
        
        visited = set()
        cycle = set()
        result = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for prereq in prereq_map[crs]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return result
                
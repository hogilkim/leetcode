# third - solved
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            
        # declare sets visited & path
        visited = set()
        path = set()
        # build dictionary for next_courses
        next_courses = defaultdict(list)
        for c1, c2 in prerequisites:
            next_courses[c2].append(c1)
            
            
        def dfs(key):
            visited.add(key)
            path.add(key)
            # loop through dic[key]:
            for next_c in next_courses[key]:
                # if in path: return False
                if next_c in path: return False
                # not in visited, calll another dfs
                elif next_c not in visited:
                    if not dfs(next_c): return False
            
            path.remove(key)
            
            return True
        
        # for loop from 0 to n-1
        for c in range(numCourses):
            # call dfs
            if c not in visited:
                if not dfs(c): return False
        
        return True
        
        
# second attempt - solved!
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {num:[] for num in range(numCourses)}
        
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        visited = set()
        path = set()
        def dfs(course):
            if course in path: return False
            
            path.add(course)
            
            
            for prereq in prereqs[course]:
                if prereq not in visited:
                    if not dfs(prereq):
                        return False
                    
            path.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

#Try Again

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visitSet=set()
        def dfs(course):
            if course in visitSet: return False
            if preMap[course] ==[] : return True
            visitSet.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq): return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        return all(dfs(course) for course in range(numCourses))
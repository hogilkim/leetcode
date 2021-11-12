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
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
                
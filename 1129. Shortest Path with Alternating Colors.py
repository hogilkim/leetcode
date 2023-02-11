from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        blue = defaultdict(list)
        red = defaultdict(list)

        for v1, v2 in redEdges:
            red[v1].append(v2)
        for v1, v2 in blueEdges:
            blue[v1].append(v2)

        res = [-1]*n
        res[0] = 0

        queue = deque([(0,0,1), (0,0,-1)])
        visited = set()

        while queue:
            node, dis, color = queue.popleft()
            if res[node] == -1: res[node] = dis 
            visited.add((node,color))
            if color == 1:
                for nxt in red[node]:
                    if (nxt, color*-1) not in visited: queue.append((nxt,dis+1, color*-1))
            else:
                for nxt in blue[node]:
                    if (nxt, color*-1) not in visited: queue.append((nxt,dis+1, color*-1))
        
        return res
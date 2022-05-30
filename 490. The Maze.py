import collections
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = collections.deque([(start[0], start[1])])
        visited = set()
        visited.add((start[0],start[1]))
        
        ROW, COL = len(maze), len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        
        while queue:
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for r_dir, c_dir in directions:
                    n_r, n_c = r, c
                    while 0<=n_r+r_dir<ROW and 0<=n_c + c_dir < COL and maze[n_r+r_dir][n_c + c_dir]==0:
                        n_r += r_dir
                        n_c += c_dir
                        
                    if n_r == destination[0] and n_c == destination[1]:
                        return True
                    if (n_r,n_c) not in visited:
                        queue.append((n_r,n_c))
                        visited.add((n_r,n_c))
        
        return False
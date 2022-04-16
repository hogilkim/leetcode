import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = set()
        
        directions = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        
        bfs_queue = collections.deque([(0,0,0)])
        
        while bfs_queue:
            x_c, y_c, steps = bfs_queue.popleft()
            if x_c == x and y_c==y: return steps
            
            for x_dir,y_dir in directions:
                if (x_c + x_dir, y_c+y_dir) not in visited:
                    visited.add((x_c + x_dir, y_c+y_dir))
                    bfs_queue.append((x_c + x_dir, y_c+y_dir,steps+1))
        
        
        return -1
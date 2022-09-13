from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW, COL = len(rooms), len(rooms[0])
        queue = deque([])
        
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0: queue.append((r,c))
                    
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            x,y = queue.popleft()
            distance = rooms[x][y]
            
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < ROW and 0 <= new_y < COL and rooms[new_x][new_y] == 2147483647:
                    rooms[new_x][new_y] = distance + 1
                    queue.append((new_x,new_y))